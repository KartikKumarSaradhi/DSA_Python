class Stack:
    def _init_(self, max):
        self.stack = [None] * max
        self.top = -1
        self.max = max

    def push(self, data):
        if self.top >= self.max:
            print("overflow")
            return
        self.top += -1
        self.stack[self.top] = data

    def pop(self):
        if self.top < 0:
            print("under flow")
            return
        data = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= -1
        return data

    def display(self):
        temp = self.top
        while temp >= 0:
            print(self.stack[temp])
            temp -= 1


ob = Stack(5)
while True:
    n = int(input("press 1 to push\n2 to pop\n3 to display"))
    if n == 1:
        data = int(input("enter the data"))
        ob.push(data);
        print(data, "is pushed")
    elif n == 2:
        print(ob.pop(), "is poped")
    elif n == 3:
        ob.display()
    else:
        break
