/*
 * @lc app=leetcode id=665 lang=cpp
 *
 * [665] Non-decreasing Array
 */

// @lc code=start
class Solution {
public:
    bool checkPossibility(vector<int> &nums) {
        int n = 0;
        for (int i = 1; i < nums.size() && n <= 1; i++) {
            if (nums[i] < nums[i - 1]) {
                n++;
                if (i < 2 || nums[i - 2] <= nums[i])
                    nums[i - 1] = nums[i];
                else
                    nums[i] = nums[i - 1];
            }
        }
        return n <= 1;
    }
};
// @lc code=end
