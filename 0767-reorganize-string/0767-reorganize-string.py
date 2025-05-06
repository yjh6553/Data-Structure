class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        max_heap = []
        for char, freq in count.items():
            max_heap.append((-freq, char))
        heapq.heapify(max_heap)

        res = ""

        while max_heap:
            freq, char = heapq.heappop(max_heap)
            if len(res) == 0 or res[-1] != char:
                res += char
                if freq + 1 != 0:
                    heapq.heappush(max_heap, (freq + 1, char))
            elif res[-1] == char and max_heap:
                second = heapq.heappop(max_heap)
                res += second[1] 
                if second[0] + 1 != 0:
                    heapq.heappush(max_heap, (second[0] + 1, second[1]))
                heapq.heappush(max_heap, (freq, char))
            else:
                return ""
        
        return res