class circularqueue:
    def __init__(self,size):
        self.size=size
        self.queue=[None]*self.size
        self.front=-1
        self.rear=-1
    def enqueue(self,x):
        if (self.rear+1)%self.size==self.front:
            print("queue is overflow")
            
        elif self.front==-1 and self.rear==-1:
            self.front=self.rear=0
            self.queue[self.rear]=x
        else:
            self.rear=(self.rear+1)%self.size
            self.queue[self.rear]=x
            
            
    def dequeue(self):
        if self.front==-1 and self.rear==-1:
            print("queue is underflow")
        elif self.front==self.rear:
            print(f"Dequeued: {self.queue[self.front]}")
            self.front = self.rear = -1
        else:
            print(f"Dequeued: {self.queue[self.front]}")
            self.front = (self.front + 1) % self.size
    def display(self):
        if self.front == -1 and self.rear == -1:
            print("Queue is empty")
        else:
            i=self.front
            while i!=self.rear:
                print(self.queue[i],end=" ")
                i=(i+1)%self.size
            print(self.queue[self.rear])
c=circularqueue(5)