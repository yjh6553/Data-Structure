class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        # Case 1: Include current book into the current row
        # Case 2: Start a new row with current book
        # Condition: Width has to be within the shelfWidth
        # Result: Find the minimum height

        self.memo = [None] * len(books)
        return self.solve(books, shelfWidth, 0)
    
    def solve(self, books: List[List[int]], shelfWidth: int, ind: int) -> int:
        if ind == len(books):
            return 0
        if self.memo[ind] is not None:
            return self.memo[ind]
        
        ans = float('inf')
        maxH = 0
        width = 0
        for i in range(ind, len(books)):
            width += books[i][0]
            if width > shelfWidth:
                break
            maxH = max(maxH, books[i][1])
            ans = min(ans, maxH + self.solve(books, shelfWidth, i + 1))
        
        self.memo[ind] = ans
        return ans