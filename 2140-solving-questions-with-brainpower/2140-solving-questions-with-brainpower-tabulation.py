class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1) # Add one more index because there is an edge case

        for i in range(n - 1, -1, -1):
            points, brainpower = questions[i]
            next_q = i + 1 + brainpower

            take = points + (dp[next_q] if next_q < n else 0)
            skip = dp[i + 1]
            dp[i] = max(take, skip)
        
        return dp[0]

