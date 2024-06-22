def handed(entry_door, rail):
    if(entry_door == 'front'):
        if(rail == '1'):
            return 'Left-Handed'
        else:
            return 'Right-Handed'
    elif(entry_door == 'rear'):
        if(rail == '1'):
            return 'Right-Handed'
        else:
            return 'Left-Handed'
    else:
        return 'Wrong Information'
    
entry_door = input("From which door did he enter? Front or Rear")
rail = (int(input("Which rail did he held? 1 or 2")))

x = handed(entry_door, rail)
print(x)