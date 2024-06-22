x=1
z=20
for i in range(1,5):
    for j in range(i):
        print(" ",end=' ')
    for k in range(i,5):
        print(+x,end='*')
        x= x+1
    
    for y in range(1,5):
        if(x>10 and x<=20):
            for w in range(5,y,-1):
                print(x,end='*')
                x=x+1
    print()