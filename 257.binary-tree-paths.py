#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        ans = []
        cur = []
        def dfs(root):
            if not root:
                return
            if not root.left and not root.right:
                cur.append(str(root.val))
                ans.append('->'.join(cur))
                cur.pop()
                return 
            cur.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
            cur.pop()

        dfs(root)
        return ans


            
# @lc code=end

