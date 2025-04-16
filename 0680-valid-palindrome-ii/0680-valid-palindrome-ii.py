class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                # Skip either left or right and check inline
                l1, r1 = left + 1, right
                valid1 = True
                while l1 < r1:
                    if s[l1] != s[r1]:
                        valid1 = False
                        break
                    l1 += 1
                    r1 -= 1

                l2, r2 = left, right - 1
                valid2 = True
                while l2 < r2:
                    if s[l2] != s[r2]:
                        valid2 = False
                        break
                    l2 += 1
                    r2 -= 1

                return valid1 or valid2
        return True
