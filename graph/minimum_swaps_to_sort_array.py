# https://www.geeksforgeeks.org/problems/minimum-swaps/1

"""
Minimum swaps to sort an array is equal to the
summation of all (length of the permutation cycles - 1) in the array.

∑(ki−1)=(∑ki)−cycles=n−cycles
cycles = number of permutation cycle
ki = length of ith cycle

Permutation cycle is the directed cycle of the array element, where directed egde is
current_pos, target_pos

"""
class Solution:
    def minSwaps(self, arr):
        n = len(arr)
        indices = list(enumerate(arr)) # (i, arr[i])
        indices.sort(key=lambda x: x[1]) # sort by arr[i]

        vis = [False] * n
        cycle = 0
        for i in range(n):
            # for each index
            if not vis[i]:
                cycle += 1
                # perform dfs to mark all the nodes in the cycle as visited
                j = i
                while not vis[j]:
                    vis[j] = True
                    j = indices[j][0]
        # check the notes on why we return this
        return n - cycle