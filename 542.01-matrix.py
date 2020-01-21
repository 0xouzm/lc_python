#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#
# https://leetcode.com/problems/01-matrix/description/
#
# algorithms
# Medium (37.82%)
# Likes:    972
# Dislikes: 93
# Total Accepted:    63.9K
# Total Submissions: 168.4K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# Given a matrix consists of 0 and 1, find the distance of the nearest 0 for
# each cell.
#
# The distance between two adjacent cells is 1.
#
#
#
# Example 1:
#
#
# Input:
# [[0,0,0],
# ⁠[0,1,0],
# ⁠[0,0,0]]
#
# Output:
# [[0,0,0],
# [0,1,0],
# [0,0,0]]
#
#
# Example 2:
#
#
# Input:
# [[0,0,0],
# ⁠[0,1,0],
# ⁠[1,1,1]]
#
# Output:
# [[0,0,0],
# ⁠[0,1,0],
# ⁠[1,2,1]]
#
#
#
#
# Note:
#
#
# The number of elements of the given matrix will not exceed 10,000.
# There are at least one 0 in the given matrix.
# The cells are adjacent in only four directions: up, down, left and right.
#
#
#

# @lc code=start
from collections import deque


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])

        def bfs(i, j):
            step = 0
            s = deque([(i, j)])
            visited = set((i, j))
            while s:
                for _ in range(len(s)):
                    y, x = s.popleft()
                    if x < 0 or x == col or y < 0 or y == row:
                        continue
                    if matrix[y][x] == 0:
                        return step
                    if (y, x) in visited:
                        continue
                    s.append((y + 1, x))
                    s.append((y - 1, x))
                    s.append((y, x + 1))
                    s.append((y, x - 1))
                    visited.add((y, x))
                step += 1

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 1:
                    matrix[i][j] = bfs(i, j)
        return matrix


# @lc code=end

