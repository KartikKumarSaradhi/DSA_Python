row = int(input("Enter no of rows"))
column = int(input("Enter no of columns"))
tree = int(input("Enter the position"))

# if(tree <= column or tree%column==0 or tree%column==1):
#   print("Mango Tree")
# else:
#   print("Orange Tree")

if(tree%column==1 or tree%column<=row or tree> column*row-column ):
    print("Mango Tree")
else:
    print("Orange Tree")