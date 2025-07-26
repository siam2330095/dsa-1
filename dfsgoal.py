v=6
adj=[[1,2], #0
     [0,3],  #1
     [0,3],  #2
     [1,2,4],  #3
     [3,5],   #4
     [4]    #5
     ]
start=0
goal=(3,4)
def dfs(v,adj):
    visited=[False]*v
    traversal=[]
    def dfs_uti(node):
        visited[node]=True            
        traversal.append(node)
        if len(traversal)>=2 and tuple(traversal[-2:])==goal:                       
            print("goal is reacheabble")    
            return True
        for nei in adj[node]:
            if not visited[nei]:
                if dfs_uti(nei):
                    return
        traversal.pop()
        return False     
                    
    dfs_uti(start)
    print(traversal)
dfs(v,adj) 
