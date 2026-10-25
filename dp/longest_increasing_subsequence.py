class Solution:
    def LIS(self, nums):
        def lower_bound(a, target):
            low, high = 0, len(a) - 1
            while low <= high:
                mid = (low + high) // 2
                if a[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return low

        n = len(nums)
        if n <= 1:
            return n
        # store numbers in increasing order
        incr = []
        for i in range(n):
            ind = lower_bound(incr, nums[i])
            if len(incr) == ind:
                incr.append(nums[i])
            else:
                incr[ind] = nums[i]
        return len(incr)


