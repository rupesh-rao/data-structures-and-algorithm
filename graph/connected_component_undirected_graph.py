# https://takeuforward.org/practice/dsa/connected-components
class Solution:
    def findNumberOfComponent(self, V, edges):
        def dfs(u: int):
            vis[u] = True
            for v in adj[u]:
                if not vis[v]:
                    dfs(v)

        vis = [False] * V
        adj: list[list[int]] = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        components = 0
        for i in range(V):
            if not vis[i]:
                dfs(i)
                components += 1
        return components
