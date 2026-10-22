# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    # idea is to return the node which is equal to any of the target, otherwise return None
    # if both left and right child returns not none, that means that node is the LCA
    # if either one of them return not none, then that one is the LCA
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None
        if root and (root.data == p.data or root.data == q.data):
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        if left:
            return left
        return right