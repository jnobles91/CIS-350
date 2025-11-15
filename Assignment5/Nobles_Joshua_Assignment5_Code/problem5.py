import random
import heapq
from time import time

#from previous homework, for quick sort
class LinkedQueue():

    class Node():
    #I'm using a linked list so we need a class for the node, with pointers for previous and next
        def __init__(self,data,prev = None , next = None):
            self.data = data
            self.prev = prev
            self.next = next


    def __init__(self):
    #keep track of the front node back node and size
        self.front = None
        self.back = None
        self.size = 0

    def __len__(self):
        return self.size

    def enqueue(self, data):
        #increment length
        self.size += 1
        item = self.Node(data,self.back)
        #previous is current back, next is none
        if self.front == None:
        #if queue is empty the new item is the front and back
            self.front = item
            self.back = item
        else:
        #else the item is the new back, point the current back to the new item
            self.back.next = item
            self.back = item
    
    def dequeue(self):
        if self.size == 0:
        #if theres nothing in the list return nothing
            return None
        temp = self.front
        self.front = temp.next
        #set the new front to the next item from the old front
        if self.front == None:
            #if list is now empty set both front and back to empty
            self.back = None
        #decrement size and return the old front
        self.size -= 1
        return temp.data
    
    def first(self):
        #return next item in queue
        return self.front.data
    
    def get_size(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0

#from book
def merge(S1, S2, S):
    i=j=0
    while i+j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i+j] = S1[i] # copy ith element of S1 as next item of S
            i += 1
        else:
            S[i+j] = S2[j] # copy jth element of S2 as next item of S
            j += 1

def merge_sort(S):
    n = len(S)
    if n < 2:
        return # list is already sorted
# divide
    mid = n // 2
    S1 = S[0:mid] # copy of first half
    S2 = S[mid:n] # copy of second half
    # conquer (with recursion)
    merge_sort(S1) # sort copy of first half
    merge_sort(S2) # sort copy of second half
# merge results
    merge(S1, S2, S) # merge sorted halves back into S

def _random_item(S):
    #get a random item of the linked list as a pivot so we don't hit stack overflow when using the sorted list
    k = random.randrange(len(S))
    cur = S.front
    for _ in range(k):
        cur = cur.next
    return cur.data

def quick_sort(S):
    """Sort the elements of queue S using the quick-sort algorithm."""
    n = len(S)
    if n < 2:
        return  # queue is already sorted

    # divide
    p = _random_item(S)  # use first element as an arbitrary pivot
    L = LinkedQueue()
    E = LinkedQueue()
    G = LinkedQueue()

    while not S.is_empty():  # divide S into L, E, and G
        if S.first() < p:
            L.enqueue(S.dequeue())
        elif p < S.first():
            G.enqueue(S.dequeue())
        else:  # S.first() equals pivot
            E.enqueue(S.dequeue())

    # conquer (with recursion)
    quick_sort(L)  # sort elements less than p
    quick_sort(G)  # sort elements greater than p

    # concatenate results back into S
    while not L.is_empty():
        S.enqueue(L.dequeue())
    while not E.is_empty():
        S.enqueue(E.dequeue())
    while not G.is_empty():
        S.enqueue(G.dequeue())

#heapsort using pythons built in heap module
def heap_sort(S):
    heapq.heapify(S)           
    sorted_array = []
    for i in range(len(S)):
        sorted_array.append(heapq.heappop(S))


def Generate_Array():
    array = []
    for i in range(5000):
        array.append(random.randint(-10000,10000))
    return array

def Generate_Sorted_Array():
    array = Generate_Array()
    array.sort()
    return array

def Generate_Reversed_Array():
    array = Generate_Array()
    array.sort(reverse=True)
    return array


rand_array = Generate_Array()
sorted_array = Generate_Sorted_Array()
reversed_array = Generate_Reversed_Array()

#merge sort
#random array
start_time= time( )
merge_sort(rand_array)
end_time = time( )
elapsed = end_time - start_time
print(f'Merge Sort, random array: {elapsed}')

#sorted array
start_time= time( )
merge_sort(sorted_array)
end_time = time( )
elapsed = end_time - start_time
print(f'Merge Sort, sorted array: {elapsed}')

#reversed array
start_time= time( )
merge_sort(reversed_array)
end_time = time( )
elapsed = end_time - start_time
print(f'Merge Sort, reverse array: {elapsed}')


#convert arrays to queues to work with quick sort from book
rand_array = Generate_Array()
sorted_array = Generate_Sorted_Array()
reversed_array = Generate_Reversed_Array()
random_ll = LinkedQueue()
sorted_ll = LinkedQueue()
reversed_ll = LinkedQueue()

for item in rand_array:
    random_ll.enqueue(item)

for item in sorted_array:
    sorted_ll.enqueue(item)

for item in reversed_array:
    reversed_ll.enqueue(item)


#quick sort
#random array
start_time= time( )
quick_sort(random_ll)
end_time = time( )
elapsed = end_time - start_time
print(f'Quick Sort, random array: {elapsed}')

#sorted array
start_time= time( )
quick_sort(sorted_ll)
end_time = time( )
elapsed = end_time - start_time
print(f'Quick Sort, sorted array: {elapsed}')

#reversed array
start_time= time( )
quick_sort(reversed_ll)
end_time = time( )
elapsed = end_time - start_time
print(f'Quick Sort, reverse array: {elapsed}')

rand_array = Generate_Array()
sorted_array = Generate_Sorted_Array()
reversed_array = Generate_Reversed_Array()

#random array
start_time= time( )
heap_sort(rand_array)
end_time = time( )
elapsed = end_time - start_time
print(f'Heap Sort, random array: {elapsed}')

#sorted array
start_time= time( )
heap_sort(sorted_array)
end_time = time( )
elapsed = end_time - start_time
print(f'Heap Sort, sorted array: {elapsed}')

#reversed array
start_time= time( )
heap_sort(reversed_array)
end_time = time( )
elapsed = end_time - start_time
print(f'Heap Sort, reverse array: {elapsed}')



