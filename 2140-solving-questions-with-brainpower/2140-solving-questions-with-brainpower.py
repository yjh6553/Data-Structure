class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        memo = {}
        def helper(index: int):
            if index >= n:
                return 0
            if index in memo:
                return memo[index]
            
            include = questions[index][0] + helper(index + questions[index][1] + 1) 
            exclude = helper(index + 1) 
            memo[index] = max(include, exclude)
            
            return memo[index]

        return helper(0)