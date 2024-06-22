def safe(box,r,c):
    for i in range(0,c):
        if box[r][i] == 1:
            return False
    for i,j in zip(range(r,-1,-1), range(c,-1,-1)):
        if(box[i][j] == 1):
            return False
    for i,j in zip(range(r,4), range(c,-1,-1)):
        if(box[i][j] == 1):
            return False
    return True

def solution(box,c):
    if c>3:
        return True
    for r in range(0,4):
        if safe(box,r,c) == True :
            box[r][c] = 1
            if(solution(box,c+1) == True):
                return True
            solution[r][c] = 0
    return False


box = [[1,1,1,1,1],
       [1,0,0,1,0],
       [1,1,0,0,1],
       [0,1,1,1,1]]
solution(box,0)
for i in range(0,4):
    for j in range(0,4):
        print(box[i][j],end=' ')
    print()