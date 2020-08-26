class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float(inf)]*(amount+1)
        dp[0] = 0
        for i in range(1, len(dp)):
            for j in range(len(coins)):
                if i - coins[j] >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - coins[j]])
        if dp[amount] == float(inf):
            return -1
        else:
            return dp[amount]
        
