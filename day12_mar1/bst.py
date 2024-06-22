class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def getnode(self,data):
        newnode = Node(data)
        return newnode
    
    def insert(self,root,data):
        if( root == None):
            newnode = ob.getnode(data)
            return newnode
        elif(data < root.data):
            root.left = ob.insert(root.left,data)
        elif(data > root.data):
            root.left = ob.insert(root.right,data)
        return root
    
    def display(self,root):
        if(root == None):
            return
        ob.display(root.left)
        print(root.data)
        ob.display(root.right)

    def depth(self,root):
        if root == None :
            return 0
        else:
            if(ob.depth(root.left) > ob.depth(root.right)):
                return 1 + ob.depth(root.left)
            else:
                return 1 + ob.depth(root.right)
            
    def level(self,root):
        if root == None:
            return 
        h = ob.depth(root)
        for i in range(1, h+1):
            print(" "*(h-i), end='')
            ob.levelprint(root,i)
            print()
    
    def levelprint(self,root,level):
        if(root == None):
            return
        elif level == 1:
            print(root.data,end=" ")
        else:
            ob.levelprint(root.left,level-1)
            ob.levelprint(root.right,level-1)

    def binary(self,root,min,max):
        if(root==None):
            return True
        if(root.data>max and root.data<min):
            return False
        else:
            return ob.binary(root.left,min,root.data) and ob.binary(root.right,root.data,max)



            



ob = Tree()
root = None
root = ob.insert(root,2)
root = ob.insert(root,1)
root = ob.insert(root,3)
ob.display()
