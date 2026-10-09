# Definition for an n-ary tree node.
class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.children = []

from collections import deque

# https://takeuforward.org/practice/dsa/clone-n-ary-tree
class Solution:
    def cloneTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        # create a dummy root
        newRoot = TreeNode(-1)

        # declare a queue for FIFO
        st = deque([])
        st.append((root, newRoot))

        while len(st) > 0:
            # take element from front
            originalNode, cloneParent = st.popleft()
            # create clone of originalNode
            cloneNode = TreeNode(originalNode.val)
            # add cloneNode to cloneParent
            cloneParent.children.append(cloneNode)

            for originalChildNode in originalNode.children:
                # add originalChildNode with cloneNode as parent
                st.append((originalChildNode, cloneNode))

        # return the new root
        return newRoot.children[0]




