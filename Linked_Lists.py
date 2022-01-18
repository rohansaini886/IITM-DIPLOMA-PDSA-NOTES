class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None
    def isempty(self):
        if self.head == None:
            return True
        else:
            return False
    def append(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = Node(data)
    def delete(self, v):
        if self.isempty()==True:
            return 'List is empty'
        # if list have only one element and equal to v
        elif self.head.next==None:
            if self.head.data==v:
                self.head = None
            else:
                return('Not exist')
        else:
            temp = self.head
            temp1 = self.head
            while temp.next!= None and temp.data != v:
                temp1 = temp
                temp = temp.next
            if temp.data==v and temp==self.head:
                self.head = temp.next
            elif temp.data==v:
                temp1.next= temp.next
            else:
                return('Not exist')
    def display(self):
        if self.isempty()==True:
            return('None')
        else:
            temp = self.head
            while temp!=None:
                print(temp.data)
                temp = temp.next
                
l = linkedList()
l.isempty()
l.append(0)
l.append(1)
l.append(2)
l.display()
l.delete(2)
l.delete(1)
l.display()
l.delete(0)
l.isempty()
