class Node:
    def __init__(self,data):
        self.data=data
        self.next=None 

def findminimum(head):
    if head is None:
        return "LIST IS EMPTY" 
    mini=head.data
    current=head.next 
    while current :
        if current.data <mini:
            mini=current.data
        current=current.next
    return mini
head=Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)
head.next.next.next.next.next = Node(60)
print(findminimum(head))