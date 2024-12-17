class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
         gifts=[-x for x in gifts]
        heapify(gifts)
        x, i=1<<32, 0
        while i<k and x>1:
            x=-heappop(gifts)
            heappush(gifts, -isqrt(x))
            i+=1
        return -sum(gifts)

        
        # # Use a max-heap by inserting negative values
        # max_heap = [-gift for gift in gifts]
        # heapq.heapify(max_heap)
        
        # # Perform k operations
        # for _ in range(k):
        #     # Extract the largest value (remember it's negative)
        #     max_gift = -heapq.heappop(max_heap)
        #     # Replace with the square root (integer part)
        #     new_gift = math.isqrt(max_gift)
        #     # Push the new value back (as negative for max-heap)
        #     heapq.heappush(max_heap, -new_gift)
        
        # # Calculate the total sum of remaining gifts
        # return -sum(max_heap)