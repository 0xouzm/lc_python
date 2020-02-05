#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isBalanced(self, root):
        self.balanced = True

        def height(root):
            if not root or not self.balanced:
                return 0
            l = height(root.left)
            r = height(root.right)
            if abs(l - r) > 1:
                self.balanced = False
                return 0
            return max(l, r) + 1

        height(root)
        return self.balanced


# @lc code=end

