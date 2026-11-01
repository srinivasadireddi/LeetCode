class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        islands=0
        
        def dfs(i,j):
            #edge cases
            if(i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]=='0'):
                return
            else:
                grid[i][j]='0'
                dfs(i-1,j)
                dfs(i+1, j)
                dfs(i, j-1)
                dfs(i, j+1)
        
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if(grid[m][n]=='1'):
                    # grid[m][n]=='0' #redundant
                    islands+=1
                    dfs(m,n)

        return islands             
   

