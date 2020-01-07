#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []

        def dfs(row, cur):
            if row == n:
                ans.append(cur[:])
                return

            for i in range(n):
                pass


# @lc code=end

