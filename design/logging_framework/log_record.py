from dataclasses import dataclass
from datetime import datetime
from log_level import LogLevel

@dataclass(frozen=True)
class LogRecord:
    timestamp: datetime
    message: str
    log_level: LogLevel
    thread_name: str


