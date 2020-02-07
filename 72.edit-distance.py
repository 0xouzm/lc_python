#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp 含义：word1[i] 和 word2[j]之间的最小编辑距离
        m = len(word1)
        n = len(word2)
        table = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            table[i][0] = i
        for j in range(1, n + 1):
            table[0][j] = j
        print(table)
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i - 1] == word2[j - 1]:
                    table[i][j] = table[i - 1][j - 1]
                else:
                    table[i][j] = min(
                        table[i - 1][j] + 1,
                        table[i][j - 1] + 1,
                        table[i - 1][j - 1] + 1,
                    )

        return table[m][n]


# @lc code=end

