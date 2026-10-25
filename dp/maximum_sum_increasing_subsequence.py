class Solution:
    def maxSumIS(self, arr):
        n = len(arr)
        # to store the max sum increasing sequence till i
        dp = [0] * n
        for i in range(n):
            dp[i] = arr[i]
            for j in range(0, i):
                if arr[j] < arr[i]:
                    # if arr[j] is less than arr[i], check if max sum increasing sequence till j + arr[i] is greater
                    dp[i] = max(dp[i], dp[j]+arr[i])

        return max(dp)