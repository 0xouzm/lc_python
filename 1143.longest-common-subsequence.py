#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        l1 = len(text1)
        l2 = len(text2)
        table = [[0] * (l2 + 1) for _ in range(l1 + 1)]

        # def dp(i, j):
        #     if i == -1 or j == -1:
        #         return 0
        #     if (i, j) in memo:
        #         return memo[(i, j)]
        #     if text1[i] == text2[j]:
        #         res = dp(i - 1, j - 1) + 1
        #         memo[(i, j)] = res
        #         return res
        #     else:
        #         memo[(i, j)] = max(dp(i - 1, j), dp(i, j - 1))
        #         res = memo[(i, j)]
        #         return res

        # return dp(len(text1) - 1, len(text2) - 1)
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if text1[i-1] == text2[j-1]:
                    table[i][j] = table[i - 1][j - 1] + 1
                else:
                    table[i][j] = max(table[i - 1][j], table[i][j - 1])

        return table[-1][-1]

# @lc code=end

