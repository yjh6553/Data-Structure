class Solution:
    def totalNQueens(self, n: int) -> int:
        # Tracking occupied columns and diagonals
        cols = set()
        diag1 = set()  # (row + col) → Main diagonal
        diag2 = set()  # (row - col) → Anti-diagonal
        count = 0  # Number of valid solutions
        
        def backtrack(row):
            nonlocal count
            if row == n:  # If all n queens are placed successfully
                count += 1
                return
            
            for col in range(n):  # Try placing a queen in each column
                if col in cols or (row + col) in diag1 or (row - col) in diag2:
                    continue  # Skip invalid positions
                
                # Place the queen
                cols.add(col)
                diag1.add(row + col)
                diag2.add(row - col)
                
                backtrack(row + 1)  # Move to the next row
                
                # Backtrack (remove the queen)
                cols.remove(col)
                diag1.remove(row + col)
                diag2.remove(row - col)
        
        backtrack(0)  # Start placing queens from row 0
        return count  # Return the number of valid solutions

