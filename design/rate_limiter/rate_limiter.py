import time
import threading
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple


# ==========================================
# 1. Models & Data Structures
# ==========================================

@dataclass(frozen=True)
class RateLimitRule:
    """Defines the quota rule for a specific route or action."""
    max_requests: int
    window_seconds: int

@dataclass
class RateLimitResult:
    """The result returned to the client/middleware."""
    allowed: bool
    limit: int
    remaining: int
    retry_after: float  # Seconds to wait before retrying (if denied)


# ==========================================
# 2. Storage Strategy Interface & Implementations
# ==========================================

class StorageBackend(ABC):
    """Abstract interface for storage engines (Memory, Redis, Memcached)."""

    @abstractmethod
    def get(self, key: str) -> Optional[str]:
        pass

    @abstractmethod
    def set(self, key: str, value: str, ttl: Optional[int] = None) -> None:
        pass


class MemoryStorage(StorageBackend):
    """In-memory key-value store with thread safety."""

    def __init__(self):
        self._store: Dict[str, Tuple[str, Optional[float]]] = {}
        self._lock = threading.Lock()

    def get(self, key: str) -> Optional[str]:
        with self._lock:
            if key not in self._store:
                return None
            val, expiry = self._store[key]
            if expiry and time.time() > expiry:
                del self._store[key]
                return None
            return val

    def set(self, key: str, value: str, ttl: Optional[int] = None) -> None:
        with self._lock:
            expiry = (time.time() + ttl) if ttl else None
            self._store[key] = (value, expiry)


# ==========================================
# 3. Rate Limiter Strategy Interface
# ==========================================

class RateLimiterStrategy(ABC):
    """Abstract Strategy for Rate Limiting Algorithms."""

    @abstractmethod
    def is_allowed(self, client_id: str, rule: RateLimitRule) -> RateLimitResult:
        pass


# ==========================================
# 4. Concrete Strategy 1: Token Bucket Algorithm
# ==========================================

class TokenBucketStrategy(RateLimiterStrategy):
    """
    Refills tokens at a steady rate over time.
    Allows short bursts up to max_requests.
    """

    def __init__(self, storage: StorageBackend):
        self.storage = storage
        self._lock = threading.Lock()  # Ensures local thread safety

    def is_allowed(self, client_id: str, rule: RateLimitRule) -> RateLimitResult:
        key = f"tb:{client_id}"
        now = time.time()
        refill_rate = rule.max_requests / rule.window_seconds

        with self._lock:
            data = self.storage.get(key)
            if data:
                tokens, last_refill = map(float, data.split(":"))
            else:
                tokens = float(rule.max_requests)
                last_refill = now

            # 1. Calculate refilled tokens based on time passed
            elapsed = now - last_refill
            tokens = min(rule.max_requests, tokens + elapsed * refill_rate)
            last_refill = now

            # 2. Consume token if available
            if tokens >= 1.0:
                tokens -= 1.0
                allowed = True
                retry_after = 0.0
            else:
                allowed = False
                retry_after = (1.0 - tokens) / refill_rate

            # 3. Save state
            self.storage.set(key, f"{tokens}:{last_refill}", ttl=rule.window_seconds)

            return RateLimitResult(
                allowed=allowed,
                limit=rule.max_requests,
                remaining=int(tokens),
                retry_after=round(retry_after, 2)
            )


# ==========================================
# 5. Concrete Strategy 2: Sliding Window Log Algorithm
# ==========================================

class SlidingWindowLogStrategy(RateLimiterStrategy):
    """
    Keeps track of precise timestamps of previous requests.
    Eliminates boundary bursts completely.
    """

    def __init__(self):
        self._logs: Dict[str, List[float]] = {}
        self._lock = threading.Lock()

    def is_allowed(self, client_id: str, rule: RateLimitRule) -> RateLimitResult:
        key = f"swl:{client_id}"
        now = time.time()
        window_start = now - rule.window_seconds

        with self._lock:
            if key not in self._logs:
                self._logs[key] = []

            # 1. Remove timestamps outside the current window
            timestamps = [ts for ts in self._logs[key] if ts > window_start]
            self._logs[key] = timestamps

            # 2. Check quota
            if len(timestamps) < rule.max_requests:
                timestamps.append(now)
                allowed = True
                remaining = rule.max_requests - len(timestamps)
                retry_after = 0.0
            else:
                allowed = False
                remaining = 0
                # Wait time until the oldest timestamp slides out of the window
                oldest_ts = timestamps[0]
                retry_after = (oldest_ts + rule.window_seconds) - now

            return RateLimitResult(
                allowed=allowed,
                limit=rule.max_requests,
                remaining=remaining,
                retry_after=max(0.0, round(retry_after, 2))
            )


# ==========================================
# 6. Main RateLimiter Context Class
# ==========================================

class RateLimiter:
    """Facade / Context for clients to interact with."""

    def __init__(self, strategy: RateLimiterStrategy):
        self.strategy = strategy
        self._rules: Dict[str, RateLimitRule] = {}

    def add_rule(self, route_name: str, rule: RateLimitRule) -> None:
        self._rules[route_name] = rule

    def check(self, client_id: str, route_name: str) -> RateLimitResult:
        rule = self._rules.get(route_name)
        if not rule:
            # Default fallback rule if route rule is missing
            rule = RateLimitRule(max_requests=60, window_seconds=60)

        composite_key = f"{route_name}:{client_id}"
        return self.strategy.is_allowed(composite_key, rule)


if __name__ == "__main__":
    # Setup Storage and Strategy
    memory_storage = MemoryStorage()
    strategy = TokenBucketStrategy(storage=memory_storage)

    # Initialize Limiter
    limiter = RateLimiter(strategy=strategy)

    # Add rules: Allow 3 requests per 5 seconds on the "/login" route
    limiter.add_rule("/login", RateLimitRule(max_requests=3, window_seconds=5))

    user_id = "user_123"

    print("--- Simulating Requests ---")
    for i in range(1, 6):
        res = limiter.check(client_id=user_id, route_name="/login")
        if res.allowed:
            print(f"Req #{i}: ✅ Allowed (Remaining: {res.remaining})")
        else:
            print(f"Req #{i}: ❌ Denied (Retry after: {res.retry_after}s)")
        time.sleep(0.5)