from trees import LinkedBinaryTree

class ExpressionTree(LinkedBinaryTree):
    #expression tree class from book
    def __init__(self, token, left=None, right=None):
        super().__init__()
        if not isinstance(token, str):
            raise TypeError("Token must be a string")
        self._add_root(token)
        if left is not None:
            if token not in "+-x*/":
                raise ValueError("token must be valid operator")
            self._attach(self.root(), left, right)

    def __str__(self):
        pieces = []
        self.parenthesize_recur(self.root(), pieces)
        return "".join(pieces)

    def parenthesize_recur(self, p, result):
        if self.is_leaf(p):
            result.append(str(p.element()))
        else:
            result.append("(")
            self.parenthesize_recur(self.left(p), result)
            result.append(p.element())
            self.parenthesize_recur(self.right(p), result)
            result.append(")")
    
    
    
    
    
    
    
#Convert a tree to postfix   
    
    def _postfix_conversion(self,p,array):
    #helper function so we don't have to pass arguments to the method
        if self.is_leaf(p):
            #if the node has no children it is a number, so append it to the array
            array.append(str(p.element()))
        else:
            #else navigate through the tree postorder and append
            self._postfix_conversion(self.left(p), array)
            self._postfix_conversion(self.right(p),array)
            array.append(str(p.element()))
    
    def postfix_conversion(self):
        #initialize an array to store the numbers and operators from the tree
        postfix_array = []
        self._postfix_conversion(self.root(),postfix_array)
        #call helper function
        return ' '.join(postfix_array)
        #return the array as a string ex x y +
    

#built a tree out to test
    

subtree_1 = ExpressionTree("+", ExpressionTree("5"), ExpressionTree("9")) #(5+9)
subtree_2 = ExpressionTree("*", ExpressionTree("4"), subtree_1) #(4*(5+9))
full_tree = ExpressionTree("-", ExpressionTree("3"), subtree_2) #(3-(4*(5+9)))

print(str(full_tree))  #(3-(4*(5+9)))
print(full_tree.postfix_conversion()) #3459+*-

    
    