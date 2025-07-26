# def has_cycle(n,edge):
#     graph=[[] for _ in range(n)]
#     for u,v in edge:
#         graph[u].append(v)
#         graph[v].append(u) 
#     def dfss(node,parent): #
#         visited[node]=True
#         for neibour in graph[node]:
#             if not visited[neibour]:
#                 if dfss(neibour,node):
#                     return True 
#             elif neibour!=parent:
#                 return True
#         return False        
#     visited=[False]*n
#     for i in range(n):
#         if not visited[i]:
#             if dfss(i,-1):
#                 return True
            
        
#     return False 
# n = 4
# edge  = [
#     (0, 1),
#     (1, 2),
#     (2, 0),
#     (2, 3)
# ]
# print(has_cycle(n, edge)) 
from collections import deque
def has_cycle_bfs():
    N, E = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)  
    visited=[False]*N 
    def bfs(start):
        queue=deque()
        queue.append((start,-1)) #current node and parent
        visited[start]=True
        while queue:
            node,parent=queue.popleft()
            for neighbour in graph[node]:
                if not visited[neighbour]:
                    visited[neighbour]=True
                    queue.append((neighbour,node))
                elif neighbour!=parent:
                    return True
        return False
    #check all componenet
    for i in range(N):
        if not visited[i]:
            if bfs(i):
                return True
    return False 
print(has_cycle_bfs())
            
    