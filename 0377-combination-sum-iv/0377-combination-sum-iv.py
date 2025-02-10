class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
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


        # memo = {}

        # def dfs(remaining: int) -> int:
        #     if remaining == 0:
        #         return 1
        #     if remaining < 0:
        #         return 0

        #     if remaining in memo:
        #         return memo[remaining]
        #     count = 0
        #     for num in nums:
        #         count += dfs(remaining - num)

        #     memo[remaining] = count
        #     return count

        # return dfs(target)


