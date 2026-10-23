# https://takeuforward.org/practice/dsa/detect-a-cycle-in-a-directed-graph
class Solution:
    def isCyclic(self, N, adj):
        """
        Use recStack to find if the node is visited in the current DFS path.
        vis is not reliable as it may be visited by some other path
        """
        def helper(u):
            vis[u] = True
            recStack[u] = True
            for v in adj[u]:
                if not vis[v] and helper(v):
                    return True
                if recStack[v]:
                    return True
            recStack[u] = False
            return False

        vis = [False] * N
        recStack = [False] * N

        for i in range(N):
            if not vis[i] and helper(i):
                return True

        return False
