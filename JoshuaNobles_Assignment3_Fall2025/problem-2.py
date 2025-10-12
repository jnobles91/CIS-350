class Queue():

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
    
    def peek(self):
        #return next item in queue
        return self.front.data
    
    def get_size(self):
        return self.size
    
    def isempty(self):
        return self.size == 0
    
spooler = Queue()
#initiate queue and add in jobs

spooler.enqueue('homework.doc')
spooler.enqueue('study_guide.pdf')
spooler.enqueue('report.xlsx')

#check size and next items

print(f'Items in queue: {spooler.get_size()}') #expected 3
print(f'Front item: {spooler.peek()}') #expected homework.doc

#process first 2 jobs

print(f'Processing Job: {spooler.dequeue()}') #expected homework.doc
print(f'Processing Job: {spooler.dequeue()}') #expected study_guide.pdf

#add 2 more jobs

spooler.enqueue('cat_photo.jpg')
spooler.enqueue('owners_manual.pdf')

#check size and front again

print(f'Items in queue: {spooler.get_size()}') #expected 3
print(f'Front item: {spooler.peek()}') #expected report.xlsx

#process all jobs

print(f'Processing Job: {spooler.dequeue()}') #expected report.xlsx
print(f'Processing Job: {spooler.dequeue()}') #expected cat_photo.jpg
print(f'Processing Job: {spooler.dequeue()}') #expected owners_manual.pdf

#check if queue is empty and make sure theres no error trying to dequeue from an empty spooler

print(f'Is spooler empty: {spooler.isempty()}')
print(f'Processing Job: {spooler.dequeue()}')


        