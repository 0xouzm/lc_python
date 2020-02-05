/*
 * @lc app=leetcode id=111 lang=java
 *
 * [111] Minimum Depth of Binary Tree
 */

// @lc code=start
/**
 * Definition for a binary tree node. public class TreeNode { int val; TreeNode
 * left; TreeNode right; TreeNode(int x) { val = x; } }
 */
class Solution {
    public int minDepth(TreeNode root) {
        if (root == null)
            return 0;
        int m1 = minDepth(root.left);
        int m2 = minDepth(root.right);
        if (root.left == null || root.right == null)
            return m1 + m2 + 1;
        return Math.min(m1, m2) + 1;

    }
}
// @lc code=end
