class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        left = 0
        right = left + minutes - 1 
        satisfied = 0
        current_satisfied = 0

        # Add always satisfied customers (where grumpy is 0)
        satisfied = sum(customers[i] for i in range(len(customers)) if grumpy[i] == 0)

        # In the window only counts the grumpy people to avoid double counts.
        for i in range(left, right + 1):
            if grumpy[i] == 1:
                current_satisfied += customers[i]

        max_additional_satisfied = current_satisfied

        # Slide the window across the array, only counts the customers when owner is grumpy.
        while right < len(customers) - 1:
            # Move the window forward
            left += 1
            right += 1

            # Add the new element to the window if the owner is grumpy
            if grumpy[right] == 1:
                current_satisfied += customers[right]
            # Remove the element that is sliding out of the window if the owner was grumpy
            if grumpy[left - 1] == 1:
                current_satisfied -= customers[left - 1]

            # Update the max additional satisfied
            max_additional_satisfied = max(max_additional_satisfied, current_satisfied)

        return satisfied + max_additional_satisfied
        
        # Time O(n)
        # Space O(1)