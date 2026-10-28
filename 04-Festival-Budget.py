# 04-Festival-Budget.py
# Case-04: Festival Budget Planner

print("="*60)
print("     FESTIVAL BUDGET PLANNER - CASE 04")
print("="*60)

festival = input("Enter Festival Name: ")
budget = float(input("Enter Total Budget: Rs."))

print(f"\nFestival: {festival} | Total Budget: Rs.{budget}")
print("-"*60)

# Expenses Input
decoration = float(input("Enter Decoration Expense: Rs."))
food = float(input("Enter Food & Sweets Expense: Rs."))
clothing = float(input("Enter Clothing Expense: Rs."))
gifts = float(input("Enter Gifts Expense: Rs."))
others = float(input("Enter Other Expenses: Rs."))

total_expense = decoration + food + clothing + gifts + others
remaining = budget - total_expense

print("\n--- EXPENSE BREAKDOWN ---")
print(f"Decoration : Rs.{decoration} ({decoration/budget*100:.1f}%)")
print(f"Food       : Rs.{food} ({food/budget*100:.1f}%)")
print(f"Clothing   : Rs.{clothing} ({clothing/budget*100:.1f}%)")
print(f"Gifts      : Rs.{gifts} ({gifts/budget*100:.1f}%)")
print(f"Others     : Rs.{others} ({others/budget*100:.1f}%)")
print("-"*60)
print(f"Total Spent: Rs.{total_expense:.2f}")
print(f"Remaining  : Rs.{remaining:.2f}")

print("\n--- BUDGET STATUS ---")
if remaining > 0:
    print(f"✅ You Saved Rs.{remaining:.2f} - Great Planning!")
    if remaining > budget * 0.3:
        print("Tip: You can invest remaining amount!")
elif remaining == 0:
    print("⚖️ Budget Exactly Balanced!")
else:
    print(f"❌ Over
