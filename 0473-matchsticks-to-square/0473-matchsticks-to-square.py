class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4 != 0:
            return False
        
        edge_length = sum(matchsticks) // 4  # Integer division
        matchsticks.sort(reverse=True)  # Sorting in descending order to optimize
        
        sides = [0] * 4  # To store lengths of four sides
        

        # [3, 3, 2, 1, 1, 1, 1, 1, 1, 1]
        # edge_length = 4
        # [4 4 4 4]
        # index = 4
        # cur_lenght = 0
        # 
        def backtrack(index) -> bool:
            if index == len(matchsticks):
                return all(side == edge_length for side in sides)
            
            for i in range(4): # i = 1
                if sides[i] + matchsticks[index] <= edge_length: # 4 + 1 <= 4
                    sides[i] += matchsticks[index] 
                    if backtrack(index + 1): #backtrack(10)
                        return True
                    sides[i] -= matchsticks[index] #sides[0] -= math  
                
                # if sides[i] == 0:  #side[0] = 3
                #     break  # Optimization: Avoid trying the same empty side multiple times
            
            return False
        
        return backtrack(0)
        