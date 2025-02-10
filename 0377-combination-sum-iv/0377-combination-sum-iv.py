class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Top down: Target-------------
        memo = {}
        def dfs(cur: int) -> int:
            if cur == target:
                return 1
            if cur > target:
                return 0

            if cur in memo:
                return memo[cur]

            count = 0
            for num in nums:
                count += dfs(cur + num)  # Recursively explore with updated cur
            memo[cur] = count

            return count

        return dfs(0)

        # Tabulation, Target 1, target 2

        dp = [0] * (target + 1) # Index: subproblem target, value: number of cases that sums up to index.
        dp[0] = 1  # Base case: One way to make sum 0 (do nothing)

        for t in range(1, target + 1):  # Compute solutions for each sum up to target
            for num in nums:
                if t >= num:  # Ensure we don't go out of bounds
                    dp[t] += dp[t - num]  # Add ways from smaller sums

        return dp[target]  # Final answer is stored in dp[target]




