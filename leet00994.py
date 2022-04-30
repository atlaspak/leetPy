class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        que = deque()
        next_que = deque()
        for i in range(N):
            for j in range(M):
                if(grid[i][j] == 2):
                    que.append([i,j])
                    
        elapsed_time = 0   
        while que:
            i,j = que.pop()
            if(i-1 >= 0 and grid[i-1][j] == 1):
                grid[i-1][j] = 2
                next_que.append([i-1,j])            
            if(j-1 >= 0 and grid[i][j-1] == 1):
                grid[i][j-1] = 2
                next_que.append([i,j-1])
            if(i+1 < N and grid[i+1][j] == 1):
                grid[i+1][j] = 2
                next_que.append([i+1,j])
            if(j+1 < M and grid[i][j+1] == 1):
                grid[i][j+1] = 2
                next_que.append([i,j+1])
            
            if not que:
                if not next_que:
                    break
                elapsed_time += 1
                que = next_que
                next_que = deque()
                
        for row in grid:
            for orange in row:
                if orange == 1:
                    return -1
        
        return elapsed_time
