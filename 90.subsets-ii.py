#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        def dfs(n, s, cur):
            if n == len(cur):
                ans.append(cur.copy())
                return
            for i in range(s, len(nums)):
                if i > s and nums[i] == nums[i - 1]:
                    continue
                cur.append(nums[i])
                dfs(n, i + 1, cur)
                cur.pop()

        for i in range(len(nums) + 1):
            dfs(i, 0, [])
        return ans


# @lc code=end

