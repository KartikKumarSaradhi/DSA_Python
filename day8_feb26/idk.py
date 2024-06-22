def abc(a):
    if(a==0):
        print(a)
    else:
        abc(a-1)
        abc(a-1)
        print(a)

abc(2)
