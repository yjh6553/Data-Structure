class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words) 
        """
        {i : 2, 
        love : 2, 
        leetcode: 1, 
        coding : 1}

        """
        min_heap = []
        res = []

        for key in counts.keys():
            heapq.heappush(min_heap, (-counts[key], key))
            # min_heap.heappop()

        for _ in range(k):
            res.append(heapq.heappop(min_heap)[1])

        return res