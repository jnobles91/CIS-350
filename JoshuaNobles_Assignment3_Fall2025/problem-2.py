class Queue():
    class Node():
        def __init__(self,data,prev = None , next = None):
            self.data = data
            self.prev = prev
            self.next = next

    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0

    def enqueue(self, data):
        self.size += 1
        item = self.Node(data,self.back)
        if self.front == None:
            self.front = item
            self.back = item
        else:
            self.back.next = item
            self.back = item
    
    def dequeue(self):
        if self.size == 0:
            return None
        temp = self.front
        self.front = temp.next
        if self.front == None:
            self.back = None
        self.size -= 1
        return temp.data
    
    def peek(self):
        return self.front.data
    
    def get_size(self):
        return self.size
    
    def isempty(self):
        return self.size == 0
    
spooler = Queue()

spooler.enqueue('homework.doc')
spooler.enqueue('study_guide.pdf')
spooler.enqueue('report.xlsx')

print(f'Items in queue: {spooler.get_size()}') #expected 3
print(f'Front item: {spooler.peek()}') #expected homework.doc

print(f'Processing Job: {spooler.dequeue()}') #expected homework.doc
print(f'Processing Job: {spooler.dequeue()}') #expected study_guide.pdf

spooler.enqueue('cat_photo.jpg')
spooler.enqueue('owners_manual.pdf')

print(f'Items in queue: {spooler.get_size()}') #expected 3
print(f'Front item: {spooler.peek()}') #expected report.xlsx

print(f'Processing Job: {spooler.dequeue()}') #expected report.xlsx
print(f'Processing Job: {spooler.dequeue()}') #expected cat_photo.jpg
print(f'Processing Job: {spooler.dequeue()}') #expected owners_manual.pdf

print(f'Is spooler empty: {spooler.isempty()}')
print(f'Processing Job: {spooler.dequeue()}')


        