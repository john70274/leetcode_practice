class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        left = 0
        right = len(matrix) * len(matrix[0]) - 1
        len_matrix = len(matrix[0])
        while left <= right:
            mid = (left + right) // 2
            m = mid // len_matrix
            n = mid % len_matrix
            print("mid: ", mid, "m: ", m, "n: ", n)
            if matrix[m][n] < target:
                left = mid + 1
            elif matrix[m][n] > target:
                right = mid - 1
            elif matrix[m][n] == target:
                return True
        return False

sol = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
ans = sol.searchMatrix(matrix, target)
print(ans)