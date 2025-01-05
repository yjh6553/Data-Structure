class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        n = len(s)
        check = set()
        max_length = 0

        for r in range(len(s)):
            if s[r] not in check:
                check.add(s[r])
            else:
                while s[r] in check:
                    check.remove(s[l])
                    l += 1
                check.add(s[r])
            max_length = max(max_length, r - l + 1)

        return max_length

