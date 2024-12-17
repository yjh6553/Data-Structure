class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        marked = [False] * n  # Track marked elements
        min_heap = []  # Min-heap to prioritize smallest elements
        score = 0

        # Build the heap with (value, index) pairs
        for i, num in enumerate(nums):
            heapq.heappush(min_heap, (num, i))

        # Process the heap
        while min_heap:
            value, index = heapq.heappop(min_heap)
            
            # Skip if already marked
            if marked[index]:
                continue
            
            # Update score
            score += value
            
            # Mark current element and its neighbors
            marked[index] = True
            if index > 0:
                marked[index - 1] = True
            if index < n - 1:
                marked[index + 1] = True

        return score

    # Time: n log n
    # Space: O(n)