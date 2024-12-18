class MedianFinder:
    def __init__(self):
        # Create min with first half and max heap with other half
        self.max_heap = []  
        self.min_heap = []

    def addNum(self, num: int) -> None:
        heappush(self.max_heap, -num)
        heappush(self.min_heap, -heappop(self.max_heap))
        if len(self.min_heap) > len(self.max_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    
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