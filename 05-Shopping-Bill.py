# 05-Shopping-Bill.py
# Case-05: Shopping Bill System - Correct Answer

print("="*60)
print("        SHOPPING BILL SYSTEM - CASE 05")
print("="*60)

customer_name = input("Enter Customer Name: ")
customer_id = input("Enter Customer ID: ")
num_items = int(input("Enter Number of Items: "))

print("-"*60)
total_amount = 0
items_list = []

for i in range(1, num_items + 1):
    print(f"\nItem {i}:")
    item_name = input(f"  Enter Item Name: ")
    quantity = int(input(f"  Enter Quantity: "))
    price = float(input(f"  Enter Price per Item: Rs."))
    
    item_total = quantity * price
    total_amount += item_total
    items_list.append((item_name, quantity, price, item_total))
    print(f"  -> {item_name} = Rs.{item_total:.2f}")

print("\n" + "="*60)
print("                BILL DETAILS
