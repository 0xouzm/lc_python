#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []

        def inorder(r, k):
            while True:
                while r:
                    stack.append(r)
                    r = r.left
                r = stack.pop()
                k -= 1
                if k == 0:
                    return r.val
                r = r.right

        return inorder(root, k)


# @lc code=end

