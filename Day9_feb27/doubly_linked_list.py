class Node:
    def __init__(self, d):
        self.data = d
        self.next = None
        self.prev = None
    
class List:
    def __init__(self):
        self.head = None
    
    def insert(self, d):
        newnode = Node(d)
        if (self.head == None):
            self.head = newnode
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newnode
            newnode.prev = temp
    
    def display(self):
        temp = self.head
        while temp!=None :
            print(temp.data, end=" <=> ")
            temp = temp.next
        print("None")

    def reverse_display(self):
        temp = self.head
        while temp.next:
            temp = temp.next
        
        while temp:
            print(temp.data, end=" <=> ")
            temp = temp.prev
        print("None")


ob = List()
ob.insert(10)
ob.insert(20)
ob.insert(30)
ob.insert(40)
ob.display()
ob.reverse_display()
