class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # Safte State means a node that has no out going edges.
        #

        # Find terminal nodes
        n = len(graph)
        
        # Reverse the graph
        reversed_graph = [[] for _ in range(n)]
        indegree = [0]*n #indegree in reversed_graph
        for start in range(n):
            for end in graph[start]:
                reversed_graph[end].append(start)
                indegree[start] += 1

        print(reversed_graph)
        print(indegree)

        # Start with nodes that have no outgoing edges (indegree 0 in reversed graph)
        q = deque()
        for node in range(n):
            if indegree[node] == 0:
                q.append(node)

        # Find all safe nodes
        safe_nodes = []
        while q:
            node = q.popleft()
            safe_nodes.append(node)
            for nei in reversed_graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        # Return safe nodes sorted
        return sorted(safe_nodes)

                

