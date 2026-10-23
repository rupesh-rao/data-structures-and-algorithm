class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        n = len(intervals)
        if n == 0:
            return []
        intervals.sort()
        res = [intervals[0]]
        # for storing the last intervals index
        i = 0
        for j in range(1, n):
            # if current interval overlaps with last interval
            if res[i][1] >= intervals[j][0]:
                res[i][0] = min(res[i][0], intervals[j][0])
                res[i][1] = max(res[i][1], intervals[j][1])
            # otherwise
            else:
                res.append(intervals[j])
                i+=1
        return res