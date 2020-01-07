#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x, y, d):
            if x < 0 or x == len(board[0]) or y < 0 or y == len(board) or board[y][x] != word[d]:
                return False

            if d == len(word) - 1:
                return True

            tmp = board[y][x]
            board[y][x] = 0
            found = dfs(x - 1, y, d + 1) or dfs(x + 1, y, d + 1) or dfs(x, y - 1, d + 1) or dfs(x, y + 1, d + 1)
            board[y][x] = tmp
            return found

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(j, i, 0):
                    return True
        return False

    # @lc code=end
