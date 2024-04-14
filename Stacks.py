# Stack data structure

class Stack:
    def __init__(self):             # initialize the stack
        self.items = []
    def is_empty(self):             # check if the stack is empty
        return self.items == []
    def push(self, item):           # push item in the stack
        self.items.append(item)
    def pop(self):                  # delete the last item in the stack
        return self.items.pop()
    def peek(self):                 # peek the last item in the stack
        l = len(self.items)-1
        return self.items[l]
    def size(self):                 # size of the stack
        return len(self.items)
    
stack = Stack()
print(stack.is_empty()) 

for i in range(0, 10):
    stack.push(i)
    
print(stack.size())

peek = stack.peek()
print(peek)

pop = stack.pop()
print(pop)

print(stack.items)