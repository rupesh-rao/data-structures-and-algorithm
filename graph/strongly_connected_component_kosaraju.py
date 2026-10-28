"""
A strongly connected component is a maximal group of vertices where every
vertex can reach every other vertex through directed paths.

Algorithm:
1. Sort all the nodes according to their finishing time:
2. Find transpose of the graph (reverse the direction of edges)
3. Perform the DFS and count the number of different DFS calls to get the number of SCC

"""


class Solution:
    def kosaraju(self, V, adj):
        # dfs 1 to store nodes in stack
        def dfs(u):
            vis[u] = True
            for v in adj[u]:
                if not vis[v]:
                    dfs(v)
            st.append(u)

        # dfs 2 to visit the transpose graph
        def dfs1(u):
            vis[u] = True
            for v in adjT[u]:
                if not vis[v]:
                    dfs1(v)

        # to store the nodes in the descending order of visiting time
        st = []
        vis = [False] * V
        # perform 1st dfs
        for i in range(V):
            if not vis[i]:
                dfs(i)

        # create transpose graph
        adjT = [[] for _ in range(V)]
        for i in range(len(adj)):
            for j in adj[i]:
                adjT[j].append(i)

        count = 0
        vis = [False] * V
        # perform 2nd dfs
        while st:
            node = st.pop()
            if not vis[node]:
                dfs1(node)
                count += 1

        return count





