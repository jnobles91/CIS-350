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
    
    #find function
    def find(self,element):
        temp = self.header.right
        i = 0 #keep track of the index we're at since its not built into the linked list
        #start at the head and then iterate through it until you find the element or reach the end
        while temp != self.trailer:
            if temp.ele == element:
                print(f'{element} found at index {i}')
                return i
                #if you find the element return
            i +=1 #increment the index
            temp = temp.right #go to the next node
        return -1 #if we get to the end without finding return -1
    
    #insert after
    def insert_after(self,existing_element,new_element):
        temp = self.header.right
        #similar to find function we need to iterate through the list until we find the element we're looking for
        while temp.ele != existing_element and temp != self.trailer:
            temp = temp.right
        #return an error if we get to the end without finding the element we want to insert after
        if temp == self.trailer:
            print("That element isn't in the list")
        #else insert the new item
        else:
            new = DNode(new_element)
            new.left = temp #element we found in the list is to the left of our new item
            new.right = temp.right #item to the right of the old item is now to the right of our new item
            temp.right.left = new #element to the right of the element we are inserting after now points to the new element
            temp.right = new #old eleemtn is now to the left of our new element
    
    #reverse list
    def reverse(self):
        self.trailer.left, self.header.right = self.header.right, self.trailer.left #have the header and trailer point to the new front and back
        self.header.right.right = self.header #was pointing to trailer, now header
        self.trailer.left.left = self.trailer #was pointing to header, now trailer
        #there is probably a better way to do this proceeding step, but we're gonna go through and flip everything so I want to make sure everything
        #is pointing to the right spot at the end
        current = self.header.right #start at the new head
        while current != self.trailer:
            current.right, current.left = current.left, current.right
            current = current.right
    #add back
    def addBack(self,new_element):
        old_back = self.trailer.left
        new = DNode(new_element)
        new.left, old_back.right = old_back, new #old back is now to the left of new back
        self.trailer.left, new.right = new, self.trailer  #new node is now the back

    #remove back
    def removeBack(self):
        if self.empty() == False:
            old_back = self.trailer.left #new back will be the item to the left of the old back
            new_back = old_back.left
            self.trailer.left = new_back 
            new_back.right = self.trailer #have the new back point to nothing instead of the old trailer

    #remove front
    def removeFront(self):
        if self.empty() == False:
            old_front = self.header.right
            new_front = old_front.right
            self.header.right = new_front
            new_front.left = self.header


if __name__ == "__main__":
    if __name__ == "__main__":
    # Initialize a DLinkedList object
        lst= DLinkedList()

        print("--- 1. Testing on an empty list ---")
        print(f"Is the list empty: {lst.empty()}")
        print("List contents:")
        lst.printList()  # Should print "List is empty"
        print("Attempting to remove from an empty list...")
        lst.removeFront()   # Should handle gracefully
        lst.removeBack()    # Should handle gracefully
        print()

        print("--- 2. Populating the list ---")
        print("Adding elements: SFO, PVD (front) and JFK, BOS (back)")
        lst.addFront("PVD")
        lst.addFront("SFO")
        lst.addBack("JFK")
        lst.addBack("BOS")

        print("Current list:")
        lst.printList()
        print(f"Front element: {lst.front()}")
        print(f"Back element: {lst.back()}")
        print(f"Is the list empty: {lst.empty()}")
        print()

        print("--- 3. Testing find() function ---")
        # Note: The find function should print its own message as per instructions
        lst.find("PVD")  # Element in the middle
        lst.find("SFO")  # First element
        lst.find("BOS")  # Last element
        print(lst.find("MIA"))  # Non-existent element
        print()

        print("--- 4. Testing insert_after() function ---")
        print("Inserting 'BWI' after 'PVD'...")
        lst.insert_after("PVD", "BWI")
        print("List after insertion:")
        lst.printList()

        print("Attempting to insert 'MIA' after non-existent 'LAX'...")
        lst.insert_after("LAX", "MIA")
        print("List remains:")
        lst.printList()
        print()

        print("--- 5. Testing reverse() function ---")
        print("Reversing the list...")
        lst.reverse()
        print("List after reverse:")
        lst.printList()
        print(f"New front element: {lst.front()}")
        print(f"New back element: {lst.back()}")
        print()

        print("--- 6. Testing removeFront() and removeBack() ---")
        print("Removing from front...")
        lst.removeFront()
        print("List after removeFront:")
        lst.printList()

        print("Removing from back...")
        lst.removeBack()
        print("List after removeBack:")
        lst.printList()
        print()

        print("--- 7. Emptying the list ---")
        lst.removeBack()
        lst.removeBack()
        lst.removeBack()
        print("List after removing all elements:")
        lst.printList()
        print(f"Is the list empty: {lst.empty()}")
