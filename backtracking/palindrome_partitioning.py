# https://takeuforward.org/practice/dsa/palindrome-partitioning
class Solution:
    def partition(self, s: str):
        n = len(s)

        def isPalindrome(st, start, end):
            while start <= end:
                if st[start] != st[end]:
                    return False
                start += 1
                end -= 1
            return True

        def builder(index):
            if index == n:
                ans.append(path[::])
                return
            for i in range(index, n):
                if isPalindrome(s, index, i):
                    path.append(s[index:i + 1])
                    builder(i + 1)
                    path.pop()

        ans = []
        path = []
        builder(0)
        return ans