# https://takeuforward.org/practice/dsa/rod-cutting-problem
class Solution:
    """
    f(4) = max(f(1)*4, f(2)*2, f(3)+f(1))
    """
    def RodCutting(self, a, n):
        # dp[i] , max length of cutting rod of length 'i'
        dp = [0 for _ in range(n + 1)]

        for i in range(1, n + 1):  # length of rod 1 to n
            dp[i] = float("-inf")
            for j in range(1, i + 1):  # cut in pieces of 1 to i
                dp[i] = max(dp[i - j] + a[j - 1], dp[
                    i])  # when cutting it by length j, add its cost which is a[j-1] because the array is following 1-based indexing

        return dp[n]



