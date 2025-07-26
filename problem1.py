from collections import deque
n,e=map(int,input().split())
graph=[[] for _ in range(n)]
for _ in range(e):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
target=int(input())
visited=[False]*n
level=[-1]*n
queue=deque([0])
visited[0]=True
level[0]=0
while queue:
    node=queue.popleft()
    for neibour in graph[node]:
        if not visited[neibour]:
            visited[neibour]=True
            level[neibour]=level[node]+1
            queue.append(neibour)
print(level[3])

