class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)
        max_heap = []
        res = []
        for key in counts.keys():
            max_heap.append((-counts[key], key))
        heapq.heapify(max_heap)
        for _ in range(k):
            res.append(heapq.heappop(max_heap)[1])

        return res