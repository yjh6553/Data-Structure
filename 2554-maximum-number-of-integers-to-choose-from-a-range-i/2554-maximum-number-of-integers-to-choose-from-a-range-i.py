class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        # create a banned_set
        # Loop through the range(1, n+1) and skip the banned nums
        # Check if the current sum is not bigger than maxSum.

        banned_set = set(banned)
        current_sum = 0
        count = 0

        for num in range(1, n+1):
            if num in banned_set:
                continue
            if current_sum + num <= maxSum:
                current_sum = current_sum + num
                count += 1
            elif current_sum == maxSum:
                return count
            else:
                break
        
        return count

        # Time Complexity O(n + m)
        # Space Complexity O(m)
        # n: length of the range, m: length of the banned list.