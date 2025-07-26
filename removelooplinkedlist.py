class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 
def removeLoop(head):
    slow = head
    fast = head
    while slow and fast and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = head
        # Special case when loop starts at head
            while fast != slow:
                slow = slow.next
                fast = fast.next
            while fast.next != slow:
                fast = fast.next
            fast.next = None
        
# Function to print the list
def printList(curr):
    while curr:
        print(curr.data, end=' ')
        curr = curr.next
    print()
# Main execution
if __name__ == "__main__":
    # Create a linked list: 1 -> 3 -> 4
    head = Node(1)
    head.next = Node(3)
    head.next.next = Node(4)
    
    # Introduce a loop: last node (4) points back to node (3)
    head.next.next.next = head.next

    # Before removing the loop, printing would result in an infinite loop
    # So we call removeLoop first
    removeLoop(head)

    # Now it's safe to print
    print("Linked list after removing loop:")
    printList(head)
