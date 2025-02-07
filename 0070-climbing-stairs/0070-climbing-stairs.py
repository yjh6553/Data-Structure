class Solution:
    def climbStairs(self, n: int) -> int:
        # def helper(steps_remaining: int) -> int:
        #     if steps_remaining == 0:
        #         return 1
        #     if steps_remaining < 0:
        #         return 0
            
        #     return helper(steps_remaining - 1) + helper(steps_remaining - 2)

        # return helper(n)

        if n == 1:
            return 1

        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2  # Base cases

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]  # Transition formula

        return dp[n]