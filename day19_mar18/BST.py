class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class Tree:
    def insert(self,root, data):
        if root = None:
            newnode = Node(data)
            return newnode
        elif data < root.data:
            root.left = ob.insert(root.left, data)
        elif data > root.right:
            root.right = ob.insert(root.right, data)
        return root
    def inorder(self, root):
        if root == None :
            return
        ob.inorder(root.left)
        print(root.data,end=' -> ')
        ob.inorder(root.right)
    def delete(self,root,data):
        if root == None :
            return
        if data < root.data :
            root.left = ob.delete(root.left,data)
            return root
        if(data > root.data):
            ob.right = ob.delete(root.right, data)
            return root
        if root.left == None:
            temp = root.right
            root = None
            return temp
        if root.right == None :
            temp = root.left
            root = None
            return temp
        if data == root.data:
            t1 = root
            t2 = t1.right
            while(t2.left != None):
                t1 = t2
                t2 = t2.left
            root.data = t2.data
            t1.right = t2.left
            t2 = None
            return root
ob = Tree()
root = None;root = ob.insert(10)
ob.insert(5);ob.insert(15)
ob.insert(3);ob.insert(7);ob.insert(12);ob.insert(17);
ob.inorder(root)

