class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for char in s:
            if char == "(":
                stack.append(char)
            if char == ")":
                if len(stack) == 0 or stack[-1] == ")":
                    stack.append(")")
                elif stack[-1] == "(":
                    stack.pop()
                
        
        print(stack)
        return len(stack)