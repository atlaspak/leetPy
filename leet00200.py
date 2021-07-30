class Solution:    
    def cleanIsland(self,grid, i,j):
        grid[i][j] = "0"
        if (j+1 < self.lenLin) and (grid[i][j+1] == "1"):
            self.cleanIsland(grid,i,j+1)
        if (i+1 < self.lenCol) and (grid[i+1][j] == "1"):
            self.cleanIsland(grid,i+1,j)
        if (j-1 >= 0) and (grid[i][j-1] == "1"):
            self.cleanIsland(grid,i,j-1)            
        if (i-1 >= 0) and (grid[i-1][j] == "1"):
            self.cleanIsland(grid,i-1,j)
    
    def numIslands(self, grid: List[List[str]]) -> int:        
        self.lenLin = len(grid[0])
        self.lenCol = len(grid)
        islandCount = 0
        
        for i in range(self.lenCol):
            for j in range(self.lenLin):
                if(grid[i][j] == "1"):
                    self.cleanIsland(grid,i,j)
                    islandCount += 1
        return islandCount
