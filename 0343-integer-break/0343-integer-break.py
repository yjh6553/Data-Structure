class Solution:
    def integerBreak(self, n: int) -> int:
        memo = {}

        def helper(num):
            if num in memo:
                return memo[num]
            if num <= 3:
                return num

            ans = num
            for i in range(2, num):
                ans = max(ans, i * helper(num - i))
                
            memo[num] = ans
            return ans

        if n <= 3:
            return n - 1
        return helper(n)
