"""
A vertex of a graph is called a Articulation point when the component
is divided into 2 or more components if that particular vertex is removed.
Removing a vertex means to also remove all the edges that share the vertex.
"""


class Solution:
    def __init__(self):
        # To store the current time during traversal
        self.timer = 1

    def articulationPoints(self, V, adj):
        def dfs(node, parent):
            vis[node] = True
            tin[node] = self.timer
            low[node] = self.timer
            self.timer += 1
            child = 0
            for adjNode in adj[node]:
                if adjNode == parent:
                    continue
                if not vis[adjNode]:
                    child += 1
                    dfs(adjNode, node)
                    # update the lowest time of insertion of current node
                    # compare with adjacent node's low array value
                    low[node] = min(low[node], low[adjNode])

                    # if lowest insertion time of adjNode is greater than time of the insertion of node
                    # it means there is no edge in adjNode to an ancestor of current node
                    if low[adjNode] >= tin[node] and parent != -1:
                        ap[node] = True
                else:
                    # update the lowest time of insertion of current node
                    # compare with adjNode's tin array value because it is visited before current node
                    low[node] = min(low[node], tin[adjNode])

            # if the parent is -1 and more children than 1
            # it is an AP
            if parent == -1 and child > 1:
                ap[node] = True

        self.timer = 0
        vis = [False] * V
        # to store articulation point
        ap = [False] * V
        # to store the time of insertion(first time the node is visited)
        tin = [0] * V
        # to the lowest time of insertion that can be reached from its adjacent nodes
        low = [0] * V

        for i in range(V):
            if not vis[i]:
                dfs(i, -1)

        res = [i for i, v in enumerate(ap) if v]

        return res if len(res) != 0 else [-1]
