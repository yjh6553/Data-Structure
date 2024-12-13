class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        count = 0
        repeated_word = word

        # Incrementally check for the repeated word
        while repeated_word in sequence:
            count += 1
            repeated_word += word  # Add another repetition of word

        return count