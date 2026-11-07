class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #first search BETWEEN the starting values in each row
        #find rows a,b s.t. target lies in between 
        # -- first value of matrix[a] and matrix[b]
        # -- so matrix[a] < target < matrix[b]
        # then binary search matrix[a]


        #initially - search only matrix[0][0], matrix[1][0], etc.

        lo_row = 0
        hi_row = len(matrix)
        while lo_row<hi_row:
            mid_row = ((hi_row+lo_row)//2)

            if matrix[mid_row][0]==target:
                return True
            
            elif matrix[mid_row][0]<target:
                lo_row = mid_row+1
            #if matrix[mid_row][0]>target:
            else:
                hi_row = mid_row
        
        #if matrix[mid_row][0]<target we start at mid row
        if matrix[mid_row][0]>target:
            #we start at mid_row-1
            mid_row -= 1

        lo = 0
        hi = len(matrix[0])
        while lo<hi:
            mid = ((hi+lo)//2)

            if matrix[mid_row][mid]==target:
                return True
            elif matrix[mid_row][mid]<target:
                lo = mid+1
            #if matrix[mid_row][mid]>target:
            else:
                hi = mid

        return False