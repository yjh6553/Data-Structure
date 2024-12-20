class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        num_count = {}
        count = 0
        
        for num in nums:
            complement = k - num
            # Check if the complement exists in the map
            if complement in num_count and num_count[complement] > 0:
                count += 1  # Pair found
                num_count[complement] -= 1  # Use up one complement
            else:
                # Add current number to the map
                if num in num_count:
                    num_count[num] += 1
                else:
                    num_count[num] = 1
        
        return count