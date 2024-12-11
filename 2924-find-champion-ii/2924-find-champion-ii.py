class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # Use Topological Sort
        indegree = [0] * n

        for start, end in edges:
            indegree[end] += 1
        
        champion = -1
        champion_count = 0

        for team in range(n):
            if indegree[team] == 0:
                champion = team
                champion_count += 1
        
        if champion_count == 1:
            return champion
        
        return -1