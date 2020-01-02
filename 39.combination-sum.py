#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
# https://leetcode.com/problems/combination-sum/description/
#
# algorithms
# Medium (52.16%)
# Likes:    2775
# Dislikes: 86
# Total Accepted:    437K
# Total Submissions: 835.5K
# Testcase Example:  '[2,3,6,7]\n7'
#
# Given a set of candidate numbers (candidates) (without duplicates) and a
# target number (target), find all unique combinations in candidates where the
# candidate numbers sums to target.
#
# The same repeated number may be chosen from candidates unlimited number of
# times.
#
# Note:
#
#
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
#
#
# Example 1:
#
#
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
# ⁠ [7],
# ⁠ [2,2,3]
# ]
#
#
# Example 2:
#
#
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
# [2,2,2,2],
# [2,3,3],
# [3,5]
# ]
#
#
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(cur, s, target):
            if target == 0:
                ans.append(cur[:])
                return

            for i in range(s, len(candidates)):
                if candidates[i] > target:
                    break
                cur.append(candidates[i])
                dfs(cur, i, target - candidates[i])
                cur.pop()

        ans = []
        candidates.sort()
        dfs([], 0, target)
        return ans


# @lc code=end

