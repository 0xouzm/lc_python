#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(l, r):
            if not l and not r:
                return True
            if not l or not r:
                return False
            return all(
                (l.val == r.val, isMirror(l.left, r.right), isMirror(l.right, r.left),)
            )

        return isMirror(root, root)


# @lc code=end

