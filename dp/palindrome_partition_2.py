"""
Given a string s, a partitioning of the string is a palindrome partitioning if every sub-string of the partition
is a palindrome. Find the fewest cuts needed for palindrome partitioning of the given string.
"""

# https://www.geeksforgeeks.org/problems/palindromic-patitioning4845/1
# https://leetcode.com/problems/palindrome-partitioning-i
# https://takeuforward.org/practice/dsa/palindrome-partitioning-ii-
class Solution:
    def minCut(self, s):
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        # string of length is always palindrome
        for i in range(n):
            dp[i][i] = True

        # calculate isPalindrome for all index pairs
        for l in range(2, n + 1):
            for i in range(0, n - l + 1):
                j = i + l - 1
                if l == 2:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (s[i] == s[j] and dp[i + 1][j - 1])

        cuts = [n + 1] * n
        for i in range(n):
            # entire string from [0,i] is palindrom so no cuts
            if dp[0][i]:
                cuts[i] = 0
            else:
                for j in range(1, i + 1):
                    # check palindrome from [1,i]
                    # since cut [j,i] is palindrome, take cut from j-1
                    if dp[j][i] and cuts[j - 1] + 1 < cuts[i]:
                        cuts[i] = cuts[j - 1] + 1
        return cuts[n - 1]


