class Solution:
    def minInsertions(self, s: str) -> int:
        stack = 0
        res = 0
        i = 0

        while i < len(s):
            if s[i] == "(":
                stack += 1
                i += 1
            else:
                if i + 1 < len(s) and s[i+1] == ")": # Current char is ")" and next is ")"
                    if stack > 0:  # Use one "(" from stack
                        stack -= 1
                    else: # Consider we added "("
                        res += 1
                    i += 2 
                else: # current char is ")" but next char is not ")" or there is no more next char.
                    res += 1 # Insert ")"
                    if stack > 0: #There is "(" not being used
                        stack -= 1
                    else: # There is no more "(" to use.
                        res += 1
                    i += 1
        
        #Remain with unmatched "("s
        res += stack * 2
        return res

    # Time Complexity: O(n)
    # Space Complexity: O(n)
        