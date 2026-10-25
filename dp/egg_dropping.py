# https://leetcode.com/problems/super-egg-drop
# Read solution: https://leetcode.com/problems/super-egg-drop/solutions/158974/cjavapython-2d-and-1d-dp-oklogn-by-lee21-xfs9
# Read comment for explanation: https://leetcode.com/problems/super-egg-drop/solutions/158974/cjavapython-2d-and-1d-dp-oklogn-by-lee21-xfs9/comments/167591/?parent=164636

class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        # k eggs, n floors
        # change problem to finding number of floor that can checked by using m moves and k eggs
        # dp[m][k] = dp[m-1][k] + dp[m-1][k-1] + 1
        # dp[m][k] = number of floors that can be checked by m moved and k eggs
        # dp[m-1][k] = number of floors that can be checked when egg does not break, m (moves) reduced by 1, k (egg) not reduced
        # dp[m-1][k-1] = number of floors that can be checked when egg breaks, m (moves) reduced by 1, k (eggs) reduced by 1

        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for m in range(1, n + 1):
            for i in range(1, k + 1):
                dp[m][i] = dp[m - 1][i] + dp[m - 1][i - 1] + 1
            if dp[m][k] >= n:
                return m

        return -1
