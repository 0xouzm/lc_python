#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        def dfs(used, cur):
            if len(cur) == n:
                ans.append(cur[:])
                return
            for i in range(n):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                cur.append(nums[i])
                dfs(used, cur)
                used[i] = False
                cur.pop()
        
        nums.sort()
        dfs([False] * n, [])
        return ans


# @lc code=end

