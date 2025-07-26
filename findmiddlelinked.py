class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def middile(head):
    slow=head
    fast=head
    while fast is not None and fast.next is not None:
        fast=fast.next.next
        slow=slow.next
           
    return slow.data
head=Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)
head.next.next.next.next.next = Node(60)
print(middile(head))
