class abc:
    def __init__(self,d):
        self.b=d
    a = 10
    def abcd(self):
        print("hello",self.a,self.b)
ob = abc(20)
ob.abcd()