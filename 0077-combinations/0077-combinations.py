class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
    
        def backtrack(start, path):
            # Base case: if the combination is of length k, add to results
            if len(path) == k:
                result.append(path[:])  # Make a copy to store the valid combination
                return
            
            # Iterate from `start` to `n`
            for i in range(start, n + 1):
                path.append(i)  # Choose
                backtrack(i + 1, path)  # Explore
                path.pop()  # Unchoose (backtrack)

        backtrack(1, [])
        return result