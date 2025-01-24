class Solution:
    def reverseWords(self, s: str) -> str:
        split = s.split()
        reverse = split[::-1]
        return " ".join(reverse)