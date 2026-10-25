# https://www.geeksforgeeks.org/problems/coin-change2448/1
class Solution:
    def count_memoization(self, coins: list[int], S: int) -> int:
        def func(i, s):
            if s == 0:
                return 1
            if i < 0:
                return 0

            if dp[i][s] != -1:
                return dp[i][s]

            if (coins[i] <= s):
                dp[i][s] = func(i, s-coins[i]) + func(i-1, s)
            else:
                dp[i][s] = func(i-1, s)
            return dp[i][s]
        N = len(coins)
        dp = [[-1]*(S+1) for _ in range(N)]
        return func(N-1, S)


    def count_tabular(self, coins: list[int], S: int):
        N = len(coins)
        dp = [[0] * (S + 1) for _ in range(N)]
        # initialise for S=0
        for i in range(N):
            dp[i][0] = 1
        # initialise for i = 0, first row
        for i in range(coins[0], S + 1):
            dp[0][i] = dp[0][i - coins[0]]

        for i in range(1, N):
            for j in range(S + 1):
                if coins[i] <= j:
                    dp[i][j] = dp[i][j - coins[i]] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[N - 1][S]


    def count_tabular_space_optimised(self, coins: list[int], S: int):
        N = len(coins)
        dp = [[0] * (S + 1) for _ in range(2)]
        # initialise for S=0
        for i in range(N):
            dp[i%2][0] = 1
        # initialise for i = 0, first row
        for i in range(coins[0], S + 1):
            dp[0][i] = dp[0][i - coins[0]]

        for i in range(1, N):
            for j in range(S + 1):
                if coins[i] <= j:
                    dp[i%2][j] = dp[i%2][j - coins[i]] + dp[(i - 1)%2][j]
                else:
                    dp[i%2][j] = dp[(i - 1)%2][j]

        return dp[(N - 1)%2][S]