#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(len(dp)):
            for c in coins:
                if i - c < 0:
                    continue
                dp[i] = min(dp[i], 1 + dp[i - c])
        return -1 if dp[amount] == amount + 1 else dp[amount]


# @lc code=end

