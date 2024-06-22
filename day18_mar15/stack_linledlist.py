ob = Stack(5)
while(True):
    n = int(input("press 1 to push\n2 to pop\n3 to display"))
    if n ==1:
        data = int(input("enter the data"))
        ob.push(data);
        print(data," is pushed")
    elif(n==2):
        print(ob.pop()," is poped")
    elif n==3:
        ob.display()
    else:
        break



