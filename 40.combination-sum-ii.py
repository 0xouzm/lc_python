#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, target, s, cur, ans):
            if target == 0:
                ans.append(cur[:])
                return
            for i in range(s, len(candidates)):
                if candidates[i] > target:
                    return
                # remove duplicate number
                # i>s,判断不是第一个元素,同一层不能继续使用,比如有两个1,对于当前这层递归循环,只能使用一个1
                # 重点注意i和s分别控制的关系
                if i > s and candidates[i] == candidates[i - 1]:
                    continue
                cur.append(candidates[i])
                dfs(candidates, target - candidates[i], i + 1, cur, ans)
                cur.pop()

        ans = []
        candidates.sort()
        dfs(candidates, target, 0, [], ans)
        return ans


# @lc code=end

