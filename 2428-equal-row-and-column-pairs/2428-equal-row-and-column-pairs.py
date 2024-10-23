from collections import defaultdict
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
         #dict for rows
        # Create a defaultdict with a default value of an empty list
        rowcount=defaultdict(int)
        
        count=0
        #taking the count of rows repetition
        for row in grid:
            rowcount[tuple(row)]+=1
        #zip(*matrix) function makes transpose of the matrix
        for column in zip(*grid):
            count+=rowcount[column]
        return count
       ## out = 0
       ## n = len(grid)
        ##for i in range(n):
         ##   row = ",".join(map(str,grid[i]))
          ##  for j in range(n):
           ##     col = ','.join(str(grid[k][j]) for k in range(n))
            ##    if row == col:
             ##       out += 1
        ##return out 
  
     