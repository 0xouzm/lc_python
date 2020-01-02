#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n):
        left = right = n
        ans = []

        def dfs(left, right, cur):
            if right < left:
                return
            if not left and not right:
                ans.append(cur)
                return
            if left:
                dfs(left - 1, right, cur + "(")
            if right:
                dfs(left, right - 1, cur + ")")

        dfs(left, right, "")
        return ans


# @lc code=end

