/*
 * @lc app=leetcode id=167 lang=cpp
 *
 * [167] Two Sum II - Input array is sorted
 */

// @lc code=start
class Solution {
public:
    vector<int> twoSum(vector<int> &numbers, int target) {
        int l = 0, r = numbers.size() - 1, sum = 0;
        while (l < r) {
            sum = numbers[l] + numbers[r];
            if (sum == target)
                break;
            if (sum < target)
                ++l;
            else
                --r;
        }
        return vector<int>{l + 1, r + 1};
    }
};
// @lc code=end
