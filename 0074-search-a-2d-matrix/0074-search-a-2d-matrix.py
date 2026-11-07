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

            print(matrix[i][j])

            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False

        # for i in range(len(matrix)):
        #     x = matrix[i]
        #     left, right = 0, len(x) - 1

        #     while left <= right:
        #         mid = (left+right) // 2

        #         if x[mid] == target:
        #             return True
        #         elif x[mid] > target:
        #             right = mid - 1
        #         else:
        #             left = mid + 1

        # return False