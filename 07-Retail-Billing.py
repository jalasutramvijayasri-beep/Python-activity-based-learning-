# 07-Retail-Billing.py
# Case 7: Retail Billing with Multiple Discount Rules

print("="*60)
print("  RETAIL BILLING WITH DISCOUNT RULES - CASE 07")
print("="*60)

n = int(input("Enter No. of Products: "))
items = [] # nested list

# Category tax - Tuple
# (category, tax%)
categories = [("Grocery", 5), ("Electronics", 18), ("Clothing", 12)]

total = 0
for i in range(n):
    print(f"\nProduct {i+1}:")
    name = input("  Name: ")
    qty = int(input("  Quantity: "))
    price = float(input("  Price: Rs."))
    print("  Category: 1-Grocery 2-Electronics 3-Clothing")
    cat_choice = int(input("  Choose: "))
    cat_name, tax_rate = categories[cat_choice-1]
    
    amount = qty * price
    items.append([name, qty, price, cat_name, tax_rate, amount])
    total += amount

print("\n" + "-"*60)
for name, qty, price, cat, tax, amt in items:
    print(f"{name} ({cat}) x{qty} = Rs.{amt} + Tax {tax}%")

print("-"*60)
print(f"Sub Total: Rs.{total:.2f}")

# Threshold Discount
if total > 10000:
    discount = total * 0.15
    max_concession = 2000
elif total > 5000:
    discount = total * 0.10
    max_concession = 1000
else:
    discount = 0
    max_concession = 0

# Maximum concession limit
if discount > max_concession:
    discount = max_concession

print(f"Discount: -Rs.{discount:.2f}")

# Tax calculation using loop
total_tax = 0
for name, qty, price, cat, tax_rate, amt in items:
    tax_amt = (amt - discount/len(items)) * tax_rate / 100
    total_tax += tax_amt

final = total - discount + total_tax
print(f"Tax: +Rs.{total_tax:.2f}")
print(f"FINAL BILL: Rs.{final:.2f}")
print("="*60)
