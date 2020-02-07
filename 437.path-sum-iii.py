#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.count = 0
        ans = []
        cur = []

        def find(root, newsum):
            if not root:
                return
            if root.val == newsum:
                cur.append(root.val)
                ans.append(cur[:])
                cur.pop()
                self.count += 1
                return
            cur.append(root.val)
            find(root.left, newsum - root.val)
            find(root.right, newsum - root.val)
            find(root.left, sum)
            find(root.right, sum)
            cur.pop()

        find(root, sum)
        print(ans)
        return self.count


# @lc code=end

