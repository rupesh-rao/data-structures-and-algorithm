# Idea: (Graph Coloring) If alternate coloring of the node is possible then it is bipartite.
class Solution:
    def dfs(self, node, color, current_color, adj):
        # store the current color for the current node
        color[node] = current_color
        # find the next color
        next_color = 1 - current_color

        # check for all the neighboring nodes
        for v in adj[node]:
            # perform dfs if not visited
            if color[v] == -1:
                if not self.dfs(v, color, next_color, adj):
                    return False
            # if neighbor does not have alternate color return false
            elif color[v] != next_color:
                return False
        return True

    def isBipartite(self, V, edges):
        # create adjacency matrix
        adj = [[] for _ in range(V)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        # for storing color of each node
        color = [-1] * V
        # perform dfs on each node
        for i in range(V):
            if color[i] == -1:
                if not self.dfs(i, color, 0, adj):
                    return False
        return True



