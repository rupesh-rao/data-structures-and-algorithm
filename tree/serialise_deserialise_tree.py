from __future__ import annotations
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# https://takeuforward.org/practice/dsa/serialize-and-de-serialize-bt
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        dq = deque()
        dq.append(root)
        res = []
        while dq:
            node = dq.popleft()
            if not node:
                res.append("#")
            else:
                res.append(str(node.val))
                dq.append(node.left)
                dq.append(node.right)

        return ",".join(res)

    def deserialize(self, val):
        """Decodes your encoded val to tree.

        :type val: str
        :rtype: TreeNode
        """
        if not val:
            return None
        vallist = deque(val.split(","))
        root = TreeNode(int(vallist.popleft()))
        dq = deque([root])
        while dq:
            node = dq.popleft()
            leftval = vallist.popleft()
            if leftval != "#":
                node.left = TreeNode(int(leftval))
                dq.append(node.left)
            rightval = vallist.popleft()
            if rightval != "#":
                node.right = TreeNode(int(rightval))
                dq.append(node.right)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))