# https://takeuforward.org/practice/dsa/largest-rectangle-in-a-histogram
# https://leetcode.com/problems/largest-rectangle-in-histogram/description
class Solution:
    def largestRectangleArea(self, heights):
        """
        Store height in increasing order in stack
        When a small element is encountered start calculating area for each pop
        (reason: it will decrease height for future)
        """
        st = []
        max_area = 0
        n = len(heights)
        for i in range(n):
            # remove element when smaller element arrives
            while st and heights[st[-1]] > heights[i]:
                j = st.pop()
                h = heights[j]
                # window is [st[-1]+1, i)
                w = i if not st else (i - st[-1] - 1)
                max_area = max(max_area, h * w)
            st.append(i)

        while st:
            j = st.pop()
            h = heights[j]
            w = n if not st else (n - st[-1] - 1)
            max_area = max(max_area, h * w)

        return max_area


