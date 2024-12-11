class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # Use Topological Sort
        indegree = [0] * n
        adj = [[] for i in range(n)]
        for start, end in edges:
            adj[start].append(end)
            indegree[end] += 1
        
        # indegree = [0, 0, 2, 1]
        # adj  = [[2], [2, 3], [], []]
        
        q = deque()
        for node in range(n):
            if indegree[node] == 0:
                q.append(node)
        
        #q = [0, 1]

        champion = -1
        count_zero_indegree = 0

        while q:
            if len(q) > 1:
                return -1
                
            curr = q.popleft()
            champion = curr
            count_zero_indegree += 1 # Pop from que where it contains zero indegree nodes

            for neighbor in adj[curr]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        return champion if count_zero_indegree == 1 else -1
