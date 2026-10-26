# https://leetcode.com/problems/best-time-to-buy-and-sell-stock
# https://takeuforward.org/practice/dsa/best-time-to-buy-and-sell-stock
class Solution:
    """
    Maintain the lowest price from left and try to maximise the profit
    """
    def stockBuySell(self, arr, n):
        n = len(arr)
        if n <= 1:
            return 0
        max_profit, lowest_price = 0, arr[0]

        for i in range(1, n):
            max_profit = max(max_profit, arr[i] - lowest_price)
            lowest_price = min(lowest_price, arr[i])

        return max_profit
