# Case 02 - Progressive Electricity Billing
# Roll No: 26001654

def calculate_bill(units):
    energy = 0
    rem = units

    if rem > 0:
        u = min(rem, 100)
        energy += u * 1.5
        rem -= u
    if rem > 0:
        u = min(rem, 100)
        energy += u * 2.5
        rem -= u
    if rem > 0:
        u = min(rem, 100)
        energy += u * 4.0
        rem -= u
    if rem > 0:
        energy += rem * 6.0

    fixed = 50
    surcharge = energy * 0.1 if energy > 1000 else 0
    rebate = 25 if units < 100 else 0
    total = energy + fixed + surcharge - rebate
    return total

# Main part
name = input("Enter Customer Name: ")
n = int(input("Enter No of Months: "))

bills = []
for i in range(n):
    month = input(f"Enter Month {i+1} Name: ")
    units = int(input(f"Enter Units for {month}: "))
    total = calculate_bill(units)
    print(f"{month} Bill: Rs.{total:.2f}")
    bills.append([month, units, total])

# Compare and find unusual increase
print("\n--- Comparison ---")
for m, u, t in bills:
    print(f"{m} - {u} units = Rs.{t:.2f}")

print("\n--- Unusual Increase (>30%) ---")
found = False
for i in range(1, len(bills)):
    prev = bills[i-1][2]
    curr = bills[i][2]
    if prev > 0:
        inc = (curr - prev) / prev * 100
        if inc > 30:
            print(f"{bills[i][0]} increased by {inc:.1f}% from {bills[i-1][0]}")
            found = True

if not found:
    print("No unusual increase")

print(f"\nHighest: Rs.{max([b[2] for b in bills]):.2f}")
print(f"Lowest: Rs.{min([b[2] for b in bills]):.2f}")
