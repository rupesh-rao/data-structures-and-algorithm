class Solution:
    def maxProduct(self, nums):
        min_prod, max_prod = nums[0], nums[0]
        res = nums[0]
        n = len(nums)
        for i in range(1, n):
            if nums[i] < 0:
                min_prod, max_prod = max_prod, min_prod
            min_prod = min(min_prod * nums[i], nums[i])
            max_prod = max(max_prod * nums[i], nums[i])
            res = max(res, max_prod)

        return res
