# from typing import List


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


# s = Solution()
# print(s.combinationSum([2, 3, 6, 7], 7))



def permutations(nums, d, n, used, cur, ans):
    if d == n:
        ans.append(cur[:])
        return
    for i in range(0, len(nums)):
        if used[i]:
            continue
        used[i] = True
        cur.append(nums[i])
        permutations(nums, d + 1, n, used, cur, ans)
        cur.pop()
        used[i] = False


def combination(nums, d, n, s, cur, ans):
    if d == n:
        ans.append(cur[:])
        return
    for i in range(s, len(nums)):
        cur.append(nums[i])
        combination(nums, d + 1, n, i + 1, cur, ans)
        cur.pop()


ans = []
permutations([1, 2, 3], 0, 3, [False] * 3, [], ans)
print(ans)

c = []

combination([1, 2, 3], 0, 3, 0, [], c)
print(c)

