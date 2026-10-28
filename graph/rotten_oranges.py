from collections import deque


class Solution:
    def orangesRotting(self, grid):
        def bfs(x, y):
            level = 0
            q = deque()
            q.append((x, y))
            vis[x][y] = True

            while q:
                level += 1
                size = len(q)
                # print(level, q)
                for _ in range(size):
                    nx, ny = q.popleft()

                    for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                        if 0 <= nx + dx < m and 0 <= ny + dy < n and grid[nx+ dx][
                            ny + dy] == 1 and not vis[nx+ dx][ny + dy]:
                            vis[nx+ dx][ny + dy] = True
                            grid[nx+ dx][ny + dy] = 2
                            q.append((nx+ dx, ny + dy))
            return max(level-1, 0)

        m, n = len(grid), len(grid[0])
        vis = [[False] * n for _ in range(m)]
        max_time = -1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2 and not vis[i][j]:
                    cur_time = bfs(i, j)
                    max_time = max(cur_time, max_time)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1

        return max_time


