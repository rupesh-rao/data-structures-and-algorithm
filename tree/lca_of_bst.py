# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right
#
class Solution:
    # idea is that we can skip checking one half of the tree based on comparison
    def lca(self, root, p, q):
        # if root is greater than both p and q, it means LCA is present in left subtree
        if root.data > p and root.data > q:
            return self.lca(root.left, p, q)
        # if root is lesser than both p and q, it means LCA is present in right subtree
        if root.data < p and root.data < q:
            return self.lca(root.right, p, q)
        # if we cannot skip any half then, current node is LCA as p and q lie in opposite halves
        return root

