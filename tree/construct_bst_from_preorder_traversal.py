# Definition for a binary tree node.
from __future__ import annotations


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
class Solution:
    def bstFromPreorder(self, preorder: list[int]) -> TreeNode | None:
        """
        First element always root,
        Find index greater than root, divide left and right tree on that index
        Time Complexity: O(NlogN) average, O(N*N) worst
        """
        def bst(start, end):
            if start > end:
                return
            root = TreeNode(preorder[start])
            ind = start + 1
            while ind <= end and preorder[ind] < preorder[start]:
                ind += 1
            root.left = bst(start + 1, ind - 1)
            root.right = bst(ind, end)

            return root

        if len(preorder) == 0:
            return None

        return bst(0, len(preorder) - 1)