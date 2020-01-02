#
# @lc app=leetcode id=301 lang=python3
#
# [301] Remove Invalid Parentheses
#

# @lc code=start


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        l = r = 0
        for i in s:
            if i == "(":
                l += 1
            if i == ")":
                if l > 0:
                    l -= 1
                else:
                    r += 1

        def isValid(s):
            count = 0
            for i in s:
                if i == "(":
                    count += 1
                if i == ")":
                    count -= 1
                if count < 0:
                    return False
            return count == 0

        def dfs(cur, start, l, r):
            if l == 0 and r == 0:
                if isValid(cur):
                    ans.append(cur[:])
                    return
            for i in range(start, len(cur)):
                if i != start and cur[i] == cur[i - 1]:
                    continue
                if cur[i] in ["(", ")"]:
                    tmp = cur
                    tmp = tmp[:i] + tmp[i + 1 :]
                    if l > 0 and cur[i] == "(":
                        dfs(tmp, i, l - 1, r)
                    elif r > 0 and cur[i] == ")":
                        dfs(tmp, i, l, r - 1)

        ans = []
        dfs(s, 0, l, r)
        return ans

# @lc code=end

