class Solution:
    def climbStairs(self, n: int) -> int:
        # if n == 1:
        #     return 1

        # dp = [0] * (n + 1)
        # dp[1], dp[2] = 1, 2  # Base cases

        # for i in range(3, n + 1):
        #     dp[i] = dp[i - 1] + dp[i - 2]  # Transition formula

        # return dp[n]

        # memo = {}
        # def helper(cur: int) ->int:
        #     if cur == n:
        #         return 1
        #     if cur > n:
        #         return 0
            
        #     memo[cur] = helper(cur + 1) + helper(cur + 2)
        #     return memo[cur]

        # return helper(0)

        # Tabulation
        if n == 1:
            return 1

        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n + 1):
            dp[i] = dp[i-2] + dp[i-1]
        
        return dp[n]