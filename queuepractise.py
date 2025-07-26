#normal queue dequeue
qsize=5
myq=[0]*qsize
front=-1
rear=-1
def enqueue(x):
    global front,rear,myq
    #checkoverflow
    if rear>=qsize-1:
        print("queue is overflow")
    elif front==-1 and rear==-1:
        front=rear=0
        myq[rear]=x
        print(f"inserted:{x}")
    else:
        raer+=1
        myq[rear]=x
        print(f"inserted:{x}") 
myq=[1,2,3,4,5]
front=0
rear=len(myq)-1
def dequeue(queue,front,rear):
    if (front>rear )or (front==-1 and rear==-1):
        print("queue is underflow")
    else:
        value=queue[front]
        front+=1
        return value,front
    value,front=dequeue(myq,front,rear) 
    if value is not None:
        print("deque value",value)
def displayqueue():
    if front==-1 or front>rear:
        print("queue is empty")
    else:
        print("queue elements")
        for i in range(front,rear+1):
            print(myq[i],end=" ")
        print()