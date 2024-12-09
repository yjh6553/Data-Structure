class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()  # Sort the potions array
        result = []

        for spell in spells:
            # Calculate the minimum required potion strength
            min_required = math.ceil(success / spell)
            # Use custom binary search to find the position
            index = self.binary_search_first_gte(potions, min_required)
            # Calculate the count of successful pairs
            result.append(len(potions) - index)
        
        return result
    
    def binary_search_first_gte(self, arr, target):
        """
        Custom binary search to find the first index where arr[index] >= target.
        """
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left