# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

# https://takeuforward.org/practice/dsa/range-sum-in-bst
class Solution:
    def rangeSumBST(self, root, low, high):
        if not root:
            return 0

        s = 0

        if low <= root.data <= high:
            s += root.data

        if root.data > low:
            s += self.rangeSumBST(root.left, low, high)

        if root.data < high:
            s += self.rangeSumBST(root.right, low, high)

        return s


