class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # First pass: Identify invalid closing parentheses
        stack = []
        to_remove = set()

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()  # Matched parenthesis
                else:
                    to_remove.add(i)  # Unmatched closing parenthesis

        # Add any unmatched opening parentheses to the removal set
        to_remove.update(stack)

        # Second pass: Build the result string
        result = []
        for i, char in enumerate(s):
            if i not in to_remove:
                result.append(char)

        return ''.join(result)