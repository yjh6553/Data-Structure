class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        """
        [1 2 3 5 10 1]
        [0 1 1 3 3  4]


        heeap_1 = [2, 3] -> [3, 2] -> pop = 3
        heap_3 = [5 10] -> [10, 5] 
        
        k = 2 - 1 = 1
        w = 3 
        0 + 3 + 10

        """
        n = len(profits)
        project_cost = sorted((capital[i], profits[i]) for i in range(n))  # Sort by capital

        max_heap = []
        heapq.heapify(max_heap)

        index = 0  # Track the position in project_cost

        while k > 0:
            while index < n and project_cost[index][0] <= w:
                heapq.heappush(max_heap, -project_cost[index][1])  # Push profit as negative (max-heap)
                index += 1

            if not max_heap:
                break  # If no projects can be done, exit early

            w += -heapq.heappop(max_heap)  # Take the most profitable project
            k -= 1

        return w

            
                

            

