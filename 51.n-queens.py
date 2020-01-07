#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []

        def dfs(queens, xy_sum, xy_dif):
            p = len(queens)
            if p == n:
                ans.append(queens)
                return

            for q in range(n):
                if q not in queens and p + q not in xy_sum and p - q not in xy_dif:
                    dfs(queens + [q], xy_sum + [p + q], xy_dif + [p - q])

        dfs([], [], [])

        return [["." * i + "Q" + "." * (n - i - 1) for i in s] for s in ans]


# @lc code=end
