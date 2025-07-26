from collections import deque
def has_path(grid):
    if not grid and grid[0][0]==0:
        return False
    m,n=len(grid),len(grid[0])
    visited=[[False]*n for _ in range(m)]
    directions = [(-1,0), (1,0), (0,-1), (0,1)] 
    queue=deque()
    queue.append((0,0))
    visited[0][0]=True
    while queue:
        x,y=queue.popleft()
        if x==m-1 and y==n-1:
            return True #buttom reached
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0<=nx<m and 0<=ny<n and grid[nx][ny]==1 and not visited[nx][ny]:
                visited[nx][ny]=True
                queue.append((nx,ny))
    return False 
grid = [
    [1,0,1],
    [1,1,1],
    [0,0,1]
]

print(has_path(grid)) 
    