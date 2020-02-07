#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo=dict()
        # dp 含义：word1[i] 和 word2[j]之间的最小编辑距离
        def dp(i, j):
            if(i,j) in memo:
                return memo[(i,j)]
            if i == -1:
                return j + 1
            if j == -1:
                return i + 1
            if word1[i] == word2[j]:
                memo[(i,j)] = dp(i - 1, j - 1)
            else:
                memo[(i,j)] = min(dp(i - 1, j) + 1, dp(i, j - 1) + 1, dp(i - 1, j - 1) + 1)
            return memo[(i,j)]

        return dp(len(word1) - 1, len(word2) - 1)


# @lc code=end

