# Queues data structure

class Queue:
    def __init__(self):             # initialize the queue
        self.items = []
    def is_empty(self):             # check if the queue is empty
        return self.items == []
    def enqueue(self, item):        # insert a new item from the left side of the queue 
        self.items.insert(0, item)
    def dequeue(self):              # delete the item from the right side of the queue 
        return self.items.pop()
    def size(self):
        return len(self.items)
    
queue = Queue()
print(queue.is_empty()) 

for i in range(0, 10):
    queue.enqueue(i)

print(queue.size())

pop = queue.dequeue()
print(pop)

print(queue.items)