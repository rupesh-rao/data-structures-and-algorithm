class Solution:
    def editDistanceHelper(self, i, j, s, t, dp):
        if i == len(s):
            return len(t) - j  # insert all remaining
        if j == len(t):
            return len(s) - i  # delete all remaining

        if dp[i][j] != -1:
            return dp[i][j]

        if s[i] == t[j]:
            dp[i][j] = self.editDistanceHelper(i + 1, j + 1, s, t, dp)
        else:
            insert = self.editDistanceHelper(i, j + 1, s, t, dp)
            delete = self.editDistanceHelper(i + 1, j, s, t, dp)
            replace = self.editDistanceHelper(i + 1, j + 1, s, t, dp)
            dp[i][j] = 1 + min(insert, min(delete, replace))

        return dp[i][j]

    def editDistance(self, start, target):
        m, n = len(start), len(target)
        dp = [[0 for _ in range(n + 1)] for _ in range(2)]

        # if start length is 0, then insert all character
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            dp[i % 2][0] = i
            for j in range(1, n + 1):
                if start[i - 1] == target[j - 1]:
                    dp[i % 2][j] = dp[(i - 1) % 2][j - 1]
                else:
                    dp[i % 2][j] = 1 + min(dp[i % 2][j - 1], min(dp[(i - 1) % 2][j], dp[(i - 1) % 2][j - 1]))
                    # dp[i][j-1] = insert
                    # dp[i-1][j] = delete
                    # dp[i-1][j-1] = replace
        return dp[m % 2][n]

