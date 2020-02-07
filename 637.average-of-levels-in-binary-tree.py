#
# @lc app=leetcode id=637 lang=python3
#
# [637] Average of Levels in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        # ans = []
        # count = []

        # def dfs(root, depth):
        #     if not root:
        #         return
        #     if depth >= len(count):
        #         count.append([0, 0])
        #     count[depth][0] += root.val
        #     count[depth][1] += 1
        #     dfs(root.left, depth + 1)
        #     dfs(root.right, depth + 1)

        # dfs(root, 0)
        # for s, c in count:
        #     ans.append(s / c)

        # return ans
        ans = []
        cur, nxt = [root], []
        while cur:
            s = 0
            for node in cur:
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
                s += node.val
            ans.append(s / len(cur))
            cur = nxt[:]
            nxt.clear()
        return ans


# @lc code=end

