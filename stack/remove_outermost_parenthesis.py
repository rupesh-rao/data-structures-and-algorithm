# https://leetcode.com/problems/remove-outermost-parentheses/description/
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        cnt = 0
        ans = ""
        for i in s:
            cnt += 1 if i == '(' else -1
            if (i == '(' and cnt == 1) or (i == ')' and cnt == 0):
                continue
            ans += i
        return ans
