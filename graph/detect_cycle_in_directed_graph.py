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

class Solution2:
    def isCyclic(self, V, adj):
        # To store the topological ordering
        topo = self.topoSort(V, adj)

        # If topological sort doesn't include all
        # nodes, the graph is cyclic in nature
        if len(topo) < V:
            return True

        # Else the graph is acyclic
        return False

    # Function to return the topological
    # sorting of given graph
    def topoSort(self, V, adj):
        # To store the result
        ans = []

        # To store the In-degrees of nodes
        inDegree = [0] * V

        # Calculating the In-degree of the given graph
        for i in range(V):
            for it in adj[i]:
                inDegree[it] += 1
        from collections import deque
        # Queue to facilitate BFS
        q = deque()

        # Add the nodes with no in-degree to queue
        for i in range(V):
            if inDegree[i] == 0:
                q.append(i)

        # Until the queue is empty
        while q:
            # Get the node
            node = q.popleft()

            # Add it to the answer
            ans.append(node)

            # Traverse the neighbours
            for it in adj[node]:
                # Decrement the in-degree
                inDegree[it] -= 1

                # Add the node to queue if
                # its in-degree becomes zero
                if inDegree[it] == 0:
                    q.append(it)

        # Return the result
        return ans
