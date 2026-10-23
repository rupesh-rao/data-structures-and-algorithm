class Solution:
    def insertNewInterval(self, intervals, newInterval):
        res = []
        i, n = 0, len(intervals)
        # add all interval not overlapping
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # add overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)

        # add all interval not overlapping
        while i < n:
            res.append(intervals[i])
            i += 1

        return res






