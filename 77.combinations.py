#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(cur, s):
            if len(cur) == k:
                ans.append(cur[:])
                return
            for i in range(s, n + 1):
                cur.append(i)
                dfs(cur, i + 1)
                cur.pop()

        ans = []
        dfs([], 1)
        return ans


# @lc code=end

