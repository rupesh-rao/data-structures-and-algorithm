import heapq

class Solution:
    # Idea: if two events are available on same day, it is optimal to choose the event that is ending sooner
    # At any given day, choose the event with lowest endDay (use min-heap)
    def maxEvents(self, events: list[list[int]]) -> int:
        # sort the events in the increasing order of startDay
        events.sort()
        # min-heap to store end day of event
        pq = []
        j = 0
        ans = 0
        n = len(events)
        # loop for the days
        for day in range(1, 100001):
            # remove the event which are ended
            while pq and pq[0] < day:
                heapq.heappop(pq)

            # insert in the min-heap while startDay is less than equal to current day
            while j < n and events[j][0] == day:
                heapq.heappush(pq, events[j][1])
                j += 1
            # visit the event at top
            if pq:
                heapq.heappop(pq)
                ans += 1
        return ans



