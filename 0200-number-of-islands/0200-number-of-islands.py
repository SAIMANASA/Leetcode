#import deque from collections
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid) , len(grid[0])
        visited = set() #or use an adjacency matrix
        islands = 0

        def bfs(self,r,c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))

            while q:

                row,col = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]

                for dr,dc in directions:
                    drow = row+dr 
                    dcol = col+dc 
                    if (drow in range(rows) and dcol in range(cols) and 
                        grid[drow][dcol] == '1' and 
                        (drow,dcol) not in visited):
                        q.append((drow,dcol))
                        visited.add((drow,dcol))


        for i in range(0,rows):
            for j in range(0,cols):
                if grid[i][j] == '1' and  (i,j) not in visited:
                    bfs(self,i,j)
                    islands+=1
        return islands       