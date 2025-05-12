class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        unique_numbers = set()
        n = len(digits)

        # Manually generate permutations of length 3
        for i in range(n):
            # Skip leading zero for the first digit
            if digits[i] == 0:
                continue
            for j in range(n):
                if j == i:
                    continue
                for k in range(n):
                    if k == i or k == j:
                        continue
                    # Check if the last digit is even
                    if digits[k] % 2 == 0:
                        number = digits[i] * 100 + digits[j] * 10 + digits[k]
                        unique_numbers.add(number)

        # Convert to sorted list
        result = sorted(unique_numbers)
        return result

