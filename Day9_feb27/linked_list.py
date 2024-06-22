class Node:
    def __init__(self, d):
        self.data = d
        self.next = None
    
class List:
    def __init__(self):
        self.head = None
    
    def insert(self, d):
        newnode = Node(d)
        if not self.head:
            self.head = newnode
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newnode
    
    def display(self):
        temp = self.head
        while temp!=None :
            print(temp.data, end=" => ")
            temp = temp.next
        print("None")


ob = List()
ob.insert(10)
ob.insert(20)
ob.insert(30)
ob.insert(40)
ob.display()
