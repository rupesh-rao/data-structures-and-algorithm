# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def recursive(self, root):
        if not root:
            return 0
        return 1 + max(self.recursive(root.left), self.recursive(root.right))

    # bfs
    def iterative(self, root):
        if not root:
            return 0
        from collections import deque
        dq = deque()
        dq.append(root)
        level = 0
        while dq:
            size = len(dq)
            for _ in range(size):
                top = dq.popleft()
                if top.left:
                    dq.append(top.left)
                if top.right:
                    dq.append(top.right)
            level += 1
        return level

    def maxDepth(self, root):
        # return self.recursive(root)
        return self.iterative(root)
