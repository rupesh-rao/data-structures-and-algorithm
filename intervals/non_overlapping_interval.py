# https://takeuforward.org/practice/dsa/non-overlapping-intervals
#
class Solution:
    def MaximumNonOverlappingIntervals(self, intervals):
        n = len(intervals)
        if n == 0:
            return 0

        intervals.sort(key=lambda x: x[1])
        count, j = 0, 0
        for i in range(1, n):
            # overlap
            if intervals[j][1] > intervals[i][0]:
                count += 1
            else:
                j = i
        return count

