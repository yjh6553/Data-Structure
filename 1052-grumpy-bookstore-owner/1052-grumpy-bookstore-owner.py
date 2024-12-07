class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        left = 0
        right = left + minutes - 1  # Ensure the window size is exactly `minutes`
        satisfied = 0
        current_satisfied = 0

        # Initial calculation for the first window
        for i in range(left, right + 1):
            current_satisfied += customers[i] if grumpy[i] == 1 else 0

        # Add always satisfied customers (where grumpy is 0)
        satisfied = sum(customers[i] for i in range(len(customers)) if grumpy[i] == 0)

        max_additional_satisfied = current_satisfied

        # Slide the window across the array
        while right < len(customers) - 1:
            # Move the window forward
            left += 1
            right += 1

            # Add the new element to the window
            if grumpy[right] == 1:
                current_satisfied += customers[right]
            # Remove the element that is sliding out of the window
            if grumpy[left - 1] == 1:
                current_satisfied -= customers[left - 1]

            # Update the max additional satisfied
            max_additional_satisfied = max(max_additional_satisfied, current_satisfied)

        return satisfied + max_additional_satisfied
        