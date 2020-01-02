#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = list(range(1, 10))
        ans = []

        def dfs(target, s, cur):
            if target == 0 and len(cur) == k:
                ans.append(cur[:])
                return
            for i in range(s, 9):
                if nums[i] > target:
                    break
                cur.append(nums[i])
                dfs(target - nums[i], i + 1, cur)
                cur.pop()

        dfs(n, 0, [])
        return ans
        # nums = list(range(1, 10))
        # ans = []

        # def dfs(s, cur):
        #     if len(cur) == k and sum(cur) == n:
        #         ans.append(cur[:])
        #         return
        #     for i in range(s, 9):
        #         cur.append(nums[i])
        #         dfs(i + 1, cur)
        #         cur.pop()

        # dfs(0, [])
        # return ans


# Your runtime beats 89.15 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.5 MB)
# @lc code=end

