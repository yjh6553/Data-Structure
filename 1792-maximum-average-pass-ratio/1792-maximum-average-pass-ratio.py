class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # Calculate the marginal gain for each class and create a max heap
        def gain(passes, total):
            return (passes + 1) / (total + 1) - passes / total

        # Max heap (negative of gain to simulate max heap using heapq)
        max_heap = []
        for passes, total in classes:
            heapq.heappush(max_heap, (-gain(passes, total), passes, total))

        # Distribute the extra students
        for _ in range(extraStudents):
            g, passes, total = heapq.heappop(max_heap)
            passes += 1
            total += 1
            heapq.heappush(max_heap, (-gain(passes, total), passes, total))

        # Calculate the final average pass ratio
        total_ratio = 0
        for _, passes, total in max_heap:
            total_ratio += passes / total

        return total_ratio / len(classes)
