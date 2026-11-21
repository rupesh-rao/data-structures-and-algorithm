
class Solution:
    def longestSubarray(self, nums, k):
        # to store the sum
        sum_map = {}
        # set index = -1 for sum=0
        sum_map[0] = -1
        prefix_sum = 0
        ans = 0

        for i, num in enumerate(nums):
            prefix_sum += num
            # check if prefix sum is already made, 
            # remove the prefix, to make a valid subarray of sum k 
            if prefix_sum-k in sum_map:
                ans = max(ans, i-sum_map[prefix_sum-k])
            # store the earliest prefix sum index
            if prefix_sum not in sum_map:
                sum_map[prefix_sum] = i

        return ans        