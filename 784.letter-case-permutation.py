#
# @lc app=leetcode id=784 lang=python3
#
# [784] Letter Case Permutation
#

# @lc code=start
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        ans = []
        n = len(S)

        def dfs(s, cur):
            if len(cur) == n:
                ans.append(cur[:])
                return
            for i in range(s, n):
                if S[i].isalpha():
                    dfs(i + 1, cur + S[i])
                    dfs(i + 1, cur + chr(ord(S[i]) ^ 32))
                else:
                    dfs(i + 1, cur + S[i])

        dfs(0, "")
        return ans

    # def letterCasePermutation(self, S: str) -> List[str]:
    #     ans = []
    #     n = len(S)

    #     def dfs(S, i):
    #         if i == n:
    #             ans.append("".join(S))
    #             return
    #         dfs(S, i + 1)
    #         if S[i].isdigit():
    #             return
    #         S[i] = chr(ord(S[i]) ^ 32)
    #         dfs(S, i + 1)
    #         S[i] = chr(ord(S[i]) ^ 32)

    #     dfs(list(S), 0)

    #     return ans


# @lc code=end

