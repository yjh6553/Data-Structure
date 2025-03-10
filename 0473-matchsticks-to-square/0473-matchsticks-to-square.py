class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4 != 0:
            return False
        
        edge_length = sum(matchsticks) // 4  # Integer division
        matchsticks.sort(reverse=True)  # Sorting in descending order to optimize
        
        sides = [0] * 4  # To store lengths of four sides
        
        def backtrack(index):
            if index == len(matchsticks):
                return all(side == edge_length for side in sides)
            
            for i in range(4):
                if sides[i] + matchsticks[index] <= edge_length:
                    sides[i] += matchsticks[index]
                    if backtrack(index + 1):
                        return True
                    sides[i] -= matchsticks[index]  # Backtrack
                
                if sides[i] == 0:
                    break  # Optimization: Avoid trying the same empty side multiple times
            
            return False
        
        return backtrack(0)
        