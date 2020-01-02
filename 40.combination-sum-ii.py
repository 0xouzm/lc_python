#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(target, cur, s):
            if target == 0:
                ans.append(cur[:])
                return
            for i in range(s, len(candidates)):
                if candidates[i] > target:
                    break
                if i != s and candidates[i] == candidates[i - 1]:
                    continue
                cur.append(candidates[i])
                dfs(target - candidates[i], cur, i + 1)
                cur.pop()

        candidates.sort()
        ans = []
        dfs(target, [], 0)
        return ans


# @lc code=end

