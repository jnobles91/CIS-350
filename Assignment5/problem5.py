from modules import AVLTreeMap

def _height_helper(tree, p):
    if p is None:
        return -1
    return 1 + max(_height_helper(tree, tree.left(p)),
                   _height_helper(tree, tree.right(p)))

def tree_height(tree):
    #recursively get tree height
    return _height_helper(tree, tree.root())

def print_tree(tree):
    #go all the way to the right first to print from top to bottom
    #add to indent for deeper levels
    def _helper(p, indent=""):
        if p is None:
            return
        _helper(tree.right(p), indent + "    ")
        print(f"{indent}{p.key()}:{p.value()}")
        _helper(tree.left(p), indent + "    ")

    _helper(tree.root())

def main():
    #initialize values to add and tree
    insertions = [(5,2),(7,3),(15,5),(20,7),(25,4),(17,7),(32,10),(44,10),(48,3),(50,5),(62,21),
                  (78,29),(88,6),(62,40),(90,7)]
    deletions = [32, 88, 90]

    avl = AVLTreeMap()

    #insert and print output
    for key, value in insertions:
        avl[key] = value
        print(f'Inserted {value} at {key}. Tree height: {tree_height(avl)}')

    print('Tree after insertions:')
    print_tree(avl)

    #delete and print output
    for key in deletions:
        del avl[key]
        print(f'Deleted key {key}. Tree height: {tree_height(avl)}')

    print('Tree after deletions:')
    print_tree(avl)

main()