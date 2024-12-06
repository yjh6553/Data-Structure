class Solution:
    def calculate(self, s: str) -> int:
        # Initialize variables
        stack = []
        num = 0
        sign = '+'  # Start with a '+' sign by default
        
        # Iterate through the string
        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)  # Handle multi-digit numbers
            
            # If the character is an operator or we're at the end of the string
            if char in "+-*/" or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    stack.append(int(stack.pop() / num))  # Truncate towards zero
                # Update the sign and reset the number
                sign = char
                num = 0
        
        # Return the sum of the stack
        return sum(stack)

#time: O(n)
#space: O(n)