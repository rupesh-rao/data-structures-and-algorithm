from bisect import bisect_left
# https://takeuforward.org/practice/dsa/depth-of-bst-given-insertion-order
class Solution:
    def maxDepthBST(self, order):
        n = len(order)
        if n == 0:
            return 0
        N = int(1e5 + 7)
        # store depth of each node
        depth = [0] * (int(1e5 + 7))
        # store the node seen till now in sorted order
        seen = []
        max_depth = 0
        for i in range(n):
            # index of node just bigger
            r = bisect_left(seen, order[i])
            # index of node just smaller
            l = r - 1
            rightDepth = depth[seen[r]] if 0 <= r < len(seen) else 0
            leftDepth = depth[seen[l]] if 0 <= l < len(seen) else 0
            # current node depth if 1 + max of left and right node depth
            depth[order[i]] = 1 + max(leftDepth, rightDepth)
            max_depth = max(max_depth, depth[order[i]])
            # insert current node in sorted order
            seen.insert(r, order[i])
        return max_depth