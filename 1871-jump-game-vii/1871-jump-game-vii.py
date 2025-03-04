class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[-1] == '1': 
            return False  # If the last position is blocked, return False
        
        dp = [False] * n
        dp[0] = True  # We start at position 0
        reach_count = 0  # Tracks the number of reachable positions in the range [i - maxJump, i - minJump]

        for i in range(1, n):
            if i >= minJump:
                reach_count += dp[i - minJump]  # Add start of valid jump range
            if i > maxJump:
                reach_count -= dp[i - maxJump - 1]  # Remove the end of valid jump range
            
            # A position is reachable if there exists at least one reachable position in the valid jump range
            if s[i] == '0' and reach_count > 0:
                dp[i] = True

        return dp[-1]  # Return whether we can reach the last position