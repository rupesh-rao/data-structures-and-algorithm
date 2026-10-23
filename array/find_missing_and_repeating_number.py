# https://takeuforward.org/practice/dsa/find-the-repeating-and-missing-number
class Solution:
    # Function to find repeating and missing numbers
    def findMissingRepeatingNumbers(self, nums):
        n = len(nums)
        Sn = (n * (n + 1)) // 2
        Sn2 = (n * (n + 1) * (2 * n + 1)) // 6

        Sc = 0
        Sc2 = 0
        for i in range(n):
            Sc += nums[i]
            Sc2 += nums[i] * nums[i]

        b_minus_a = Sn - Sc
        b_plus_a = (Sn2 - Sc2) // b_minus_a

        b = (b_minus_a + b_plus_a) // 2
        a = b_plus_a - b

        return [a, b]

