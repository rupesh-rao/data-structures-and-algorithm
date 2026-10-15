class Solution:
    def findMedian(self, matrix):
        def upper_bound(nums, target):
            """
            Function for finding upper bound
            """
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] <= target:
                    low = mid + 1
                else:
                    high = mid - 1
            return low

        def check(x):
            """
            Function for finding count of elements less than 'x'
            """
            c = 0
            for i in range(n):
                c += upper_bound(matrix[i], x)
            return c

        n = len(matrix)
        m = len(matrix[0])
        median = (n * m) // 2
        low, high = float("inf"), float("-inf")
        for i in range(n):
            for j in range(m):
                low = min(low, matrix[i][j])
                high = max(high, matrix[i][j])
        # search over minimum and maximum element in the matrix
        while low <= high:
            mid = (low + high) // 2
            cnt = check(mid)
            if cnt <= median:
                low = mid + 1
            else:
                high = mid - 1
        return low
