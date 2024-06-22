x = float(input("Enter the total cost :- "))
y = float(input("Enter the cost of each banana :- "))

nb = 12.00

status = x - (y*12)

if(status > 0):
    print("Loss = ",status)
else:
    print("Profit =",status)