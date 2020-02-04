#
# @lc app=leetcode id=429 lang=python3
#
# [429] N-ary Tree Level Order Traversal
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: "Node") -> List[List[int]]:
        def preorder(root, d, ans):
            if not root:
                return
            while len(ans) <= d:
                ans.append([])
            ans[d].append(root.val)
            for child in root.children:
                preorder(child, d + 1, ans)

        ans = []
        preorder(root, 0, ans)
        return ans


# @lc code=end

