# https://takeuforward.org/practice/dsa/minimum-coins
class Solution:
    def MinimumCoins(self, coins, amount):
        dp = [float("inf")] * (amount + 1)  # store min coin for making ith amount
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin and dp[i - coin] != float("inf"):
                    dp[i] = min(dp[i], 1 + dp[i - coin])

        return dp[amount] if dp[amount] != float("inf") else -1
