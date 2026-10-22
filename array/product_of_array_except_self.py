# https://leetcode.com/problems/product-of-array-except-self/
class Solution:
    """
    Can be done using prefix and suffix prod array.
    Below is implementation of creating the product directly while iterating from both sides
    """
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [1] * n
        cur = 1
        for i in range(n):
            ans[i] *= cur
            cur *= nums[i]
        cur = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= cur
            cur *= nums[i]
        return ans
