class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        rowZero, colZero = False, False

        # Step 1: Determine if the first row or first column needs to be zero
        for r in range(rows):
            if matrix[r][0] == 0:
                colZero = True
                break
        
        for c in range(cols):
            if matrix[0][c] == 0:
                rowZero = True
                break
        
        # Step 2: Use first row and column to mark zeroes
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        
        # Step 3: Set elements to zero based on markers
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        # Step 4: Handle the first row and column separately
        if colZero:
            for r in range(rows):
                matrix[r][0] = 0
        
        if rowZero:
            for c in range(cols):
                matrix[0][c] = 0