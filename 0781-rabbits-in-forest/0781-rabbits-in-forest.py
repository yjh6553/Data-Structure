class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter = Counter(answers)
        res = 0
        
        for key in counter.keys():
            group_size = key + 1
            count = counter[key]
            groups = (count + group_size - 1) // group_size  # Round up
            res += groups * group_size
        
        return res