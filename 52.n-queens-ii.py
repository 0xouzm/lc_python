#
# @lc app=leetcode id=52 lang=python3
#
# [52] N-Queens II
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        def DFS(queens, xy_diff, xy_sum):
            nonlocal count
            q = len(queens)
            if q == n:
                count += 1
                return
            for p in range(n):
                if p not in queens and p - q not in xy_diff and p + q not in xy_sum:
                    DFS(queens + [p], xy_diff + [p - q], xy_sum + [p + q])
        count = 0
        DFS([],[],[])
        return count


# @lc code=end

