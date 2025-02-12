class Solution:
    def numSquares(self, n: int) -> int:
        # Generate all perfect squares less than or equal to n
        perfect_squares = []
        count = 1
        while count ** 2 <= n:
            perfect_squares.append(count ** 2)
            count += 1

        # Memoization dictionary
        memo = {}

        # Recursive function with memoization
        def helper(target: int) -> int:
            # Base case
            if target == 0:
                return 0
            if target in memo:
                return memo[target]

            # Recursive case: Try subtracting each perfect square
            min_count = float('inf')
            for square in perfect_squares:
                if target < square:
                    break
                min_count = min(min_count, 1 + helper(target - square))

            # Save the result in memo
            memo[target] = min_count
            return min_count

        return helper(n)