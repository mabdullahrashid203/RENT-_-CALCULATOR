print("===== Rent Calculator =====")

rent = float(input("Enter total house rent: "))
food = float(input("Enter total food expenses: "))
electricity = float(input("Enter total electricity bill: "))
water = float(input("Enter total water bill: "))
internet = float(input("Enter internet bill: "))

people = int(input("Enter number of people: "))

total_expenses = rent + food + electricity + water + internet
per_person = total_expenses / people

print("\n===== Expense Summary =====")
print(f"Total Rent: {rent:.2f}")
print(f"Food Expenses: {food:.2f}")
print(f"Electricity Bill: {electricity:.2f}")
print(f"Water Bill: {water:.2f}")
print(f"Internet Bill: {internet:.2f}")
print(f"Total Expenses: {total_expenses:.2f}")
print(f"Each Person Has To Pay: {per_person:.2f}")