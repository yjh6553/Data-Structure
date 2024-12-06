class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        # Create a set for faster lookup of banned numbers
        banned_set = set(banned)
        
        current_sum = 0
        count = 0
        
        # Iterate through the range [1, n]
        for num in range(1, n + 1):
            if num not in banned_set and current_sum + num <= maxSum:
                current_sum += num
                count += 1
        
        return count
        

        # #sliding Window
        # left, right = 0, 1

        # available = [i for i in range(1, n+1)]
        # current_Max = 0
        # current_Sum = 0

        # while left < right:
        #     window = available[left:right+1]
        #     for num in window:
        #         if num in banned:
        #             window.remove(num)
        #     if sum(window) < maxSum:
        #         right += 1

        