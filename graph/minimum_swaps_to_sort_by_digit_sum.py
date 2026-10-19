"""
Minimum swaps to sort an array is equal to the
summation of all (length of the permutation cycles - 1) in the array.

∑(ki−1)=(∑ki)−cycles=n−cycles
cycles = number of permutation cycle
ki = length of ith cycle

Permutation cycle is the directed cycle of the array element, where directed egde is
current_pos, target_pos

"""
from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)

        def summer(y):
            foo = 0
            while y > 0:
                foo += y % 10
                y //= 10
            return foo

        indices = list(range(n))
        # sort the current index on basis of sum of digit
        indices.sort(key=lambda i: (summer(nums[i]), nums[i]))

        edges = [0] * n
        # create edge between current to target index
        for i, j in enumerate(indices):
            edges[j] = i

        visited = [False] * n
        cycles = 0
        for i in range(n):
            if not visited[i]:
                # count all the cycle. Note: current_pos==target_pos is also a cycle
                cycles += 1
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = edges[j]

        return n - cycles













