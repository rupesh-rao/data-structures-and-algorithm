class Solution:
    # Note: Swap and Reverse does 90 clockwise
    # while, reverse and swap does 90 anti-clockwise

    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # swap
        for i in range(n):
            for j in range(i + 1):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # reverse row
        for i in range(n):
            matrix[i].reverse()

