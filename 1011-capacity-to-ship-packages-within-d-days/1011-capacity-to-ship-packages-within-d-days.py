class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        # Check function
        def checkCapacity(cap: int) -> bool:
            current_total = 0
            current_day = 1

            for weight in weights:
                # If adding the current weight exceeds the capacity
                if current_total + weight > cap:
                    current_day += 1  # Move to the next day
                    current_total = 0  # Reset the total for the new day
                    if current_day > days:
                        return False  # If days exceed allowed, return False
                current_total += weight

            return True

        # Binary search for the minimum capacity
        while left < right:
            cap = (left + right) // 2  # Correct midpoint calculation
            if checkCapacity(cap):
                right = cap
            else:
                left = cap + 1

        return left






            