class Solution:
    def calculate(self, s: str) -> int:
        # Helper function to perform operations
        def operate(a, b, op):
            if op == "*":
                return a * b
            elif op == "/":
                return a // b

        # Clean the input and parse numbers and operators
        s = s.replace(" ", "")
        num_stack = []
        op_stack = []
        i = 0
        n = len(s)

        while i < n:
            if s[i].isdigit():
                # Handle multi-digit numbers
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                num_stack.append(num)
                continue
            elif s[i] in "*/":
                # Handle multiplication and division immediately
                op = s[i]
                i += 1
                while i < n and s[i] == " ":
                    i += 1
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                # Pop the last number and calculate
                prev_num = num_stack.pop()
                num_stack.append(operate(prev_num, num, op))
                continue
            else:
                # Handle addition and subtraction later
                op_stack.append(s[i])
            i += 1

        # Handle addition and subtraction
        result = num_stack[0]
        j = 1
        for op in op_stack:
            if op == "+":
                result += num_stack[j]
            elif op == "-":
                result -= num_stack[j]
            j += 1

        return result