class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        check = set()
        max_length = 0

        for right in range(len(s)):
            while s[right] in check:
                check.remove(s[left])
                left += 1
            check.add(s[right])
            max_length = max(max_length, right - left + 1)
        
        return max_length

        #Time Complexity: O(n)
        #Space Complexity: O(n)