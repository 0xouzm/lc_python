#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (44.04%)
# Likes:    2904
# Dislikes: 352
# Total Accepted:    494.4K
# Total Submissions: 1.1M
# Testcase Example:  '"23"'
#
# Given a string containing digits from 2-9 inclusive, return all possible
# letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given
# below. Note that 1 does not map to any letters.
#
#
#
# Example:
#
#
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
#
#
# Note:
#
# Although the above answer is in lexicographical order, your answer could be
# in any order you want.
#
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # dfs
        if not digits:
            return []
        d = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        ans = []
        n = len(digits)

        def dfs(l, cur):
            if len(cur) == n:
                ans.append(cur[:])
                return
            for c in d[int(digits[l])]:
                cur += c
                dfs(l + 1, cur)
                cur = cur[:-1]
        dfs(0,"")
        return ans

        # bfs
        # if not digits: return []
        # ans = [""]
        # d = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        # for digit in digits:
        #     tmp = []
        #     for s in ans:
        #         for c in d[int(digit)]:
        #             tmp.append(s+c)
        #     ans = tmp
        # return ans


# @lc code=end
