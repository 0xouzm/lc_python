#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        maxleft = maxright = 0
        res = 0
        while left<= right :
            if height[left] <= height[right]:
                if height[left]>=maxleft:
                    maxleft = height[left]
                else:
                    res += maxleft - height[left]
                left += 1
            else:
                if height[right]>=maxright:
                    maxright = height[right]
                else:
                    res += maxright -height[right]
                right -= 1
        return res







# @lc code=end

