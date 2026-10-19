# https://takeuforward.org/practice/dsa/non-overlapping-intervals
class Solution:
    def MaximumNonOverlappingIntervals(self, a):
        a.sort(key = lambda x: x[1])
        count = 0
        n = len(a)
        last = 0
        for i in range(1, n):
            l = a[last]
            r = a[i]
            if r[0] < l[1]:
                count += 1
            else:
                last = i
        return count