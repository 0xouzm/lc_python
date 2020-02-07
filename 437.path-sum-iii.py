#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.count = 0

        def dfs(root, newsum):
            if not root:
                return
            if root.val == newsum:
                self.count += 1
                return
            dfs(root.left, newsum - root.val)
            dfs(root.right, newsum - root.val)
            dfs(root.left, sum)
            dfs(root.right, sum)

        dfs(root, sum)

        return self.count


# @lc code=end

