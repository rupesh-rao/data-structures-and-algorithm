from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        from collections import deque
        dq = deque()
        dq.append(root)

        while dq:
            cur = []
            size = len(dq)
            for _ in range(size):
                top = dq.popleft()
                cur.append(top.val)
                if top.left:
                    dq.append(top.left)
                if top.right:
                    dq.append(top.right)
            ans.append(cur)
        return ans