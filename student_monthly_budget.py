income = int(input("enter income: "))
rent = int(input("enter rent expenses: "))
food = int(input("enter food expenses: "))
transport = int(input("enter transport expenses: "))
data = int(input("enter data expenses: "))

total_expenses = rent + data + transport + food
money_remaining = income - total_expenses

print("Total expenses: ",total_expenses)
print("Money remaining: ",money_remaining)
