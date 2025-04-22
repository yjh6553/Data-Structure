class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pointer1 = 0
        pointer2 = 0
        res = ''

        while pointer1 < len(word1) and pointer2 < len(word2):
            res += word1[pointer1]
            pointer1 += 1
            res += word2[pointer2]
            pointer2 += 1

        if pointer1 >= len(word1):
            res += word2[pointer2:]
        else:
            res += word1[pointer1:]

        return res