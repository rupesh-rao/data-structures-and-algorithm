# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    # intuition is that we can find the root node from pre-order (first node)
    # the left side children can be found on the left of the index of root in in-order,
    # similarly, right children can be found on the right side of the index of root in in-order

    def buildTree(self, preorder, inorder):
        hashmap = {}
        # store the index of nodes in the inorder
        for i, v in enumerate(inorder):
            hashmap[v] = i
        # helper function to generate Tree
        def helper(preIndex, inOrderStart, inOrderEnd):
            # return None if index is out of bound
            if inOrderStart > inOrderEnd:
                return None
            # create node from the first node in pre-order
            node = TreeNode(preorder[preIndex])
            # return node if only one node
            if inOrderStart == inOrderEnd:
                return node
            # find the index of the root node in inorder
            index = hashmap[preorder[preIndex]]
            # find the index on which the next preIndex will move to
            inLeft = index - inOrderStart
            node.left = helper(preIndex + 1, inOrderStart, index - 1)
            node.right = helper(preIndex + inLeft + 1, index + 1, inOrderEnd)

            return node

        return helper(0, 0, len(inorder) - 1)


