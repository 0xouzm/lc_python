#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        if not s:
            return res
        n = len(s)
        for i in range(n):
            tmp = ""
            for j in range(i, n):
                if s[j] not in tmp:
                    tmp += s[j]
                    res = max(len(tmp), res)
                else:
                    break
        return res


# @lc code=end

