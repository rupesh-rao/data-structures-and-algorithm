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


class Solution2:
    # using Union-Find Algorithm
    def isCycle(self, N: int, adj: list[list[int]]) -> bool:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            # put smaller rank under bigger rank, bigger rank becomes parent
            if rank[x] < rank[y]:
                parent[x] = y
            elif rank[x] > rank[y]:
                parent[y] = x
            else:
                parent[x] = y
                rank[y] += 1

        parent = list(range(N))
        rank = [0] * N
        edges = []

        for u in range(len(adj)):
            for v in adj[u]:
                # avoid adding duplicate edge
                if u < v:
                    edges.append([u, v])

        for edge in edges:
            x = find(edge[0])
            y = find(edge[1])
            # if parent of both node is same, there is a cycle
            if x == y:
                return True
            # union them
            union(x, y)
        return False

