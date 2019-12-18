from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        n = len(nums)
        memo = {0: True}
        pick = []
        if s & 1:
            return False
        # nums.sort(reverse=True)

        # def dfs(i, x):
        #     if x not in memo:
        #         memo[x] = False
        #         if x > 0:
        #             for j in range(i, n):
        #                 if dfs(j + 1, x - nums[j]):
        #                     memo[x] = True
        #                     break
        #     return memo[x]
        # status = dfs(0, s >> 1)
        # print(memo)
        # return status

s = Solution()
print(s.canPartition([1, 5, 11, 5]))

