from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        d = [" ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        def dfs(digits, d, l, cur, ans):
            if l == len(digits):
                ans.append("".join(cur))
                return
            c = d[int(digits[l])]
            cur[l] = c
            dfs(digits, d, l + 1, cur, ans)

        ans = []
        cur = ["" for _ in range(len(digits))]
        dfs(digits, d, 0, cur, ans)
        return ans


digits = "23"
s = Solution()

print(s.letterCombinations(digits))
