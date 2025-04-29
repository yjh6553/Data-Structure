class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cur_max = max(nums)
        res = 0
        cur_k = 0
        right = 0

        for left in range(n):
            # Move right pointer forward if needed
            while right < n and cur_k < k:
                if nums[right] == cur_max:
                    cur_k += 1
                right += 1

            # If we found enough maximums, count subarrays
            if cur_k >= k:
                res += n - right + 1

            # Before moving left to left + 1, update cur_k
            if nums[left] == cur_max:
                cur_k -= 1

        return res