# https://leetcode.com/problems/trapping-rain-water/description/
# https://takeuforward.org/practice/dsa/trapping-rainwater

class Solution:
    def trap(self, height):
        """
        Formula: Water stored at index ith = min(leftMax, rightMax) - a[i]
        If we find the max element then we fix one end of the boundary
        """
        n = len(height)
        ans = 0
        # find max element
        max_element = max(height)
        max_element_index = height.index(max_element)
        i = 0
        curr_max = float("-inf")
        # on the left of max element
        while i < max_element_index:
            curr_max = max(curr_max, height[i])
            ans += min(curr_max, max_element) - height[i]
            i += 1
        i = n - 1
        curr_max = float("-inf")
        # on the right of max element
        while i > max_element_index:
            curr_max = max(curr_max, height[i])
            ans += min(curr_max, max_element) - height[i]
            i -= 1
        return ans




