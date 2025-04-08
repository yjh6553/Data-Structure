class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        memo = {}

        def helper(index: int) -> None:
            # Base Case
            if index >= n:
                return 0
            if index in memo:
                return memo[index]
            
            take = questions[index][0] + helper(index + 1 + questions[index][1])
            skip = helper(index + 1)
            memo[index] = max(take, skip)
            
            return memo[index]

        return helper(0)