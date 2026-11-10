class Solution:
    def climbStairs(self, n: int, costs: list[int]) -> int:
        dp = [float("inf")] * (n+3)
        dp[2] = 0

        for i in range(n):
            j = i+3
            step1 = 1 + dp[j-1]
            step2 = 4 + dp[j-2]
            step3 = 9 + dp[j-3]
            dp[j] = costs[i] + min(step1, min(step2, step3))

        return dp[-1]


    def climbStairsSpaceOptimised(self, n: int, costs: list[int]) -> int:
        a, b, c = 0, 0, 0 # dp[i-3], dp[i-2], dp[i-1]

        for i in range(n):
            a, b, c = b, c, costs[i] + min(a+9, b+4, c+1)

        return c