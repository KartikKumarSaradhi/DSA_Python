month = int(input("Enter the month number"))
cost = float(input("Enter the rent"))
days = float(input("Enter no of days"))
rent = 0.0
if(month > 3 and month <7) or (month > 10 and month <= 12):
    rent = (rent + cost + (0.20*cost)) * days
else:
    rent = (rent + cost) * days

print("%.2f"%rent)