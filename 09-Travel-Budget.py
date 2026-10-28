# 09-Travel-Budget.py
# Case 09: Travel Budget Planner

print("=== TRAVEL BUDGET PLANNER - CASE 09 ===")

trip = input("Enter Destination: ")
days = int(input("Enter Days: "))
people = int(input("Enter People: "))

# Expenses - Nested List
expenses = []

# Tuple for transport rates (mode, multiplier)
transport = [("Bus", 1.0), ("Train", 1.5), ("Flight", 3.0)]

print("\nTransport: 1-Bus 2-Train 3-Flight")
choice = int(input("Choose Transport: "))
mode, mult = transport[choice-1]

travel_cost = float(input("Enter Base Travel Cost per Person: ")) * mult * people
expenses.append(["Travel", travel_cost])

hotel = float(input("Enter Hotel Cost per Day: ")) * days
expenses.append(["Hotel", hotel])

food = float(input("Enter Food Cost per Day per Person: ")) * days * people
expenses.append(["Food", food])

activities_cost = float(input("Enter Activities Total Cost: "))
expenses.append(["Activities", activities_cost])

misc = float(input("Enter Misc Cost: "))
expenses.append(["Misc", misc])

# Total using loop
total = 0
print("\n--- BREAKDOWN ---")
for name, cost in expenses:
    print(f"{name}: Rs.{cost:.2f}")
    total += cost

print(f"\nTotal Budget: Rs.{total:.2f}")
print(f"Per Person: Rs.{total/people:.2f}")

# Budget Check - Conditional
limit = float(input("\nEnter Your Budget Limit: "))
if total <= limit:
    print(f"✅ Within Budget! Save Rs.{limit-total:.2f}")
else:
    print(f"❌ Over Budget by Rs.{total-limit:.2f}")
    print("Reduce hotel or activities!")

print("=== Happy Journey! ===")
