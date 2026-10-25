class Solution:
    # memoization
    def knapsack01_memoization(self, wt, val, n, W):
        dp = [[-1] * (W + 1) for _ in range(n)]

        def travel(index, cur_weight):
            if cur_weight == 0 or index < 0:
                return 0
            if dp[index][cur_weight] != -1:
                return dp[index][cur_weight]

            with_item = float("-inf")
            if cur_weight >= wt[index]:
                with_item = val[index] + travel(index - 1, cur_weight - wt[index])
            without_item = travel(index - 1, cur_weight)

            dp[index][cur_weight] = max(without_item, with_item)
            return dp[index][cur_weight]

        return travel(n - 1, W)

    def knapsack01_tabular(self, wt, val, n, W):

        dp = [[0] * (W + 1) for _ in range(n)]
        # Handle base case for index 0
        # Since it does not have a previous row to get the answer
        # we have to specifically fill its column
        for i in range(wt[0], W + 1):
            dp[0][i] = val[0]

        for i in range(1, n):
            for w in range(W + 1):
                if w - wt[i] >= 0:
                    dp[i][w] = max(val[i] + dp[i - 1][w - wt[i]], dp[i - 1][w])
                else:
                    dp[i][w] = dp[i - 1][w]
        return dp[n - 1][W]

    def knapsack01_tabular_space_optimised(self, wt, val, n, W):
        dp = [[0] * (W + 1) for _ in range(2)]
        # Handle base case for index 0
        # Since it does not have a previous row to get the answer
        # we have to specifically fill its column
        for i in range(wt[0], W + 1):
            dp[0][i] = val[0]

        for i in range(1, n):
            for w in range(W + 1):
                if w - wt[i] >= 0:
                    dp[i % 2][w] = max(val[i] + dp[(i - 1) % 2][w - wt[i]], dp[(i - 1) % 2][w])
                else:
                    dp[i % 2][w] = dp[(i - 1) % 2][w]
        return dp[(n - 1) % 2][W]

