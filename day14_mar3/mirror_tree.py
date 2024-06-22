class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def getNode(self,data):
        newNode = Node(data)
        return newNode
    
    def mirror(self,root1,root2):
        if(root1 == None and root2 == None):
            return True
        elif(root1 == None or root2 == None):
            return False
        elif(root1.data != root2.data):
            return False
        else:
            return (root1.left,root2.right) and ob.mirror(root1.right, root2.left)
        
    def BST(self,root,min,max):
        if(root == None):
            return None
        elif(root.data > max or root.data < min):
            return False
        else:
            return(root.left != None  and root.right1 = None) and BST(root.left, min,root.data) and BST(root.right,root.data,max)
        
ob = Tree()
root1 = None;root2 = None
root1 = ob.getNode(5)
root2 = ob.getNode(5)
root1.left = ob.getNode(6)
root2.right = ob.getNode(6)
