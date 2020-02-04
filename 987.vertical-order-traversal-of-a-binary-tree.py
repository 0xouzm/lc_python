#
# @lc app=leetcode id=987 lang=python3
#
# [987] Vertical Order Traversal of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        vals = []

        def preorder(root, x, y):
            if not root:
                return
            vals.append((x, y, root.val))
            preorder(root.left, x - 1, y + 1)
            preorder(root.right, x + 1, y + 1)

        preorder(root, 0, 0)
        ans = []
        last_x = -1000
        for x, _, val in sorted(vals):
            if x != last_x:
                ans.append([])
                last_x = x
            ans[-1].append(val)
        return ans


# @lc code=end

