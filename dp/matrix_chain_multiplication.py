class Solution:
    # NOTE: If length is n, there are n-1 matrices
    # nums[i-1][i] is a matrix
    # M1 = nums[i-1] * nums[i], M2 = nums[i] * nums[i+1], M1*M2 = nums[i-1] * nums[i] * nums[i+1]

    def matrixMultiplication_recursive(self, nums):
        def recursive(i, j):
            if i == j:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            dp[i][j] = float("inf")
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], recursive(i, k) + recursive(k + 1, j) + nums[i - 1] * nums[k] * nums[j])
            return dp[i][j]

        n = len(nums)
        dp = [[-1] * n for _ in range(n)]
        return recursive(1, n - 1)

    def matrixMultiplication_tabular(self, nums):
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for l in range(2, n + 1):
            for i in range(0, n - l + 1):
                j = i + l - 1
                dp[i][j] = float("inf")
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + nums[i - 1] * nums[k] * nums[j])
        return dp[1][n - 1]
