# https://takeuforward.org/practice/dsa/floyd-warshall-algorithm
class Solution:
    def shortestDistance(self, matrix):
        v = len(matrix)
        for k in range(v):
            for i in range(v):
                for j in range(v):
                    if matrix[i][k] == -1 or matrix[k][j] == -1:
                        continue

                    if matrix[i][j] == -1:
                        matrix[i][j] = matrix[i][k] + matrix[k][j]
                    else:
                        matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
