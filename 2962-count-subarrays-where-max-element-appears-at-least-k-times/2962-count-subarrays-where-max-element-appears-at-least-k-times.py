class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cur_k = 0
        cur_max = max(nums)
        res = 0
        left = 0

        for right in range(n):
            if nums[right] == cur_max:
                cur_k += 1

            while cur_k >= k:
                res += n - right  # all subarrays [left..n-1] ending after right are valid
                if nums[left] == cur_max:
                    cur_k -= 1
                left += 1
        
        return res