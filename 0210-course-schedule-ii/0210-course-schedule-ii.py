class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Topological Sort (Kahn’s Algorithm using Min Heap)
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        # Build adjacency list & compute indegree
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        
        # Min-Heap to store courses with 0 prerequisites
        min_heap = [i for i in range(numCourses) if indegree[i] == 0]
        heapq.heapify(min_heap)

        print(graph)
        print(indegree)
        print(min_heap)

        res = []

        while min_heap:
            node = heapq.heappop(min_heap)
            res.append(node)

            # Reduce the indegree of adjacent courses
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    heapq.heappush(min_heap, neighbor)

        # If all courses are not taken, there must be a cycle (return empty list)
        return res if len(res) == numCourses else []



