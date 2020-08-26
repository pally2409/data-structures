class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        memo[0] = 0
        memo[1] = 1
        memo[2] = 2
        return self.helper(memo, n)
        
        
    def helper(self, memo, n):
        if n in memo.keys():
            return memo[n]
        else:
            memo[n] = self.helper(memo, n-1) + self.helper(memo, n-2)
            return memo[n]
            
