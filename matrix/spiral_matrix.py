class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        ans = []
        m, n = len(matrix), len(matrix[0])
        left, right = 0, n-1
        up, down = 0, m-1
        dire = 0
        while left <= right and up <= down:
            # left -> right
            if dire%4 == 0:
                for i in range(left, right+1):
                    ans.append(matrix[up][i])
                up += 1
            # up -> down
            elif dire%4 == 1:
                for i in range(up, down+1):
                    ans.append(matrix[i][right])
                right -= 1
            # right -> left
            elif dire%4 == 2:
                for i in range(right, left-1, -1):
                    ans.append(matrix[down][i])
                down -= 1
            # down -> up
            else:
                for i in range(down, up-1, -1):
                    ans.append(matrix[i][left])
                left+=1

            dire += 1
        return ans