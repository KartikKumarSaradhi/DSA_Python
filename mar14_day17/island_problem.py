def solution(list1, x, y):
    if x < 0 or x > 4 or y < 0 or y > 4 or list[x][y] == 0:
        return
    list[x][y] = 0
    solution(list, x, y + 1)
    solution(list, x + 1, y)


list1 = [[0, 1, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [1, 0, 0, 0, 0],
        [1, 0, 0, 1, 1],
        [1, 0, 0, 1, 1]]
count = 0

for i in range(5):
    for j in range(5):
        if list[i][j] == 1:
            count += 1
            solution(list, i, j)
