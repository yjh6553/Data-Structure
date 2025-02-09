class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        key : ord(str)  Value: List()
        """

        res = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord("a")] += 1 

            count = tuple(count)

            if count in res:
                res[count].append(word)
            else:
                res[count] = [word]

        return list(res.values())

        