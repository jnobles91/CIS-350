##Design algorithms for the following operations for a binary tree T:
#preorder next(p): Return the position visited after p in a preorder
#traversal of T (or None if p is the last node visited).
#inorder next(p): Return the position visited after p in an inorder
#traversal of T (or None if p is the last node visited).
#postorder next(p): Return the position visited after p


class LinkedBinaryTree():
    
    class Node():
        __slots__ = 'data', 'parent','left','right'

        def __init__(self,data,parent,left,right):
            self.data = data
            self.parent = parent
            self.left = left
            self.right = right
    
    def __init__(self):
        root = None
        
    
