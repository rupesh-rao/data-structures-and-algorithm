class Solution:

    def pacificAtlantic(self, a: list[list[int]]) -> list[list[int]]:
        def dfs(x, y, h, vis):
            # h is the height of prev cell.
            # here we are thinking opposite movement of water from ocean to cell
            # hence, return if current cell is not taller than prev cell
            if x < 0 or y < 0 or x == m or y == n or vis[x][y] or a[x][y] < h:
                return
            vis[x][y] = True
            for k in dire:
                xi = x + k[0]
                yi = y + k[1]

                dfs(xi, yi, a[x][y], vis)

        dire = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        m = len(a)
        n = len(a[0])

        vis1 = [[False] * n for _ in range(m)]
        vis2 = [[False] * n for _ in range(m)]

        for i in range(m):
            dfs(i, 0, -1, vis1)  # left
            dfs(i, n - 1, -1, vis2)  # right

        for i in range(n):
            dfs(0, i, -1, vis1)  # top
            dfs(m - 1, i, -1, vis2)  # right

        ans = []
        for i in range(m):
            for j in range(n):
                if vis1[i][j] and vis2[i][j]:
                    ans.append([i, j])

        return ans









