def soe(list, index, sume, sumo):
    if index == len(list):
        return [sume, sumo]
    
    elif list[index] % 2 == 0:
        sume += list[index]
    else:
        sumo += list[index]
    
    return soe(list, index + 1, sume, sumo)

list = [1, 5, 3, 6, 7, 8, 0]
index = 0
sume = 0
sumo = 0
print(soe(list, index, sume, sumo))
