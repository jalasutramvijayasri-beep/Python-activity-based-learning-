# Case 09 - Multi-Currency Travel Budget Analysis

# Exchange rates (Currency, INR Rate)
exchange_rates = [
    ("USD", 83.50),
    ("EUR", 90.20),
    ("GBP", 105.00),
    ("AED", 22.70)
]

print("----- Travel Budget Calculator -----")
budget = float(input("Enter total budget in INR: "))
n = int(input("Enter number of expenses: "))

expenses = [] # nested list
total = 0

for i in range(n):
    print(f"\nExpense {i+1}")
    cat = input("Enter category (food/travel/stay/shopping): ")
    amt = float(input("Enter amount: "))
    curr = input("Enter currency (USD/EUR/GBP/AED/INR): ").upper()

    # Find rate
    rate = 1.0
    for code, r in exchange_rates:
        if code == curr:
            rate = r
            break

    fee = amt * 0.02 # 2% conversion fee
    inr_val = (amt + fee) * rate

    print(f"{cat}: {amt} {curr} + 2% Fee = Rs.{inr_val:.2f}")
    
    expenses.append([cat, amt, curr, inr_val])
    total = total + inr_val

# Report
print("\n===== Budget Report =====")
for e in expenses:
    c, a, cu, iv = e # unpacking
    print(f"{c} | {a} {cu} = Rs.{iv:.2f}")

print(f"\nBudget: Rs.{budget:.2f} | Spent: Rs.{total:.2f}")

if total > budget:
    print(f"OVER BUDGET by Rs.{total-budget:.2f}")
else:
    print(f"UNDER BUDGET by Rs.{budget-total:.2f}")

# Largest expense
if expenses:
    large = expenses[0]
    for e in expenses:
        if e[3] > large[3]:
            large = e
    print(f"Largest Expense: {large[0]} - Rs.{large[3]:.2f}")
