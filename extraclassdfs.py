v=6
adj=[[1,2],
     [0,3],
     [0,3],
     [1,2,4],
     [3,5],
     [4]
     ] 
def dfs(v,adj):
    visited=[False]*v
    traversal=[]
    def dfs_uti(node):
        visited[node]=True
        traversal.append(node)
        for nei in adj[node]:
            if not visited[nei]:
                dfs_uti(nei)
    dfs_uti(0)
    print(traversal)
dfs(v,adj) 
