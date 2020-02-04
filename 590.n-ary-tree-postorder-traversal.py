#
# @lc app=leetcode id=590 lang=python3
#
# [590] N-ary Tree Postorder Traversal
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
    def postorder(self, root: "Node") -> List[int]:
        res, s = [], root and [root]
        while s:
            node = s.pop()
            res.append(node.val)
            s += [c for c in node.children if c]

        return res[::-1]


# @lc code=end

