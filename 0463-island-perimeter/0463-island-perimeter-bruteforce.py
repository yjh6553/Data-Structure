class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # put duplicate line into set
        rows = len(grid)
        cols = len(grid[0])
        res = 0 

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res += 4
                    if r > 0 and grid[r -1][c] == 1:
                        res -= 2
                    if c > 0 and grid[r][c-1] == 1:
                        res -= 2
        
        return res

            
        

            
