class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        
        totalElements = row * col
        left, right = 0, totalElements-1

        while left <= right:
            mid = (left+right) // 2
            i = mid // col
            j = mid % col

            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False