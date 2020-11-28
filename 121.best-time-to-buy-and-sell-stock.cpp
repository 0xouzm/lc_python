/*
 * @lc app=leetcode id=121 lang=cpp
 *
 * [121] Best Time to Buy and Sell Stock
 */

// @lc code=start
class Solution {
public:
    int maxProfit(vector<int> &prices) {
        if (prices.empty())
            return 0;
        int profit = 0;
        int minV = prices[0];
        for (int i = 0; i < prices.size(); i++) {
            minV = min(prices[i], minV);
            profit = max(profit, prices[i] - minV);
        }
        return profit;
    }
};
// @lc code=end
