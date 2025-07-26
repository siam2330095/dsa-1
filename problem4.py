from collections import deque 
def minimum_operation(A,B): #current number a and b number of operation 
    visited=set()
    queue=deque()
    queue.append((A,0))
    while queue:
        current_number,step=queue.popleft()
        if current_number== B:
            return step
        if current_number in visited:
            continue
        visited.add(current_number)
        queue.append((current_number+1,step+1)) 
        queue.append((current_number-1,step+1)) 
        queue.append((current_number*2,step+1))
A = 0
B = 63
print(minimum_operation(A, B))