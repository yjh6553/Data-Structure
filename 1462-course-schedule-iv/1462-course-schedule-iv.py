from typing import List

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Step 1: Initialize reachability matrix
        reachable = [[False] * numCourses for _ in range(numCourses)]
        
        # Step 2: Mark direct prerequisites
        for u, v in prerequisites:
            reachable[u][v] = True

        # Step 3: Apply Floyd-Warshall Algorithm
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    reachable[i][j] = reachable[i][j] or (reachable[i][k] and reachable[k][j])

        # Step 4: Answer queries based on the reachability matrix
        return [reachable[u][v] for u, v in queries]
