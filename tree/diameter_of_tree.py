# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.diameter = 0

    def travel(self, root):
        if not root:
            return 0
        left = self.travel(root.left)
        right = self.travel(root.right)

        self.diameter = max(self.diameter, 1 + left + right)

        return 1 + max(left, right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.diameter = 0
        self.travel(root)
        return self.diameter - 1


