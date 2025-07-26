# from collections import deque
# class treeNode:
#     def __init__(self,val=0,left=None,right=None):
#         self.val=val
#         self.left=left
#         self.right=right
        
# def  buildbinarytree(nodes):
#     if not nodes or nodes[0] is None:  # if list empty then return None
#         return None
#     root=treeNode(nodes[0])
#     queue=deque([root])
#     index=1
#     while queue and index<len(nodes):
#         node=queue.popleft()
#         if index<len(nodes) and nodes[index] is not None:
#             node.left=treeNode(nodes[index])
#             queue.append(node.left)
#         index+=1
#         if index < len(nodes) and nodes[index] is not None:
#             node.right = treeNode(nodes[index])
#             queue.append(node.right)
#         index += 1 
#     return root
# def pathsum(root,targetsum):
#     if not root:
#         return False
#     if not root.left and not  root.right :
#         return root.val==targetsum
#     return (pathsum(root.left,targetsum-root.val) or  pathsum(root.right,targetsum-root.val) )
# nodes = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
# targetsum = 22 
# root =buildbinarytree(nodes)
# print(pathsum(root, targetsum))
from collections import deque
class treeNode:
    def __init__(self,val=0):
        self.val=val
        self.left=None
        self.right=None
def buildbinarytree(nodes):
    if not nodes or nodes[0] is None:
        return None 
    root=treeNode(nodes[0])
    queue=deque([root])
    index=1
    while queue and index<len(nodes):
        node=queue.popleft()
        if index<len(nodes) and nodes[index] is not None:
            node.left=treeNode(nodes[index])
            queue.append(node.left)
        index+=1
        if index<len(nodes) and nodes[index] is not None:
            node.right=treeNode(nodes[index])
            queue.append(node.right)
        index+=1
    return root
def pathsum(root,targetsum):
    if not root:
        return False
    if not root.right and not root.left:
        return root.val==targetsum
    return (pathsum(root.left,targetsum-root.val) or pathsum(root.right,targetsum-root.val))
nodes = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
targetsum = 22 
root =buildbinarytree(nodes)
print(pathsum(root, targetsum))
    