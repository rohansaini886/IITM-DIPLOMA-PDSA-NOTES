class Queue:
    def __init__(self, queue = []):
        self.queue = queue
        
    def enqueue(self, queue, value):
        self.queue += [value]
        
    def dequeue(self, queue):
        self.queue = self.queue[1:] 
    
    def display(self, queue):
        print(self.queue)
        
        
    
q = Queue()
queue = []
q.enqueue(queue, 0)
q.enqueue(queue, 1)
q.enqueue(queue, 2)
q.enqueue(queue, 3)
q.display(queue)
q.dequeue(queue)
q.dequeue(queue)
q.display(queue)
