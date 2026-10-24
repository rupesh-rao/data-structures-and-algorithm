# https://takeuforward.org/practice/dsa/clone-graph
# https://leetcode.com/problems/clone-graph
class Node:
    # Constructor to initialize node value and neighbors
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def helper(self, node, vis):
        if node.val in vis:
            return vis[node.val]

        newNode = Node(node.val)
        vis[node.val] = newNode
        for child in node.neighbors:
            newNode.neighbors.append(self.helper(child, vis))
        return newNode

    def cloneGraph(self, node):
        if not node:
            return node
        vis = {}
        return self.helper(node, vis)