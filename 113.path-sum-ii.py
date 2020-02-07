#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        ans = []
        cur = []

        def dfs(node, vsum):
            if not node:
                return
            if not node.left and not node.right and node.val == vsum:
                ans.append(cur[:])
                ans[-1].append(node.val)
                return
            cur.append(node.val)
            dfs(node.left, vsum - node.val)
            dfs(node.right, vsum - node.val)
            cur.pop()

        dfs(root, sum)
        return ans


# @lc code=end

