#
# @lc app=leetcode id=655 lang=python3
#
# [655] Print Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        def height(root):
            if not root:
                return 0
            return max(height(root.left), height(root.right)) + 1

        h = height(root)
        width = 2 ** h - 1
        res = [["" for _ in range(width)] for _ in range(h)]

        def dfs(root, h, l, r):
            if not root:
                return
            m = l + (r - l) // 2
            res[h][m] = str(root.val)
            dfs(root.left, h + 1, l, m - 1)
            dfs(root.right, h + 1, m + 1, r)

        dfs(root, 0, 0, width - 1)
        return res


# @lc code=end

