# Time Worst: O(N!)
# Time Avg: O(N!/(N-K)!) where k is the number of duplicate numbers
class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n, ans = len(nums), []

        def builder(index):
            if index == n:
                ans.append(nums[::])
                return
            for i in range(index, n):
                # check if current number is equal to index instead of the previous number
                if i > index and nums[i] == nums[index]:
                    continue
                nums[i], nums[index] = nums[index], nums[i]
                builder(index + 1)
            # restore the nums array back to previous state
            for i in range(n - 1, index, -1):
                nums[i], nums[index] = nums[index], nums[i]

        builder(0)
        return ans

