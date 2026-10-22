# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right
# https://takeuforward.org/practice/dsa/check-if-two-trees-are-identical-or-not
class Solution:
    def recursive(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False

        if p.data != q.data:
            return False

        return self.recursive(p.left, q.left) and self.recursive(p.right, q.right)

    def isSameTree(self, p, q):
        return self.recursive(p, q)