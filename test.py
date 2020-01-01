from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(d, n, used, cur):
            if d == n:
                ans.append(cur[:])
                return
            for i in range(len(nums)):
                if used & 1 << i:
                    continue
                cur.append(nums[i])
                dfs(d + 1, n, used | 1 << i, cur)
                cur.pop()

        dfs(0, len(nums), 0, [])
        return ans
s = Solution()
ans = s.permute([1,2,3])
print(ans)