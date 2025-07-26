from collections import deque
i1,j1=map(int,input().split())
i2,j2=map(int,input().split())
k=int(input())
row=4
grid=[]
for _ in range(row):
    line=input()
    grid.append(line.strip().split())
n=len(grid)
m=len(grid[0])
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
queue=deque()
start_value=0
if grid[i1][j1]!="*":
    start_value=int(grid[i1][j1])
queue.append((i1,j1,0,start_value))
visited=[[[False]*(k+1) for _ in range(m)] for _ in range(n)]
visited[i1][j1][0]=True
#bfs srearch 
found=False
max_coins=-1
step=0
while queue and not found:
    for _ in range(len(queue)):
        x,y,skip_use,coin_collect=queue.popleft()
        if (x,y)==(i2,j2):
            max_coins=coin_collect
            found=True
            break 
        for dx,dy in dirs:
            nx,ny=x+dx,y+dy
            if 0<=nx <n and 0<=ny <m:
                cell=grid[nx][ny]
                if cell=="*":
                     if skip_use<k and not visited[nx][ny][skip_use+1]:
                       visited[nx][ny][skip_use+1]=True
                       queue.append((nx,ny,skip_use+1,coin_collect))
                else:
                    value=int(cell)
                    if not visited[nx][ny][skip_use]:
                        visited[nx][ny][skip_use]=True
                        queue.append((nx,ny,skip_use,coin_collect+value))
    if not found:
        step+=1
print(max_coins if max_coins != -1 else 0) 

              






