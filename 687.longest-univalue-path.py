#
# @lc app=leetcode id=687 lang=python3
#
# [687] Longest Univalue Path
#
# https://leetcode.com/problems/longest-univalue-path/description/
#
# algorithms
# Easy (34.85%)
# Likes:    1253
# Dislikes: 332
# Total Accepted:    73.9K
# Total Submissions: 211.9K
# Testcase Example:  '[5,4,5,1,1,5]'
#
# Given a binary tree, find the length of the longest path where each node in
# the path has the same value. This path may or may not pass through the root.
#
# The length of path between two nodes is represented by the number of edges
# between them.
#
#
#
# Example 1:
#
# Input:
#
#
# ⁠             5
# ⁠            / \
# ⁠           4   5
# ⁠          / \   \
# ⁠         1   1   5
#
#
# Output: 2
#
#
#
# Example 2:
#
# Input:
#
#
# ⁠             1
# ⁠            / \
# ⁠           4   5
# ⁠          / \   \
# ⁠         4   4   5
#
#
# Output: 2
#
#
#
# Note: The given binary tree has not more than 10000 nodes. The height of the
# tree is not more than 1000.
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root.left and root.right and root.left.val == root.right.val:
            return (
                max(
                    self.longestUnivaluePath(root.left),
                    self.longestUnivaluePath(root.right),
                )
                + 1
            )
        else:
            return max(
                self.longestUnivaluePath(root.left),
                self.longestUnivaluePath(root.right),
            )


# @lc code=end

