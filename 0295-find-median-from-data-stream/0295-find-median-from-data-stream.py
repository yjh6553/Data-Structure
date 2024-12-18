class MedianFinder:
    def __init__(self):
        # Create min with first half and max heap with other half
        self.max_heap = []  
        self.min_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)
        
        # Ensure max_heap's largest element is smaller than min_heap's smallest
        if self.max_heap and self.min_heap and (-self.max_heap[0] > self.min_heap[0]):
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        
        # Balance the heaps
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
    
    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            # If even, average of two middle values
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        else:
            # If odd, max heap root is the median
            return -self.max_heap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()