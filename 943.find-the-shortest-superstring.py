#
# @lc app=leetcode id=943 lang=python3
#
# [943] Find the Shortest Superstring
#

# @lc code=start
class Solution:
    def shortestSuperstring(self, A: List[str]) -> str:
        n = len(A)
        g_ = [[None] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                g_[i][j] = len(A[j])
                for k in range(1, min(len(A[i]), len(A[j])) + 1):
                    d1 = A[i][-k:]
                    d2 = A[j][:k]
                    if d1 == d2:
                        g_[i][j] = len(A[j]) - k
        path = [0] * n
        best_path = [0] * n
        best_len = float("inf")

        def dfs(d, used, cur_len):
            nonlocal best_len
            nonlocal best_path
            if cur_len >= best_len:
                return
            if d == n:
                best_len = cur_len
                best_path = path[:]
                return
            for i in range(n):
                if used & 1 << i:
                    continue
                path[d] = i
                dfs(
                    d + 1,
                    used | 1 << i,
                    len(A[i]) if d == 0 else cur_len + g_[path[d - 1]][i],
                )

        dfs(0, 0, 0)
        ans = A[best_path[0]]
        for k in range(1, n):
            i = best_path[k - 1]
            j = best_path[k]
            tmp =A[j][len(A[j]) - g_[i][j]:]
            ans += tmp
        return ans


# @lc code=end

