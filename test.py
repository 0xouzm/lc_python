from typing import List


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



# class Solution {
#   private int n;
#   private int[][] g;
#   private String[] a;
#   private int best_len;
#   private int[] path;
#   private int[] best_path;

#   private void dfs(int d, int used, int cur_len) {
#     if (cur_len >= best_len) return;
#     if (d == n) {
#       best_len = cur_len;
#       best_path = path.clone();
#       return;
#     }

#     for (int i = 0; i < n; ++i) {
#       if ((used & (1 << i)) != 0) continue;
#       path[d] = i;
#       dfs(d + 1,
#           used | (1 << i),
#           d == 0 ? a[i].length() : cur_len + g[path[d - 1]][i]);
#     }
#   }

#   public String shortestSuperstring(String[] A) {
#     n = A.length;
#     g = new int[n][n];
#     a = A;
#     for (int i = 0; i < n; ++i)
#       for (int j = 0; j < n; ++j) {
#         g[i][j] = A[j].length();
#         for (int k = 1; k <= Math.min(A[i].length(), A[j].length()); ++k)
#           if (A[i].substring(A[i].length() - k).equals(A[j].substring(0, k)))
#             g[i][j] = A[j].length() - k;
#       }

#     path = new int[n];
#     best_len = Integer.MAX_VALUE;

#     dfs(0, 0, 0);

#     String ans = A[best_path[0]];
#     for (int k = 1; k < n; ++k) {
#       int i = best_path[k - 1];
#       int j = best_path[k];
#       ans += A[j].substring(A[j].length() - g[i][j]);
#     }
#     return ans;
#   }
# }
s = Solution()
ans = s.shortestSuperstring(["alex","loves","leetcode"])
print(ans)

