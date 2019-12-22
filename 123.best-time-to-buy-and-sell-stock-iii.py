#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp[k][i] = max(dp[k][i-1], prices[i]- prices[j]+dp[k-1][j]),j = 0~i-1
        # min(prices[j]-dp[k-1][j-1])
        # if not prices:
        #     return 0
        # n = len(prices)
        # dp = [[0] * n for _ in range(3)]
        # for k in [1, 2]:
        #     maxDiff = -prices[0]
        #     for i in range(1, n):
        #         # maxV = 0
        #         # for j in range(i):
        #         #     maxV = max(maxV, prices[i] - prices[j] + dp[k - 1][j])
        #         dp[k][i] = max(dp[k][i - 1], prices[i] + maxDiff)
        #         maxDiff = max(maxDiff, dp[k - 1][i] - prices[i])
        # return dp[-1][-1]
        if not prices:
            return 0
        n = len(prices)
        dp = [[0] * n for _ in range(3)]
        for k in [1,2]:
            maxDiff = -prices[0]
            for i in range(1,n):
                dp[k][i] = max(dp[k][i-1], prices[i]+maxDiff)
                maxDiff = max(maxDiff, dp[k-1][i]-prices[i])
        
        return dp[-1][-1]
        


# @lc code=end

