class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if len(coins) == 0 and amount > 0:
            return 0
        elif len(coins) == 0 and amount == 0:
            return 1
        dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins)+1)]
        dp[0][0] = 0
        for i in range(1, len(dp)):
            dp[i][0] = 1
        for i in range(1, len(dp[0])):
            dp[0][i] = 0
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                amtWithCoin = j - coins[i - 1]
                if amtWithCoin < 0:
                    dp[i][j] = dp[i-1][j] 
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][amtWithCoin]
        return dp[len(coins)][amount]
    
