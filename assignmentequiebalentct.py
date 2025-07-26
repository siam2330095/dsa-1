# from collections import deque 
# n,e=map(int,input().split())
# graph=[[] for _ in range(n)] 
# for _ in range(e):
#     u,v=map(int,input().split())
#     graph[u].append(v)
#     graph[v].append(u)
# target=int(input())
# visited=[False]*n
# level=[-1]*n
# queue=deque()
# queue.append(0)
# visited[0]=True
# level[0]=0
# while queue:
#     node=queue.popleft()
#     for neibore in graph[node]:
#         if not visited[neibore]:
#             visited[neibore]=True
#             level[neibore]=level[node]+1
#             queue.append(neibore) 
# print(level[3]) # 3 means target 
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

