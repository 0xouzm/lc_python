#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(cur, s, d):
            if len(cur) == d:
                ans.append(cur[:])
                return
            for i in range(s, len(nums)):
                if i != s and nums[i] == nums[i - 1]:
                    continue
                cur.append(nums[i])
                dfs(cur, i + 1, d)
                cur.pop()

        ans = []
        nums.sort()
        for i in range(len(nums) + 1):
            dfs([], 0, i)

        return ans


# @lc code=end

