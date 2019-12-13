#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i,n in enumerate(nums):
            if n not in d:
                d[n] = i
            foo = target - n
            if foo in d and i != d[foo]:
                return [i,d[foo]]
        return []

        
# @lc code=end

