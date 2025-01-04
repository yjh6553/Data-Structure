class MyString:
    def __init__(self, word):
        self.word = word

    def __lt__(self, other):
        return self.word > other.word

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Count word frequencies
        count = Counter(words)

        # Use a min-heap to keep the top k elements
        min_heap = []
        for word, freq in count.items():
            # Push into the heap with frequency to simulate max-heap
            heapq.heappush(min_heap, (freq, MyString(word)))
            # Maintain the heap size to k
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # Extract elements from the heap and sort them
        result = []
        while min_heap:
            result.append(heapq.heappop(min_heap)[1].word)  # Append words only

        # The result should be reversed since heap order is smallest first
        return result[::-1]
