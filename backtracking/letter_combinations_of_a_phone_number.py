class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        n = len(digits)
        ans = []
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def builder(index, cur):
            if index >= n:
                ans.append(cur)
                return
            for letter in letters[digits[index]]:
                builder(index + 1, cur + letter)

        builder(0, "")
        return ans

