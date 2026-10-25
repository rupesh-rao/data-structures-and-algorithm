# https://leetcode.com/problems/combinations
#
class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []
        cur = []

        def builder(num, available):
            if available == 0:
                result.append(cur[::])
                return
            if num > n or available < 0:
                return
            cur.append(num)
            builder(num + 1, available - 1)
            cur.pop()
            builder(num + 1, available)

        builder(1, k)
        return result

