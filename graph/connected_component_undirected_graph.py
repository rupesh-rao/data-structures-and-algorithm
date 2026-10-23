# https://takeuforward.org/practice/dsa/connected-components
class Solution:
    def findNumberOfComponent(self, V, edges):
        def dfs(u):
            vis[u] = True
            for v in adj[u]:
                if not vis[v]:
                    dfs(v)

        vis = [False] * V
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        components = 0
        for i in range(V):
            if not vis[i]:
                dfs(i)
                components += 1
        return components
