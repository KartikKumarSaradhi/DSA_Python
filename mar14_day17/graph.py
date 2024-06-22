class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Graph:
    def __init__(self,v):
        self.vertex = v
        self.graph = [None]*v
    def insert(self,s,d):
        newNode = Node(d)
        if(self.graph[s] == None):
            self.graph[s] = newNode
        else:
            temp = self.graph[s]
            while(temp.next != None):
                temp = temp.next
            temp.next = newNode
    def printgraph(self):
        for i in range(0,self.vertex):
            temp = self.graph[i];print(i,end="->")
            while(temp != None):
                print(temp.data,end=' ')
                temp = temp.next
            print()

    def dfs(self,v,visited = Node):
        if(visited == Node):
            visited = [None]*self.vertex
        print(v,end="->")
        visited[v] = 1
        temp = self.graph[v]
        while(temp!= None):
            if(visited[temp.data] == None):
                ob.dfs(temp.data,visited)
            temp = temp.next

ob = Graph(4)
ob.insert(0,1);ob.insert(0,2);ob.insert(0,3)
ob.insert(1,2)
ob.insert(3,0)
ob.printgraph()
ob.dfs(0)