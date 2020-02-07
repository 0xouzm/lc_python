#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def build(l, r):
            if l > r:
                return None
            m = l + (r - l) // 2
            root = TreeNode(nums[m])
            root.left = build(l, m - 1)
            root.right = build(m + 1, r)
            return root

        return build(0, len(nums) - 1)


# @lc code=end

