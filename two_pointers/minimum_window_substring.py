
# https://takeuforward.org/practice/dsa/minimum-window-substring
# https://leetcode.com/problems/minimum-window-substring
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def check():
            """
            Return true is all characters are present in a substring
            """
            for k, v in hashmap.items():
                if v > 0:
                    return False
            return True

        hashmap = {}
        for i in t:
            hashmap[i] = hashmap.get(i, 0) + 1

        left, right, n = 0, 0, len(s)
        min_len = n + 1
        start = -1
        while right < n:
            if s[right] in hashmap:
                hashmap[s[right]] -= 1
            while left <= right and check():
                if min_len > (right - left + 1):
                    min_len = right - left + 1
                    start = left
                if s[left] in hashmap:
                    hashmap[s[left]] += 1
                left += 1
            right += 1

        return s[start:(start + min_len)] if min_len != (n + 1) else ""


