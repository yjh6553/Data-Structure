class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_map = {0:1}

        for num in nums:
            prefix_sum += num

            diff = prefix_sum - k
            if diff in prefix_map:
                count += prefix_map[diff]
            
            prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1
        
        return count