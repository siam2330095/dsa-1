class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def constructBSTfromPostorder(postorder):
    index = [len(postorder) - 1]

    def helper(min_val, max_val):
        if index[0] < 0:
            return None
        val = postorder[index[0]]
        if val < min_val or val > max_val:
            return None
        node = Node(val)
        index[0] -= 1
        node.right = helper(val, max_val)  # Right child
        node.left = helper(min_val, val)   # Left child
        return node

    return helper(float('-inf'), float('inf'))

# Reconstruct the BST
postorder = [13, 10, 8, 7, 12, 11, 16, 14, 15, 18]
root = constructBSTfromPostorder(postorder)
