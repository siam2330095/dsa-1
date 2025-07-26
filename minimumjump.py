# from collections import deque 
# def minimummjump(arr):
#     n=len(arr)
#     mapping={}
#     for i,val in enumerate(arr):
#         if val not in mapping:
#             mapping[val]=[]
#         mapping[val].append(i) 
#     visited=[False]*n
#     #first visit node index 0
#     visited[0]=True 
#     queue=deque([0])
#     step=0
#     while queue:
#         for x in range(len(queue)):
#             i=queue.popleft()
#             if i==n-1:
#                 return step 
#             #check  left child
#             if 0<=i-1<n and visited[i-1]==False:
#                 queue.append(i-1)
#                 visited[i-1]=True
#             #check right child 
#             if 0<=i+1<n and visited[i-1]==False:
#                 queue.append(i+1)
#                 visited[i+1]=True 
#             #check same value child 
#             if arr[i] in mapping:
#                 for child in mapping[arr[i]]:
#                     if visited[child]==False:
#                         queue.append(child)
#                         visited[child]=True
#         step+=1
#     return -1
                
# arr = [100,-23,-23,404,100,23,23,23,23,3,404]
# print(minimummjump(arr)) 
# same code just practise 
from collections import deque
def minimum(arr):
    n=len(arr)
    mapping={}
    for i ,val in enumerate(arr):
        if val not in mapping:
            mapping[val]=[]
        mapping[val].append(i)
    visited=[False]*n
    visited[0]=True
    queue=deque([0])
    step=0
    while queue:
        for x in range(len(queue)):
            i=queue.popleft()
            if i==n-1:
                return step
            #check left child 
            if 0<=i-1<n and visited[i-1]==False:
                queue.append(i-1)
                visited[i-1]=True
            if 0<=i+1<n and visited[i+1]==False:
                queue.append(i+1)
                visited[i+1]=True 
            #same value in arr
            if arr[i] in mapping:
                for child in mapping[arr[i]]:
                    if visited[child]==False:
                        queue.append(child)
                        visited[child]=True
        step+=1
    return -1 
arr = [100,-23,-23,404,100,23,23,23,23,3,404]
print(minimum(arr)) 


                        
                
                
                
                
        