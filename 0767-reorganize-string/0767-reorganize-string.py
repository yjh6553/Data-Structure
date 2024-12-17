from collections import defaultdict
class Solution:
    def reorganizeString(self, s: str) -> str:
        freqDic = {}
        for char in s:
            freqDic[char] = freqDic.get(char, 0) + 1
        
        #create max_heap
        max_heap = [(-freq, char) for char, freq in freqDic.items()] # -freq because python does not have maxHeap
        heapq.heapify(max_heap)

        res = ""

        while len(max_heap) >=2:
            freq1, char1 = heapq.heappop(max_heap)
            freq2, char2 = heapq.heappop(max_heap)

            res += char1
            res += char2

            if freq1 + 1 < 0:
                heapq.heappush(max_heap, (freq1 + 1, char1))
            if freq2 + 1 < 0:
                heapq.heappush(max_heap, (freq2 + 1, char2))
        
        if max_heap:
            freq, char = heapq.heappop(max_heap)
            if -freq > 1:
                return ""
            res += char

        return res




        

                