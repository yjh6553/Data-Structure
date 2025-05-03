class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        tops_counts = Counter(tops)
        bottom_counts = Counter(bottoms)
        n = len(tops)
        candidates = []
        res = float('inf')
    
        for num in range(1, 7):
            top_value = 0
            bottom_value = 0
            if num in tops_counts:
                top_value = tops_counts[num]
            if num in bottom_counts:
                bottom_value = bottom_counts[num]
            
            if top_value + bottom_value >= n:
                candidates.append(num)
        
        if not candidates:
            return -1
        
        for candidate in candidates:
            print(f'Current candidate: {candidate}')
            cur_res = 0
            moveToTop = True
            if tops_counts[candidate] <= bottom_counts[candidate]:
                moveToTop = False

            for index in range(n):
                if tops[index] != candidate and bottoms[index] != candidate:
                    return -1
                elif moveToTop and tops[index] != candidate and bottoms[index] == candidate:
                    print(f'Candidate moves to top at index {index}')
                    cur_res += 1
                elif not moveToTop and tops[index] == candidate and bottoms[index] != candidate:
                    print(f'Candidate moves to bottom at index {index}')
                    cur_res += 1
            
            res = min(res, cur_res)
        
        return res

