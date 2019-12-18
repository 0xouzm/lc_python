#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#
# https://leetcode.com/problems/partition-equal-subset-sum/description/
#
# algorithms
# Medium (41.91%)
# Likes:    1711
# Dislikes: 51
# Total Accepted:    124.1K
# Total Submissions: 296.1K
# Testcase Example:  '[1,5,11,5]'
#
# Given a non-empty array containing only positive integers, find if the array
# can be partitioned into two subsets such that the sum of elements in both
# subsets is equal.
#
# Note:
#
#
# Each of the array element will not exceed 100.
# The array size will not exceed 200.
#
#
#
#
# Example 1:
#
#
# Input: [1, 5, 11, 5]
#
# Output: true
#
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
#
#
#
#
# Example 2:
#
#
# Input: [1, 2, 3, 5]
#
# Output: false
#
# Explanation: The array cannot be partitioned into equal sum subsets.
#
#
#
#
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # s = sum(nums)
        # n = len(nums)
        # memo = {0: True}
        # if s & 1:
        #     return False
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

        # return dfs(0, s >> 1)
        target = sum(nums)
        n = len(nums)

        if target & 1:
            return False
        # dp solution
        # dp = [True] + [False] * target
        # for x in nums:
        #     dp = [dp[s] or (s >= x and dp[s - x]) for s in range(target + 1)]
        #     if dp[target]:
        #         return True
        # return False

        # 回溯 solution
        memo = {0: True}
        nums.sort(reverse=True)

        def dfs(i, x):
            if x not in memo:
                memo[x] = False
                if x > 0:
                    # 选这个数,看能否刚好减到0
                    for j in range(i, n):
                        if dfs(j + 1, x - nums[j]):
                            memo[x] = True
                            break
            return memo[x]

        return dfs(0, target >> 1)


# @lc code=end

