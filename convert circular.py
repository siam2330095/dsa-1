class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)
head.next.next.next.next.next = Node(60)
current=head
while current.next is not None:
    current=current.next 
current.next=head 

def display(self):
        current=head
        while current is not None:
            print(f"{current.data}",end="-->")
            current  = current .next
            if current==head:
                break
            
        print("none") 