class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class doublylinked:
    def __init__(self):
        self.head=None
    def insert_first(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.prev=new_node
        self.head=new_node 
    def insert_last(self,data):
        new_node=Node(data) 
        if self.head is None:
            self.head=new_node
            return
        current=self.head
        while current.next is not None:
            current=current.next 
        current.next=new_node
        new_node.prev=current


                 
    def insert_at(self,data,position):
        if position<0 :
            print("invalide position")
        elif position==0:
            self.insert_first(data)
            return 
        else:
            new_node=Node(data)
            current =self.head 
            current_position= 0
            while current is not None and current_position<position-1 :
                current=current.next
                current_position+=1

            new_node.next=current.next 
            new_node.prev=current
            if current.next is not None:
                current.next.prev=new_node
            current.next=new_node
    def delete_first(self):
        head=self.head
        if self.head.next is not  None:
            self.head=self.head.next
        del head  
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
    def delete_item(self,item):
        current=self.head
        while current is not None:
            if current.data==item:
                if current.prev is not None:
                    current.prev.next=current.next 
                if current.next is not None:
                    current.next.prev=current.prev
                del current
                return  
            current=current.next


    def search_item(self,item):
        current=self.head
        position=0
        while current is not None:
            if current.data==item:
                return position
            current=current.next
            position+=1 
        return -1
    def printforword(self):
        current=self.head
        while current is not None:
            print("Doubly linked list (forward): ", end="")
            print(f"{current.data}",end="-->")
            current  = current .next
        print()
    
    def printbackward(self):
        current = self.head
        while current is not None and current.next is not None:
            current = current.next
        print("Doubly linked list (backward): NULL", end="")
        while current is not None:
            print(" <-", current.data, end="")
            current = current.prev
        print()
    