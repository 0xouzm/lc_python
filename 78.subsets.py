#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # def dfs(nums, n, d, s, cur, ans):
        #     if n == d:
        #         ans.append(cur[:])
        #         return
        #     for i in range(s, len(nums)):
        #         cur.append(nums[i])
        #         dfs(nums, n, d + 1, i + 1, cur, ans)
        #         cur.pop()

        # ans = []
        # for i in range(len(nums) + 1):
        #     dfs(nums, i, 0, 0, [], ans)
        # return ans

        # ans = []

        # def dfs(n, s, cur):
        #     if n == len(cur):
        #         ans.append(cur[:])
        #         return
        #     for i in range(s, len(nums)):
        #         cur.append(nums[i])
        #         dfs(n, i + 1, cur)
        #         cur.pop()

        # for i in range(len(nums) + 1):
        #     dfs(i, 0, [])
        # return ans
        n = len(nums)
        return [[nums[i] for i in range(n) if s & 1 << i] for s in range(1 << n)]


# @lc code=end

