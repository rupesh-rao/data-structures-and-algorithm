# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

# https://takeuforward.org/practice/dsa/check-if-a-tree-is-a-bst-or-not
# https://leetcode.com/problems/validate-binary-search-tree/
class Solution:
    def checkBST(self, root, min_element, max_element):
        if not root:
            return True

        if root.data <= min_element or root.data >= max_element:
            return False

        return self.checkBST(root.left, min_element, root.data) and self.checkBST(root.right, root.data, max_element)

    def isBST(self, root):
        return self.checkBST(root, float("-inf"), float("inf"))
