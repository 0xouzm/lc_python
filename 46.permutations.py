#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # def dfs(nums, d, n, used, cur, ans):
        #     if d == n:
        #         ans.append(cur[:])
        #         return
        #     for i in range(len(nums)):
        #         if used[i]:
        #             continue
        #         uesd[i] = True
        #         cur.append(nums[i])
        #         dfs(nums, d + 1, n, used, cur, ans)
        #         used[i] = False
        #         cur.pop()

        # ans = []
        # dfs(nums, 0, len(nums), [False] * len(nums), [], ans)
        # return ans
        def dfs(nums, d, n, used, cur, ans):
            if n == d:
                ans.append(cur[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                cur.append(nums[i])
                dfs(nums, d + 1, n, used, cur, ans)
                used[i] = False
                cur.pop()

        ans = []
        dfs(nums, 0, len(nums), [False] * len(nums), [], ans)
        return ans


# @lc code=end

