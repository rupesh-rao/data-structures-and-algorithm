"""
Minimum Spanning Tree is the minimum sum of weighted edges required to connect all the nodes of a connected, acyclic
undirected graph. It has V-1 edges, where V is the number of nodes
"""

class DSU:
    def __init__(self, v: int):
        self.parent = list(range(v))
        self.rank = [0] * v

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # put smaller rank under bigger self.rank, bigger self.rank becomes self.parent
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        elif self.rank[x] > self.rank[y]:
            self.parent[y] = x
        else:
            self.parent[x] = y
            self.rank[y] += 1


class Solution:
    def spanningTree(self, V, adj):
        edges = []
        for i in range(len(adj)):
            for j, w in adj[i]:
                if i < j:
                    edges.append((i, j, w))
        # sort the edges based on lower weights
        edges.sort(key=lambda x: x[2])
        dsu = DSU(V)
        e = 0
        ans = 0
        # iterate from low to high weight of edges to add V-1 edge only
        for u, v, w in edges:
            parent_u = dsu.find(u)
            parent_v = dsu.find(v)
            if parent_u != parent_v:
                e += 1
                ans += w
                dsu.union(parent_u, parent_v)
            if e == V - 1:
                break

        return ans



