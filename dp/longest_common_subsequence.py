class Solution:
    def lcaHelper(self, i, j, s1, s2, dp):
        if i < 0 or j < 0:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]

        if s1[i] == s2[j]:
            dp[i][j] = 1 + self.lcaHelper(i - 1, j - 1, s1, s2, dp)
        else:
            dp[i][j] = max(self.lcaHelper(i - 1, j, s1, s2, dp), self.lcaHelper(i, j - 1, s1, s2, dp))
        return dp[i][j]

    def lcs_memoization(self, str1, str2):
        l1, l2 = len(str1), len(str2)
        dp = [[-1 for _ in range(l2 + 1)] for _ in range(l1 + 1)]
        return self.lcaHelper(l1 - 1, l2 - 1, str1, str2, dp)


    def lcs_tabular(self, str1, str2):
        l1, l2 = len(str1), len(str2)
        dp = [[0 for _ in range(l2+1)] for _ in range(l1+1)]
        for i in range(1,l1+1):
            for j in range(1, l2+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])

        return dp[l1][l2]

    def lcs_space_optimised(self, str1, str2):
        l1, l2 = len(str1), len(str2)
        dp = [[0 for _ in range(l2 + 1)] for _ in range(2)]
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i % 2][j] = 1 + dp[(i - 1) % 2][j - 1]
                else:
                    dp[i % 2][j] = max(dp[i % 2][j - 1], dp[(i - 1) % 2][j])

        return dp[l1 % 2][l2]

