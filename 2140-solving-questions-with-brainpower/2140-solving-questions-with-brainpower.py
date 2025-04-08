class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # n = len(questions)
        # memo = {}

        # def helper(index: int) -> None:
        #     # Base Case
        #     if index >= n:
        #         return 0
        #     if index in memo:
        #         return memo[index]
            
        #     take = questions[index][0] + helper(index + 1 + questions[index][1])
        #     skip = helper(index + 1)
        #     memo[index] = max(take, skip)
            
        #     return memo[index]

        # return helper(0)


        n = len(questions)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            points, brainpower = questions[i]
            next_q = i + 1 + brainpower

            take = points + (dp[next_q] if next_q < n else 0) 
            skip = dp[i + 1]

            dp[i] = max(take, skip)
        
        return dp[0]
