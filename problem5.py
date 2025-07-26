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
            
    