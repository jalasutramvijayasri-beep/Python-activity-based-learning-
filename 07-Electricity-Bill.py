# Case 07 - Retail Billing with Multiple Discount Rules
# Using only syllabus: variables, loops, conditionals, lists, tuples, unpacking

# Product catalog: (Product Name, Price per unit, Tax %)
products = [
    ("RICE", 60, 5),
    ("WHEAT", 45, 5),
    ("OIL", 120, 12),
    ("SOAP", 35, 18),
    ("SUGAR", 50, 8)
]

print("----- Retail Billing System -----")
print("Available Products: RICE, WHEAT, OIL, SOAP, SUGAR")

n = int(input("Enter number of items: "))

bill_items = [] # nested list: [name, qty, amount, tax, discount, final]
total_invoice = 0

for i in range(n):
    print(f"\nItem {i+1}")
    p_name = input("Enter product name: ").upper()
    qty = int(input("Enter quantity: "))

    if qty <= 0:
        print("Invalid qty! Skipping")
        continue

    # Find product details using tuple unpacking
    found = False
    for prod_name, prod_price, prod_tax in products:
        if prod_name == p_name:
            price = prod_price
            tax_per = prod_tax
            found = True
            break

    if not found:
        print("Product not in catalog! Skipping")
        continue

    # 1. Amount
    amount = price * qty

    # 2. Quantity-based discount rules
    if qty >= 10:
       
