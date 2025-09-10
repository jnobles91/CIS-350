class DNode:
    def __init__(self, ele=None):
        self.ele = ele
        self.left = None
        self.right = None


class DLinkedList:
    def __init__(self):
        self.header = DNode()
        self.trailer = DNode()
        self.header.right = self.trailer
        self.trailer.left = self.header

    def empty(self):
        return self.header.right == self.trailer and self.trailer.left == self.header

    def front(self):
        return self.header.right.ele

    def back(self):
        return self.trailer.left.ele

    def addBefore(self, v, e):
        u = DNode(e)
        u.right = v
        u.left = v.left
        v.left.right = u
        v.left = u

    def addFront(self, e):
        self.addBefore(self.header.right, e)

    def remove(self, v):
        u = v.left
        w = v.right
        u.right = w
        w.left = u

        

    def printList(self):
        temp = self.header.right
        if temp == self.trailer:  # List is empty if header's right points to trailer
            print("List is empty")
            return

        while temp != self.trailer:
            print(temp.ele)
            temp = temp.right

if __name__ == "__main__":
    if __name__ == "__main__":
    # Initialize a DLinkedList object
    list = DLinkedList()

    print("--- 1. Testing on an empty list ---")
    print(f"Is the list empty: {list.empty()}")
    print("List contents:")
    list.printList()  # Should print "List is empty"
    print("Attempting to remove from an empty list...")
    list.removeFront()   # Should handle gracefully
    list.removeBack()    # Should handle gracefully
    print()

    print("--- 2. Populating the list ---")
    print("Adding elements: SFO, PVD (front) and JFK, BOS (back)")
    list.addFront("PVD")
    list.addFront("SFO")
    list.addBack("JFK")
    list.addBack("BOS")

    print("Current list:")
    list.printList()
    print(f"Front element: {list.front()}")
    print(f"Back element: {list.back()}")
    print(f"Is the list empty: {list.empty()}")
    print()

    print("--- 3. Testing find() function ---")
    # Note: The find function should print its own message as per instructions
    list.find("PVD")  # Element in the middle
    list.find("SFO")  # First element
    list.find("BOS")  # Last element
    list.find("MIA")  # Non-existent element
    print()

    print("--- 4. Testing insert_after() function ---")
    print("Inserting 'BWI' after 'PVD'...")
    list.insert_after("PVD", "BWI")
    print("List after insertion:")
    list.printList()

    print("Attempting to insert 'MIA' after non-existent 'LAX'...")
    list.insert_after("LAX", "MIA")
    print("List remains:")
    list.printList()
    print()

    print("--- 5. Testing reverse() function ---")
    print("Reversing the list...")
    list.reverse()
    print("List after reverse:")
    list.printList()
    print(f"New front element: {list.front()}")
    print(f"New back element: {list.back()}")
    print()

    print("--- 6. Testing removeFront() and removeBack() ---")
    print("Removing from front...")
    list.removeFront()
    print("List after removeFront:")
    list.printList()

    print("Removing from back...")
    list.removeBack()
    print("List after removeBack:")
    list.printList()
    print()

    print("--- 7. Emptying the list ---")
    list.removeBack()
    list.removeBack()
    list.removeBack()
    print("List after removing all elements:")
    list.printList()
    print(f"Is the list empty: {list.empty()}")
