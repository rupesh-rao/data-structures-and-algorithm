# https://leetcode.com/problems/course-schedule
# https://takeuforward.org/practice/dsa/course-schedule-i
class Solution:
    def canFinish(self, n, edges):
        """
        use topological sort to find the course that can be covered
        """
        inDegree = [0] * n
        adj: list[list[int]] = [[] for _ in range(n)]
        for v, u in edges:
            inDegree[v] += 1
            adj[u].append(v)

        from collections import deque
        q = deque()
        for i in range(n):
            if inDegree[i] == 0:
                q.append(i)
        course_taken = 0
        while q:
            node = q.popleft()
            course_taken += 1
            for child in adj[node]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    q.append(child)

        return course_taken == n

