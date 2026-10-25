# https://leetcode.com/problems/minimum-path-sum
class Solution:
    def minPathSum(self, a: list[list[int]]) -> int:
        m, n = len(a), len(a[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    dp[i][j] = a[i][j]
                elif i==0:
                    dp[i][j] = a[i][j] + dp[i][j-1]
                elif j == 0:
                    dp[i][j] = a[i][j] + dp[i-1][j]
                else:
                    dp[i][j] = a[i][j] + min(dp[i-1][j], dp[i][j-1])
        return dp[m-1][n-1]


    def minPathSum_space_optimised(self, a: list[list[int]]) -> int:
        m, n = len(a), len(a[0])
        dp = [[0 for _ in range(n)] for _ in range(2)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i % 2][j] = a[i][j]
                elif i == 0:
                    dp[i % 2][j] = a[i][j] + dp[i % 2][j - 1]
                elif j == 0:
                    dp[i % 2][j] = a[i][j] + dp[(i - 1) % 2][j]
                else:
                    dp[i % 2][j] = a[i][j] + min(dp[(i - 1) % 2][j], dp[i % 2][j - 1])
        return dp[(m - 1) % 2][n - 1]