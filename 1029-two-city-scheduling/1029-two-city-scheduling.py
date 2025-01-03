class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
       
        costs.sort(key=lambda x: x[0] - x[1])
        
        total_cost = 0
        n = len(costs) // 2  # Half the people (N go to City A, N go to City B)
        
        # First N people go to City A, the remaining N people go to City B
        for i in range(n):
            total_cost += costs[i][0]  # Add the cost of City A for the first N people
        for i in range(n, 2 * n):
            total_cost += costs[i][1]  # Add the cost of City B for the next N people
        
        return total_cost