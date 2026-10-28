# 02-Electricity-Bill.py
# Case-02: Electricity Bill Calculation

print("="*50)
print("   ELECTRICITY BILL CALCULATOR - CASE 02")
print("="*50)

customer_name = input("Enter Customer Name: ")
customer_id = input("Enter Customer ID: ")
units = float(input("Enter Units Consumed: "))

print("\n" + "-"*50)
print(f"Customer: {customer_name} | ID: {customer_id}")
print(f"Units Consumed: {units}")
print("-"*50)

# Rate Calculation (Telangana Slab)
if units <= 100:
    amount = units * 4.5
    rate = 4.5
elif units <= 200:
    amount = (100 * 4.5) + (units - 100) * 6.5
    rate = 6.5
elif units <= 300:
    amount = (100 * 4.5) + (100 * 6.5) + (units - 200) * 8.0
    rate = 8.0
else:
    amount = (100 * 4.5) + (100 * 6.5) + (100 * 8.0) + (units - 300) * 9.5
    rate = 9.5

# Additional Charges
fixed_charge = 100
if amount > 5000:
    surcharge = amount * 0.05
else:
    surcharge = 0

total_bill = amount + fixed_charge + surcharge

print(f"\nEnergy Charge : Rs.{amount:.2f}")
print(f"Fixed Charge  : Rs.{fixed_charge}")
print(f"Surcharge     : Rs.{surcharge:.2f}")
print("-"*50)
print(f"TOTAL BILL    : Rs.{total_bill:.2f}")
print("="*50)

if
