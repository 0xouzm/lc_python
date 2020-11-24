/*
 * @lc app=leetcode id=122 lang=cpp
 *
 * [122] Best Time to Buy and Sell Stock II
 */

// @lc code=start
class Solution {
public:
    int maxProfit(vector<int> &prices) {
        int profit = 0;
        int len = prices.size();
        for (int i = 0; i < len - 1; i++) {
            profit += max(prices[i + 1] - prices[i], 0);
        }
        return profit;
    }
};
// @lc code=end

