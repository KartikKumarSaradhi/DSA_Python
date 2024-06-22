n = int(input())
a=3
b=2
for i in range(0,n):
    if(i%2==0):
        print(a,end=" ")
        a=a+4
    else:
        print(b,end=" ")
        b=b+1