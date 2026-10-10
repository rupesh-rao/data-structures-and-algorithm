# https://leetcode.com/problems/minimum-sum-of-squared-difference/description
class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        n = len(nums1)
        ans = 0
        hashmap = [0] * int(1e5 + 7)
        max_diff = 0

        # count of diff
        for i in range(n):
            diff = nums1[i] - nums2[i]
            if diff < 0:
                diff = -diff
            max_diff = max(max_diff, diff)
            hashmap[diff] += 1

        k = k1 + k2
        # iterate over all the diff and decrease it by 1 till K is left
        for i in range(max_diff + 1, -1, -1):
            if hashmap[i] > 0:
                minus = min(hashmap[i], k)
                hashmap[i] -= minus
                hashmap[i - 1] += minus
                ans += (i * i) * (hashmap[i])
                k -= minus

        return ans

