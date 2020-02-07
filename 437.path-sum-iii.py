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

        def dfs(root, target):
            if not root:
                return
            test(root, target)
            dfs(root.left, target)
            dfs(root.right, target)

        def test(root, target):
            if not root:
                return
            if target == root.val:
                self.count += 1
            target -= root.val
            test(root.left, target)
            test(root.right, target)

        dfs(root, sum)
        return self.count


# @lc code=end

