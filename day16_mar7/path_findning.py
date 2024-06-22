def solution(box,sol,x,y):
    if x == 3 and y == 0 and box[x][y] == 1:
        return True
    if safe(box,x,y) == True:
        sol[x][y] =1
        if solution(box,x+1,y) == True:
            return True
        if solution(box,x,y+1) == True:
            return True
        sol[x][y] = 0
        return False
    return False

def safe(box,x,y):
    if x >= 0 and x <= 4 and y>=0 and y<=4 and box[x] == 1:
        return True
    return False


    
    
box = [[1,1,1,1,1,1],
       [1,0,0,1,0],
       [1,1,0,0,1],
       [0,1,1,1,1]]

sol = [[0,0,0,0,0,0],
       [0,0,0,0,0,0],
       [0,0,0,0,0,0],
       [0,0,0,0,0,0]]
solution(box,sol,0,4)
for i in range(0,4):
    for j in range(0,4):
        print(sol[i][j],end=" ")
print()