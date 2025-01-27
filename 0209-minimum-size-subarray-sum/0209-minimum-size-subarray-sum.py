class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        min_len = float('inf')
        cur_sum = 0

        for right in range(len(nums)):
            cur_sum += nums[right]

            while cur_sum >= target:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                cur_sum -= nums[left]
                left += 1
        
        return min_len if min_len != float('inf') else 0

        # Time Complexity: O(n)
        # Space Complexity: O(1)
        