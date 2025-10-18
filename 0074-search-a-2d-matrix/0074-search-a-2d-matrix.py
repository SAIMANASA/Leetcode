class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        top, bot = 0 , row-1
        
        while(top<=bot):
            mid = (top+bot)//2
            if matrix[mid][0] > target:
                bot = mid-1
            elif matrix[mid][-1] <  target:
                top = mid+1
            else:
                break 
        
        if top > bot:
            return False
        mid = (top+bot)//2

        topcol = 0
        botcol = col-1
        while(topcol <= botcol):
            midcol = (topcol+botcol) //2
            if matrix[mid][midcol] > target:
                botcol=midcol-1
            elif matrix[mid][midcol] < target:
                topcol = midcol+1
            elif matrix[mid][midcol] == target:
                return True
        
        return False

        