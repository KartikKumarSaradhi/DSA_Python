def search(list,index,target):
    if(index == len(list)):
        print("Not Found")
    elif(target == list[index]):
        print("Element found at pos = ",index)
    else:
        return search(list,index+1,target)
    
list = [1, 5, 3, 6, 7, 8, 0]
target = 10
search(list,0,target)
    