class Node:
    def __init__(self, data):
        self.data =data
        self.next = None
def printList(head):
    current = head
    while current is not None:
        print(current.data, end=" ")
        current = current.next 
    print()
def merge(head1, head2):
    current1= head1
    current2= head2
                    
    # Traverse both lists and merge them
    while current1  is not None and current2 is not None:
      
        # Save the next nodes of the current
        # nodes in both lists
        ptr1 = current1.next
        ptr2 = current2.next

        # Insert the current node from the second list
        # after the current node from the first list
        current2.next = current1.next
        current1.next = current2 

        # Update the pointers for the next iteration
        current1 = ptr1
        current2 = ptr2

    return [head1, current2]
           
if __name__ == "__main__":
    
    # Creating first linked list 1->2->3
    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(3)

    # Creating second linked list 4->5->6->7->8
    head2 = Node(4)
    head2.next = Node(5)
    head2.next.next = Node(6)
    head2.next.next.next = Node(7)
    head2.next.next.next.next = Node(8)

    # Store first and second head points in array
    ar = merge(head1, head2)
    printList(ar[0])
    printList(ar[1])    