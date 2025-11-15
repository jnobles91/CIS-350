def _subtree_search_iterative(self,p,k):
    while k != p.key() and p.key() != None:
        #search until we find a match or reach the end of the tree
        if k < p.key():
            #search left if target is less than current
            p = self.left(p)
        else:
            #search right if target is greater than current
            p = self.right(p)
    #return p if we find a match, or return None if we dont
    return p