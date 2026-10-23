# https://takeuforward.org/practice/dsa/graph-valid-tree
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        inDegree, outDegree = [0] * n, [0] * n

        for u, v in edges:
            inDegree[v] += 1
            outDegree[u] += 1

        root = 0
        maxIn = 0
        maxOut = 0
        for i in range(n):
            if inDegree[i] == 0:
                root += 1
            maxIn = max(maxIn, inDegree[i])
            maxOut = max(maxOut, outDegree[i])

        return root == 1 and maxIn <= 1
