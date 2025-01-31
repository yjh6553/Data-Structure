class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for r in range(len(matrix)):
            left, right = 0, len(matrix[0]) - 1
            if matrix[r][0] <= target <= matrix[r][len(matrix[r]) - 1]:
                while left <= right:
                    mid = (left + right) // 2
                    if matrix[r][mid] == target:
                        return True
                    if matrix[r][mid] < target :
                        left = mid + 1
                    else:
                        right = mid - 1
        return False

        #Time: O(n)
        #Space: O(1)