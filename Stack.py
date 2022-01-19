class stack:
    def __init__(self, size):
        self.top = 0
        self.size = size
        self.stack = [None] * size
    
    def push(self, value):
        if self.top == self.size :
            print("Stack is FULL")
        else:
            self.stack[self.top] = value
            self.top += 1
    def pop(self):
        self.top -= 1
        if self.top == 0:
            print("Stack is EMPTY")
        else:
            self.stack[self.top] = None
    
    def display(self):
        for i in range(self.top - 1):
            print(self.stack[i], end = " ")
        print(self.stack[self.top - 1])
        
size = 3
s = stack(size)
s.push(0)
s.push(1)
s.push(2)
s.push(3)
s.display()
s.pop()
s.display()
s.push(3)
s.display()
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
