class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
         # If the length of the string is odd, it's impossible to balance
        if len(s) % 2 != 0:
            return False
        
        open_stack = []  # Stack to store indices of '('
        star_stack = []  # Stack to store indices of '*'
        
        # First pass: Process the string
        for i in range(len(s)):
            if locked[i] == '1':  # Locked character
                if s[i] == '(':
                    open_stack.append(i)
                else:  # s[i] == ')'
                    if open_stack:
                        open_stack.pop()  # Match with '('
                    elif star_stack:
                        star_stack.pop()  # Match with '*'
                    else:
                        return False  # No match available
            else:  # Unlocked character ('*')
                star_stack.append(i)
        
        # Second pass: Match leftover '(' with '*'
        while open_stack:
            if not star_stack or star_stack[-1] < open_stack[-1]:
                return False  # No '*' available to balance '('
            open_stack.pop()
            star_stack.pop()
        
        return True
            
            