# class Solution:
#     def numSquares(self, n: int) -> int:
#         # perfect squares: 1*1, 2*2, 3*3, 4*4, 5*5
#         # find the largest perfect square that is less than n

#         # Match with other perfect sqaures that is less than the largest perfect squares number that we find.

#         #find the availabe numbers to find n
#         count = 1
#         availableNums = []
#         while count**2 < n:
#             availableNums.append(count)
#             count += 1
       
#         #[1, 4, 9]
#         #Find a combination
#         def findCombinations(nums: list, target: int, current: int) -> int:
#             if current == target:
#                 return 0
#             if current > target:
#                 return float('inf')
#             exclude = 1 + findCombinations(nums[1:], target, current + nums[1:][0]) #[4, 9]
#             include = 1 + findCombinations(nums, target, current + nums[0]) 
#             result = min(include, exclude)
#             return result

#         return findCombinations(availableNums, n, 0)


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