class Solution:
    """
    We can solve using visited array, but it is better to solve by replacing current character with '$' and backtrack.
    """
    def exist(self, board: list[list[str]], word: str) -> bool:
        def travel(ii, jj, k):
            if k == len(word):
                return True
            cur = board[ii][jj]
            board[ii][jj] = '$'
            flag = False
            for x, y in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                if 0 <= ii + x < m and 0 <= jj + y < n and word[k] == board[ii + x][jj + y] and travel(ii + x, jj + y,
                                                                                                       k + 1):
                    flag = True
                    break
            board[ii][jj] = cur
            return flag

        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if travel(i, j, 1):
                        return True
        return False
