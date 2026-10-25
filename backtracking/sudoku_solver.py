class Solution:
    def check(self, digit, ind, board):
        row = ind // 9
        col = ind % 9
        for i in range(0, 9):
            if board[row][i] == str(digit) or board[i][col] == str(digit):
                return False
        row = row // 3
        col = col // 3
        for i in range(0, 3):
            for j in range(0, 3):
                if board[i + 3 * row][j + 3 * col] == str(digit):
                    return False
        return True

    def fillBoard(self, ind, board):
        if ind == 81:
            return True
        if board[ind // 9][ind % 9] != '.':
            if self.fillBoard(ind + 1, board):
                return True
            else:
                return False

        for digit in range(1, 10):
            if self.check(digit, ind, board):
                board[ind // 9][ind % 9] = str(digit)
                if self.fillBoard(ind + 1, board):
                    return True
                board[ind // 9][ind % 9] = '.'
        return False

    def solveSudoku(self, board):
        self.fillBoard(0, board)
        return board