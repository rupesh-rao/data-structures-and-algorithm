class Solution:
    def topological_sort(self, V, adj: list[list[str]]):
        inDegree = [0] * V
        # calculate the inDegree of all nodes
        for i in range(len(adj)):
            for j in adj[i]:
                inDegree[j] += 1
        from collections import deque
        q = deque()

        for i in range(V):
            if inDegree[i] == 0:
                q.append(i)
        topo = []
        while q:
            i = q.popleft()
            topo.append(i)

            for j in adj[i]:
                inDegree[j] -= 1
                if inDegree[j] == 0:
                    q.append(j)

        return topo

    def findOrder(self, dict, n, k):
        adj = [[] for _ in range(k)]
        for i in range(n - 1):
            # the first character of difference between two consecutive word gives the edge
            for j in range(min(len(dict[i]), len(dict[i + 1]))):
                if dict[i][j] != dict[i + 1][j]:
                    adj[ord(dict[i][j]) - ord('a')].append(ord(dict[i + 1][j]) - ord('a'))
                    break

        topo = self.topological_sort(k, adj)
        if len(topo) == k:
            return " ".join([chr(ord('a') + x) for x in topo])
        else:
            return ""



