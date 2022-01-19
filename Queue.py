class queue:
    def __init__(self, size):
        self.front = 0
        self.rear = 0
        self.queue = [None] * size
        self.size = size + 1
        
    def current_size(self):
        print(self.rear - self.front)
        
    def isempty(self):
        if self.rear - self.front == 0:
            print("True")
        else:
            print("False")
            
    def first(self):
        print(self.queue[self.front])
    
    def enqueue(self, value):
        if self.rear == self.size - 1:
            print("Queue is Full")
        elif self.rear == 0:
            self.queue[self.rear] = value
            self.rear += 1
        else:
            self.queue[self.rear] = value
            self.rear = (self.rear + 1) % self.size
            
    def dequeue(self):
        if self.front == self.size - 1:
            print("Queue is Empty")
        else:
            self.queue[self.front] = None
            self.front += 1
            
    def display(self):
        for i in range(self.front, self.rear - 1):
            print(self.queue[i], end = " ")
        print(self.queue[self.rear - 1])
        
 
size = int(input("Enter the size of the Queue:- "))
q = queue(size)
q.enqueue(0)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.display()
q.enqueue(5)
q.dequeue()
q.display()
q.dequeue()
q.first()
q.dequeue()
q.display()
