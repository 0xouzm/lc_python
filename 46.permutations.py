#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        def dfs(used, cur):
            if len(cur) == n:
                ans.append(cur[:])
                return
            for i in range(n):
                if used & 1 << i:
                    continue
                cur.append(nums[i])
                # dfs(used + 2 ** i, cur)
                dfs(used | 1 << i, cur)
                cur.pop()

        dfs(0, [])
        return ans


# @lc code=end

