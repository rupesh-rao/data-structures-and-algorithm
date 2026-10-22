# Definition for a binary tree node.
from __future__ import annotations


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# https://takeuforward.org/practice/dsa/maximum-path-sum-
# https://leetcode.com/problems/binary-tree-maximum-path-sum/
class Solution:
    def helper(self, root, max_sum):
        if not root:
            return 0

        left = max(self.helper(root.left, max_sum), 0)
        right = max(self.helper(root.right, max_sum), 0)

        max_sum[0] = max(max_sum[0], root.val + left + right)

        return root.val + max(left, right)

    def maxPathSum(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        max_sum = [float("-inf")]
        self.helper(root, max_sum)
        return max_sum[0]