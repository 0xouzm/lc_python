from typing import List


# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         ans = []
#         cur = []

#         def dfs(candidates, target, l, cur, ans):
#             if l == len(candidates):
#                 if sum(cur) == 7:
#                     ans.append(cur)
#                     return
#             if sum(cur) == 7:
#                 ans.append(cur)
#                 return

#             for i in candidates:
#                 if sum(cur) + i <= target:
#                     cur.append(candidates[l])
#                     dfs(candidates, target, l, cur, ans)
#                 dfs(candidates, target, l + 1, cur, ans)

#         dfs(candidates, target, 0, cur, ans)
#         return ans


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
                if i > s and candidates[i] == candidates[i - 1]:
                    continue
                cur.append(candidates[i])
                dfs(candidates, target - candidates[i], i + 1, cur, ans)
                cur.pop()

        ans = []
        candidates.sort()
        dfs(candidates, target, 0, [], ans)
        return ans


s = Solution()
print(s.combinationSum2([1, 1, 2, 5, 6, 7], 8))

