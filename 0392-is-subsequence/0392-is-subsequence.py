class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        def helper(s_index: int, t_index: int) -> bool:
            # Base cases
            if s_index == len(s):  # All characters in s matched
                return True
            if t_index == len(t):  # t is exhausted
                return False
            
            if s[s_index] == t[t_index]:
                return helper(s_index + 1, t_index + 1)  
            else:
                return helper(s_index, t_index + 1)  
        
        return helper(0, 0)