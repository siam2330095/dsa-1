class Node:
    def __init__(self, data):
        self.data = data
        self.next = None                                                                                                                            
class singlylinkedlist:
    def __init__(self):
        self.head=None 
    def insert_last(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return   
        current = self.head
        while current.next is not None:
            current  = current .next
        current .next = new_node 
    def delete_last(self):
        if self.head is None:
            print("nothing delete")
            return 
        elif self.head.next is None:
            del self.head 
            self.head=None
            return
        else:
            current=self.head
            while current.next.next is not None:
                current=current.next
            del current.next 
            current.next=None 
    # Remove duplicates in a sorted list
    def remove_duplicates(self):
        current = self.head
        while current and current.next is not None:  
            if current.data == current.next.data:
                current.next = current.next.next  # skip duplicate
            else:
                current = current.next 
                       
    def printforword(self):
        current=self.head
        while current is not None:
            print(f"{current.data}",end="-->") 
            current  = current.next 
        print("none")         
    def printbackword(self):
        stack = []
        current = self.head    
        while current is not None:
            stack.append(current.data) 
            current=current.next
        print("Singly linked list (backward): NULL", end=" ")
        while stack:
            print(" <-", stack.pop(), end=" ") 
        print()
if __name__ == "__main__":
    ll = singlylinkedlist()
    for val in [1, 2, 3, 4, 5]:
        ll.insert_last(val)

    ll.printforword()
    ll.printbackword()
    ll.remove_duplicates()
        
    