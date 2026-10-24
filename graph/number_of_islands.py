# https://takeuforward.org/practice/dsa/number-of-islands
#
class Solution:
    def numIslands(self, grid):
        def dfs(x, y):
            grid[x][y] = "0"
            for dire in directions:
                dx = dire[0]
                dy = dire[1]
                if 0 <= x + dx < m and 0 <= y + dy < n and grid[x + dx][y + dy] == "1":
                    dfs(x + dx, y + dy)

        directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 0], [0, 1], [1, -1], [1, 0], [1, 1]]
        count = 0
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)
        return count

