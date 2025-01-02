class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}
        for i in range(len(s)):
            if s[i] not in last_index:
                last_index[s[i]] = i
            last_index[s[i]] = i
        

        partition = []
        start, end = 0, 0
        for i, char in enumerate(s):
            end = max(end, last_index[char])
            if i == end:
                partition.append(end-start+1)
                start = i + 1
            
        return partition
        
        
            
            


            
            