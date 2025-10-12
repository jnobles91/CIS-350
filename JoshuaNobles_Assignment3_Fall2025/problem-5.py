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
    
    
    
    
    
    
    
    
    
    def _postfix_conversion(self,p,array):
        if self.is_leaf(p):
            #if the node has no children it is a number, so append it to the array
            array.append(str(p.element()))
        else:
            #else navigate through the tree postorder and append
            self._postfix_conversion(self.left(p), array)
            self._postfix_conversion(self.right(p),array)
            array.append(str(p.element()))
    
    def postfix_conversion(self):
        postfix_array = []
        self._postfix_conversion(self.root(),postfix_array)
        return ' '.join(postfix_array)
    
    