from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY, FRESH, ROTTEN = 0,1,2
        q= deque()
        num_mins=-1
        num_fresh=0
        m,n= len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j]==ROTTEN:
                    q.append((i,j))    
                elif grid[i][j]==FRESH:
                    num_fresh+=1
        
        if num_fresh ==0: 
            return 0 #took 0 minutes

        while q:
            num_mins+=1
            q_size=len(q)

            for _ in range(q_size):
                i,j=q.popleft()
                for r,c in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
                    if ((0<=r<m) and (0<=c<n) and grid[r][c]==FRESH):
                        grid[r][c]=ROTTEN
                        num_fresh-=1
                        q.append((r,c))
            
        if num_fresh==0:
            return num_mins
        else:
            return -1
# TC: O(M*N)
# SC: O(M*N)
#         EMPTY, FRESH, ROTTEN = 0, 1, 2
#         m, n = len(grid), len(grid[0])
#         num_fresh = 0
#         q = deque()

#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == ROTTEN:
#                     q.append((i, j))
#                 elif grid[i][j] == FRESH:
#                     num_fresh += 1

#         if num_fresh == 0:
#             return 0

#         num_minutes = -1
#         while q:
#             q_size = len(q)
#             num_minutes += 1
        
#             for _ in range(q_size):
#                 i, j = q.popleft()
#                 for r, c in [(i, j + 1), (i + 1, j), (i, j - 1), (i - 1, j)]:
#                     if 0 <= r < m and 0 <= c < n and grid[r][c] == FRESH:
#                         grid[r][c] = ROTTEN
#                         num_fresh -= 1
#                         q.append((r, c))

#         if num_fresh == 0:
#             return num_minutes
#         else:
#             return -1

# #TC: O(m*n)
# #SC: O(m*n)