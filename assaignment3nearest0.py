from  collections import deque
def matrixs(matrix):
    if not matrix:
        return []
    m,n=len(matrix),len(matrix[0])
    dist=[[float('inf')]*n  for _ in range(m)]
    queue=deque()
    for i in range(m):
        for j in range(n):
            if matrix[i][j]==0:
                dist[i][j]=0
                queue.append((i,j))
    directions = [(-1,0), (1,0), (0,-1), (0,1)]  # up, down, left, right
    while queue:
        x,y=queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0<=nx<m and 0<=ny<n:
                if dist[nx][ny]>dist[x][y]+1:
                    dist[nx][ny]=dist[x][y]+1
                    queue.append((nx,ny))
    return dist
matrix = [
    [0,0,0],
    [0,1,0],
    [1,1,1]
]

result = matrixs(matrix)
for row in result:
    print(row)

    
        