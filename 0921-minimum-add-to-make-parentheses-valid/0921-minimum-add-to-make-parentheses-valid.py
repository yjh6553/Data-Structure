class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opened = 0
        closed = 0
        for char in s:
            if char == "(":
                opened += 1
            if char == ")":
                if opened:
                    opened -= 1
                else:
                    closed += 1
        
        res = opened + closed
        return res