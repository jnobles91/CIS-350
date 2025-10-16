##Design algorithms for the following operations for a binary tree T:
#preorder next(p): Return the position visited after p in a preorder
#traversal of T (or None if p is the last node visited).
#inorder next(p): Return the position visited after p in an inorder
#traversal of T (or None if p is the last node visited).
#postorder next(p): Return the position visited after p

from trees import LinkedBinaryTree

def preorder_next(T, p):
    #if there is a left child that is the next node we will visit preorder, just return that
    if T.left(p) is not None:
        return T.left(p)
    #if there is no left but a right child, return right child since that is the next node we will visit preorder
    if T.right(p) is not None:
        return T.right(p)
    #start climbing up the tree
    while True:
        parent = T.parent(p)
        if parent is None:
        #if we get to the first node in the tree without finding a right child we havent visited there is no next item to visit preorder, return none
            return None
        if T.left(parent) is p and T.right(parent) is not None:
        #if we hit a node with a right child that we wouldn't have visited yet preorder that is the next node, return it
            return T.right(parent)
        p = parent


def inorder_next(T, p):
    r = T.right(p)
    if r is not None:
        #if there is a node to the right its leftmost node will be the one we have to go to next in inorder traversal
        while T.left(r) is not None:
            r = T.left(r)
        #find the leftmost node and return it
        return r
    #otherwise climb til we come from a left child, then return that parent node
    while True:
        parent = T.parent(p)
        if parent is None:
            #we reached the absolute root without finding a valid node, we are at the end of an inorder traversal
            return None
        if T.left(parent) is p:
        #weve reached a node where we came from the left child, so this is t6he next node in an inorder traversal
            return parent
        p = parent


def postorder_next(T, p):
    parent = T.parent(p)
    if parent is None:
        # we are at root, there would be no next node to visit postorder
        return None
    if T.left(parent) is p and T.right(parent) is not None:
    #if we are at a left leaf we are trying to find the leftmost leaf of our parents right child
        current = T.right(parent)
        while True:
            left, right = T.left(current), T.right(current)
            if left is not None:
                current = left
            elif right is not None:
                current= right
            else:
                return current
    #otherwise parent is next, return that
    return parent





