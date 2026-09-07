class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        lo = 0
        hi = m - 1
        row = 0
        while lo <= hi :
            mid = lo + (hi - lo) // 2
            if matrix[mid][0] <= target <= matrix[mid][n-1]:
                row = mid
                break
            elif matrix[mid][0] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        lo = 0
        hi = n - 1
        while lo <= hi :
            mid = lo + (hi - lo) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return False
            
            