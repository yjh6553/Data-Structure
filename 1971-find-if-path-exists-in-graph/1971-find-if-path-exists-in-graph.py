class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        #DFS?
        #Create adjacency list
        adj = [[] * i for i in range(n)]
        for start, end in edges:
            adj[start].append(end)
            adj[end].append(start)

        
        stack = [source]
        visited = set()

        # Conduct DFS
        while stack:
            node = stack.pop()
            
            if node == destination:
                return True
            
            if node not in visited:
                visited.add(node)

                for nei in adj[node]:
                    if nei not in visited:
                        stack.append(nei)


        return False