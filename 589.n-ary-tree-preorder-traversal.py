#
# @lc app=leetcode id=589 lang=python3
#
# [589] N-ary Tree Preorder Traversal
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
    def preorder(self, root: "Node") -> List[int]:
        res, q = [], root and [root]
        while q:
            node = q.pop()
            res.append(node.val)
            q += [c for c in reversed(node.children) if c]
        return res

# @lc code=end

