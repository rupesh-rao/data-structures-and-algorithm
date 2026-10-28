"""
An edge is a "bridge" if its removal makes some vertex unable to reach another vertex in connected graph.
"""

class Solution:
    def __init__(self):
        self.timer = 0

    def criticalConnections(self, V, E):
        def dfs(node, parent):
            vis[node] = True
            tin[node] = self.timer
            low[node] = self.timer
            self.timer += 1

            for adjNode in adj[node]:
                if adjNode == parent:
                    continue
                if not vis[adjNode]:
                    dfs(adjNode, node)
                    # update the lowest time of insertion of current node
                    # compare with adjacent node's low array value
                    low[node] = min(low[node], low[adjNode])

                    # if lowest insertion time of adjNode is greater than time of the insertion of node
                    # it means there is no edge in adjNode to an ancestor of current node
                    if low[adjNode] > tin[node]:
                        bridge.append([adjNode, node])
                else:
                    # update the lowest time of insertion of current node
                    # compare with adjNode's tin array value because it is visited before current node
                    low[node] = min(low[node], tin[adjNode])

        self.timer = 0
        adj: list[list[int]] = [[] for _ in range(V)]
        vis = [False] * V
        # to store the time of insertion(first time the node is visited)
        tin = [0] * V
        # to the lowest time of insertion that can be reached from its adjacent nodes
        low = [0] * V
        # create adjacency list
        for u, v in E:
            adj[u].append(v)
            adj[v].append(u)
        # do dfs and find bridges
        bridge = []
        dfs(0, -1)

        return bridge


