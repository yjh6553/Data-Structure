class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if any(num < k for num in nums):
            return -1

        # Count unique values greater than k
        unique_greater = set(num for num in nums if num > k)
        return len(unique_greater)