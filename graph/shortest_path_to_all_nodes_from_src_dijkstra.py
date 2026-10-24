# https://takeuforward.org/practice/dsa/dijkstra's-algorithm
# https://leetcode.com/problems/network-delay-time
class Solution:
    def dijkstra(self, V, edges, src):
        # create adjacency list
        adj: list[list[tuple]] = [[] for _ in range(V)]
        for u, v, wt in edges:
            adj[u].append((v, wt))
            adj[v].append((u, wt))

        from heapq import heappush, heappop
        INT_MAX = int(1e9)
        # distance list for all the nodes
        dist = [INT_MAX] * V
        dist[src] = 0
        # min heap
        pq = [(dist[src], src)]

        while pq:
            # pop the shortest distance node
            dis, u = heappop(pq)
            # do edge relaxation for each adjacent node (i.e. update the shortest distance if possible)
            for v, wt in adj[u]:
                if dis + wt < dist[v]:
                    dist[v] = dis + wt
                    # add the shortest distance for future nodes
                    heappush(pq, (dist[v], v))

        return dist

