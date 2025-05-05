class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        
        count = defaultdict(int)
        res = 0

        for domino in dominoes:
            key = (min(domino[0], domino[1]), max(domino[0], domino[1]))
            if key in count:
                res += count[key]
                count[key] += 1
            else:
                count[key] = 1
        
        return res
            