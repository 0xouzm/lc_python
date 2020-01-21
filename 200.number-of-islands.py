#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (44.18%)
# Likes:    3833
# Dislikes: 140
# Total Accepted:    514.3K
# Total Submissions: 1.2M
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of
# islands. An island is surrounded by water and is formed by connecting
# adjacent lands horizontally or vertically. You may assume all four edges of
# the grid are all surrounded by water.
# 
# Example 1:
# 
# 
# Input:
# 11110
# 11010
# 11000
# 00000
# 
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input:
# 11000
# 11000
# 00100
# 00011
# 
# Output: 3
# 
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        ans = 0
        rows = len(grid)
        cols = len(grid[0])
        def dfs(y,x):
            if y<0 or y == rows or x<0 or x== cols or grid[y][x] == "0":
                return
            grid[y][x] = "0"
            dfs(y+1,x)
            dfs(y-1,x)
            dfs(y,x+1)
            dfs(y,x-1)

        for y in range(rows):
            for x in range(cols):
                if grid[y][x] == "1":
                    ans += 1
                    dfs(y,x)
        return ans
        
        
# @lc code=end

