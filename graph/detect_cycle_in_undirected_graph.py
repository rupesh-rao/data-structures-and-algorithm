# https://takeuforward.org/practice/dsa/detect-a-cycle-in-an-undirected-graph
class Solution:
    def isCycle(self, N: int, adj: list[list[int]]) -> bool:
        """
        If a node is visited but not by the same parent, then return True for cycle
        """
        def helper(u, parent):
            vis[u] = True
            for v in adj[u]:
                if not vis[v]:
                    if helper(v, u):
                        return True
                elif vis[v] and parent != v:
                    return True
            return False

        vis = [False] * N
        adj = adj
        for i in range(N):
            if not vis[i] and helper(i, -1):
                return True
        return False
