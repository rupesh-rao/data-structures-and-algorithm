class Solution:
    def solveNQueens(self, queen):
        def canPlaceQueen(row, col):
            r,c=row,col
            # top same column
            while r>=0:
                if board[r][c] == 'Q':
                    return False
                r-=1
            # right diagonal
            r,c=row,col
            while r>=0 and c<queen:
                if board[r][c] == 'Q':
                    return False
                r-=1
                c+=1
            # left diagonal
            r,c=row,col
            while r>=0 and c>=0:
                if board[r][c] == 'Q':
                    return False
                r-=1
                c-=1
            return True

        def findNQueen(row):
            if row == queen:
                all_board.append(["".join(r) for r in board])
                return
            for col in range(queen):
                if canPlaceQueen(row, col):
                    board[row][col] = 'Q'
                    findNQueen(row+1)
                    board[row][col] = '.'

        all_board = []
        board = [['.' for _ in range(queen)] for _ in range(queen)]
        findNQueen(0)
        return all_board