#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp 含义：word1[0...i] 和 word2[0...j]之间的最小编辑距离
        m = len(word1)
        n = len(word2)
        # tuple第一个代表距离，第二个代表操作
        #  0 代表啥都不做
        #  1 代表插入
        #  2 代表删除
        #  3 代表替换
        table = [[0] * (n + 1) for _ in range(m + 1)]
        choices = [[0] * (n + 1) for _ in range(m + 1)] 
        for i in range(1, m + 1):
            table[i][0]= i
        for j in range(1, n + 1):
            table[0][j]= j
        # 这里注意range 范围
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    table[i][j]= table[i - 1][j - 1]
                else:
                    table[i][j]= min(
                        # insert
                        table[i][j - 1] + 1,
                        # delete
                        table[i - 1][j] + 1,
                        # replace
                        table[i - 1][j - 1] + 1,
                    )
                    if table[i][j] == table[i][j - 1]+1:
                        choices[i][j] = 1
                    elif table[i][j] == table[i - 1][j]+1:
                        choices[i][j] = 2
                    elif table[i][j] == table[i - 1][j - 1]+1:
                        choices[i][j] = 3
        print(table)
        print(choices)

        return table[m][n]


# @lc code=end

