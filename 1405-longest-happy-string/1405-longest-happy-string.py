class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # Create a max_heap : (count, char)
        count = [(-a, "a"), (-b, "b"), (-c, "c")]
        max_heap = []
        for ele in count:
            if ele[0] == 0:
                continue
            else:
                max_heap.append(ele)
        heapq.heapify(max_heap)

        res = ""

        while max_heap:
            print(f"Before: {max_heap}")
            first_count, first_char = heapq.heappop(max_heap)

            # Last two char is the same as the char that we want to add
            if len(res) >= 2 and res[-1] == first_char and res[-2] == first_char:
                # There is no more element left in heap
                if not max_heap:
                    return res
                
                # Get the second most frequent char
                second_count, second_char = heapq.heappop(max_heap)
                res = res + second_char
                second_count += 1

                # Check if first and second char has more nums to add to res.
                if first_count < 0: 
                    heapq.heappush(max_heap, (first_count, first_char))
                if second_count < 0:
                    heapq.heappush(max_heap, (second_count, second_char))
                
            
            else: # Last two chars are not the same as cur char.
                res = res + first_char
                first_count += 1
                if first_count < 0:
                    heapq.heappush(max_heap, (first_count, first_char))

        return res