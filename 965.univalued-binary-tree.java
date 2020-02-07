/*
 * @lc app=leetcode id=965 lang=java
 *
 * [965] Univalued Binary Tree
 */

// @lc code=start
/**
 * Definition for a binary tree node. public class TreeNode { int val; TreeNode
 * left; TreeNode right; TreeNode(int x) { val = x; } }
 */
class Solution {
    int val = -1;
    public boolean isUnivalTree(TreeNode root) {
        if (root == null)
            return true;
        if (val < 0)
            val = root.val;
        return root.val == val && isUnivalTree(root.left) && isUnivalTree(root.right);

    }
}
// @lc code=end
