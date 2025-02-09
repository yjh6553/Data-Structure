class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in range(len(matrix)):
            left, right = 0, len(matrix[0]) - 1


            while left <= right:
                mid = (left + right) // 2
                if matrix[row][mid] == target:
                    return True
                elif matrix[row][mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
        
        return False
