/*
 * @lc app=leetcode id=135 lang=cpp
 *
 * [135] Candy
 */

// @lc code=start
class Solution {
public:
    int candy(vector<int> &ratings) {
        int len = ratings.size();
        vector<int> num(len, 1);

        for (int i = 0; i < len - 1; i++) {
            if (ratings[i] < ratings[i + 1]) {
                num[i + 1] = num[i] + 1;
            }
        }
        for (int i = len - 1; i > 0; i--) {
            if (ratings[i - 1] > ratings[i] & num[i - 1] <= num[i]) {
                num[i - 1] = num[i] + 1;
            }
        }
        return accumulate(num.begin(), num.end(), 0);
    }
};
// @lc code=end
