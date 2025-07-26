# class Node:
#     def __init__(self,key):
#         self.key=key
#         self.left=None
#         self.right=None
        
# def insert(root,key):
#     if root is None:
#         return Node(key)
#     if key<root.key:
#         root.left=insert(root.left,key)
#     else:
#         root.right=insert(root.right,key)
#     return root

# def delete(root,key):
#     if root is None:
#         return root
#     if key<root.key:
#         root.left=delete(root.left,key)
    
#     elif  key>root.key:
#         root.right=delete(root.right,key) 
#     else:
#         if root.left is None:
#             return root.right
#         elif root.right  is None:
#             return root.left 
#         ss=minvaluenode(root.right)
#         root.key=ss.key
#         root.right=delete(root.right,ss.key)
#     return root 
# def minvaluenode(first):
#     current=first
#     while current.left is not None:
#         current=current.left
#     return current 
# def search (root,key):
#     if root is None:
#         return False
#     if root.key==key:
#         return True
#     elif key<root.key:
#         return search(root.left,key)
#     else:
#         return search(root.right,key) 
    
# def inorder(root):
#     if root:
#         inorder(root.left)
#         print(root.key,end=" ")
#         inorder(root.right)
        
# def preorder(root):
#     if root:
#         print(root.key,end=" ")
#         preorder(root.left)
#         preorder(root.right) 
        
# def postorder(root):
#     if root:
#         postorder(root.left)
#         postorder(root.right) 
#         print(root.key,end=" ") 
        
# def height(root):
#     if root is Node:
#         return 0
#     return 1+max(height(root.left),height(root.right)) 





class Node:
    def __init__(self,key):
        self.key=key 
        self.left=None
        self.right=None
       
def insertation(root,key):
    if root is None:
        return Node(key)
    if key<root.key:
        root.left=insertation(root.left,key)
    else:
         root.right=insertation(root.right,key)
    return root 
def deletion(root,key):
    if root is None:
        return root 
    elif key<root.key:
        root.left=deletion(root.left,key)
    
    elif  key>root.key:
          root.right=deletion(root.right,key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        ss=minimumvalue(root.right)
        root.key=ss.key
        root.right=deletion(root.right,ss.key)
    return root
def minimumvalue(first):
    current=first
    while current.left is not None:
        current=current.left
    return current  
def search(root,key):
    if root is None:
        return False
    if root.key==key:
        return True 
    elif key<root.key:
        return search(root.left,key)
    else:
        return search(root.right,key) 
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key,end=" ")
        inorder(root.right)
def preorder(root):
    if root:
        print(root.key,end=" ")
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.key,end=" ")
        
def hight(root):
    if root is Node:
        return 0
    return 1+max(height(root.left),height(root.right))  
    