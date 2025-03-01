class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = defaultdict(list)
        degree = [0] * n

        for edge in edges:
            start, end = edge[0], edge[1]
            graph[start].append(end)
            graph[end].append(start)
            degree[start] += 1
            degree[end] += 1
        
        #find a leaf node. Ex) dgree[i] == 1
        q = deque([])
        for i, num in enumerate(degree):
            if num == 1:
                q.append(i)
        
        
        while n > 2:
            size = len(q)
            n -= size
            for _ in range(size):
                node = q.popleft()
                neighbor = graph[node]
                for nei in neighbor:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        q.append(nei)
        
        return list(q)
