class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []

        def builder(open_bracket, close_bracket, parenthesis):
            if open_bracket == n and close_bracket == n:
                ans.append(parenthesis)
                return

            if open_bracket < n:
                builder(open_bracket + 1, close_bracket, parenthesis + "(")
            if close_bracket < open_bracket:
                builder(open_bracket, close_bracket + 1, parenthesis + ")")

        builder(0, 0, "")
        return ans
