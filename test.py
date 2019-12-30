from typing import List

# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         def dfs(nums, d, s, cur, ans):
#             if d == k:
#                 ans.append(cur[:])
#                 return
#             for i in range(s, len(nums)):
#                 cur.append(nums[i])
#                 dfs(nums, d + 1, i + 1, cur, ans)
#                 cur.pop()

#         ans = []
#         dfs(list(range(1, n + 1)), 0, 0, [], ans)
#         return ans
class Solution:
    def combine(self, nums, k):
        ans = []

        def dfs(s, cur):
            if len(cur) == k:
                ans.append(cur[:])
                return
            for i in range(s, len(nums)):
                cur.append(nums[i])
                dfs( i + 1, cur)
                cur.pop()

        dfs(0, [])
        print(ans)


s = Solution()
s.combine(list(range(1,10)), 3)

