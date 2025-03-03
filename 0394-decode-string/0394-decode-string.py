class Solution:
    def decodeString(self, s: str) -> str:
        op_stack = []
        num = ''
        i = 0
        n = len(s)
        rest = ''

        while i < n:
            # Check number in front of open bracket
            if s[i].isdigit():
                num += s[i]
                while i + 1 < n and s[i + 1].isdigit():  # Ensure within bounds
                    num += s[i + 1]
                    i += 1
                op_stack.append(int(num))  # Convert to integer
                num = ''  # Reset num after pushing to stack

            elif s[i] == "[":
                op_stack.append(rest)  # Store any accumulated characters
                rest = ''  # Reset rest
            elif s[i] == "]":  # Fixed missing colon
                prev_str = op_stack.pop()
                count = op_stack.pop()
                rest = prev_str + rest * count  # Expand the encoded part
            else:
                rest += s[i]
            
            i += 1  # Ensure loop progresses
        
        return "".join(op_stack) + rest  # Construct final result

        

