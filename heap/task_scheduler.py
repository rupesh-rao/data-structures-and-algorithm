# https://takeuforward.org/practice/dsa/task-scheduler
# https://leetcode.com/problems/task-scheduler/
import heapq
class Solution:
    def leastInterval(self, tasks, n):
        # Build frequency map
        freq = [0] * 26
        for ch in tasks:
            freq[ord(ch) - ord('A')] += 1

        # Max heap to store frequencies
        pq = [-f for f in freq if f > 0]
        heapq.heapify(pq)

        time = 0
        # Process tasks until the heap is empty
        while pq:
            cycle = n + 1
            store = []
            task_count = 0
            # Execute tasks in each cycle
            while cycle > 0 and pq:
                current_freq = -heapq.heappop(pq)
                if current_freq > 1:
                    store.append(-(current_freq - 1))
                task_count += 1
                cycle -= 1
            # Restore updated frequencies to the heap
            for x in store:
                heapq.heappush(pq, x)
            # Add time for the completed cycle
            # Note: elements are again added to heap before doing this check
            time += task_count if not pq else n + 1

        return time