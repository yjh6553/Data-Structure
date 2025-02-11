class Solution:
    def integerBreak(self, n: int) -> int:
        memo = {}

        def dp(num):
            if num in memo:
                return memo[num]
            if num == 2:
                return 1  # The only valid way to split 2 is 1+1
            
            ans = 0  # Start with 0 since we want the maximum product
            for i in range(1, num):  # Split `num` into `i` and `num - i`
                ans = max(ans, i * (num - i), i * dp(num - i))  # Maximize the product
            
            memo[num] = ans  # Store computed result
            return ans

        if n <= 3:
            return n - 1  # Special case: integer break requires at least one split
        
        return dp(n)
