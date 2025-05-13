class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        path = set()  # Use set to avoid duplicates

        def backtrack(used, length, cur):
            # If we have a valid 3-digit even number
            if length == 3:
                if cur % 2 == 0:
                    path.add(cur)  # Add to the set to avoid duplicates
                return
            
            # Try all possible digits
            for i in range(len(digits)):
                # Skip if digit is already used or leading zero for the first digit
                if used[i] or (length == 0 and digits[i] == 0):
                    continue
                
                # Mark this digit as used and build the number
                used[i] = True
                # Append the current digit and continue building the number
                backtrack(used, length + 1, cur * 10 + digits[i])
                # Backtrack: unmark the digit
                used[i] = False

        # Initialize the backtracking with no digits used
        backtrack([False] * len(digits), 0, 0)

        # Convert set to sorted list for the final output
        result = sorted(path)
        return result
