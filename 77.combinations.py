#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(nums, d, s, cur, ans):
            if d == k:
                ans.append(cur[:])
                return
            for i in range(s, len(nums)):
                cur.append(nums[i])
                dfs(nums, d + 1, i + 1, cur, ans)
                cur.pop()

        ans = []
        dfs(list(range(1, n + 1)), 0, 0, [], ans)
        return ans


# @lc code=end

