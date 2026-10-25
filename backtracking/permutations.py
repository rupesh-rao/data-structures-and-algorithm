class Solution:
    # the idea is swapping
    def permute(self, nums: list[int]) -> list[list[int]]:
        def builder(index):
            if index == n:
                ans.append(nums[::])
                return
            # swap with current index as well so that it is not skipped in the final answer
            for swapIndex in range(index, n):
                nums[index], nums[swapIndex] = nums[swapIndex], nums[index]
                builder(index + 1)
                nums[index], nums[swapIndex] = nums[swapIndex], nums[index]

        n, ans = len(nums), []
        builder(0)
        return ans
