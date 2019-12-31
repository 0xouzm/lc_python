#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(d, n, used, cur):
            if d == n:
                ans.append(cur[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                cur.append(nums[i])
                dfs(d + 1, n, used, cur)
                used[i] = False
                cur.pop()

        dfs(0, len(nums), [False] * len(nums), [])
        return ans


# @lc code=end

