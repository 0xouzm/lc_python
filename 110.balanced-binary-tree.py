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
    def isBalanced(self, root: TreeNode) -> bool:
        def height(node):
            return 1 + max(map(height, (node.left, node.right))) if node else 0

        if root is None:
            return True
        lh = height(root.left)
        rh = height(root.right)

        if (
            abs(lh - rh) <= 1
            and self.isBalanced(root.left)
            and self.isBalanced(root.right)
        ):
            return True
        return False


# @lc code=end

