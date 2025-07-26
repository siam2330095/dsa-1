v=6
adj=[[1,2], #0
     [0,3],  #1
     [0,3],  #2
     [1,2,4],  #3
     [3,5],   #4
     [4]    #5
     ]
from collections import deque 
def bfs(v,adj):
    visited=[False]*v
    queue=deque()
    
    traversal=[]
    queue.append(0)
    visited[0]=True
    while queue:
        node=queue.popleft()
        traversal.append(node)
        for nei in adj[node]:
            if not visited[nei]:
                visited[node]=True
                queue.append(nei)
                
                
    print(traversal)
bfs(v,adj)
    