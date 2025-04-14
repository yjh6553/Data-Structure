class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        path = [0]*1000
        
        for num, a, b in trips:
            for loc in range (a, b):
                path[loc] += num
                if path[loc] > capacity: return False
                
        return True

        