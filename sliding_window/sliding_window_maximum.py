from collections import deque
# https://leetcode.com/problems/sliding-window-maximum/description/
# https://takeuforward.org/practice/dsa/sliding-window-maximum
class Solution:
    def maxSlidingWindow(self, arr, k):
        n = len(arr)
        dq = deque()
        ans = []

        for i in range(0, n):
            # remove index out of range from front
            while len(dq) > 0 and dq[0] <= i - k:
                dq.popleft()
            # remove index which are smaller element from back
            while len(dq) > 0 and arr[dq[-1]] <= arr[i]:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                ans.append(arr[dq[0]])
        return ans
