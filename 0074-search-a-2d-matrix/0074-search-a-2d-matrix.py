class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        
        mid_row = len(matrix) // 2
        
        
        if matrix[mid_row][0] > target:
            return self.searchMatrix(matrix[0:mid_row], target)
        elif matrix[mid_row][-1] < target:
            return self.searchMatrix(matrix[mid_row+1:], target)
        else:
            for num in matrix[mid_row]:
                if num == target:
                    return True
            
        return False
        
