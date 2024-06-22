def util(matrix,r,c):
    for i in range(c):
        if(matrix[r][i] == 1):
            return False
    for i,j in zip(range(r,-1,-1),range(c,-1,-1)):
        if(matrix[i][j] == 1):
            return False
    
    for i,j in zip(range(r,4),range(c,-1,-1)):
        if(matrix[i][j] == 1):
            return False
    return True
    
        

def solution(matrix,c):
    if(c >= 4):
        return True
    for i in range(0,4):
        if(util(matrix,i,c) == True):
            matrix[i][c] = 1
            if solution(matrix,c):
                return True
        matrix[i][c] = 0
    return False



matrix = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
solution(matrix,0)
for i in range(4):
    for j in range(4):
        if(matrix[i][j] == 1):
            x=1
        else:
            print()