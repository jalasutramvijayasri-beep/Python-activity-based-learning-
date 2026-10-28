# 08-Manufacturing-Cost.py
# Case 08: Manufacturing Cost Calculator with Raw Material and Labor

print("="*65)
print("  MANUFACTURING COST CALCULATOR - CASE 08")
print("="*65)

product_name = input("Enter Product Name: ")
num_materials = int(input("Enter Number of Raw Materials: "))

# Raw Materials - Nested List
materials = []

# (material_id, rate_per_kg) - Tuple for rate slab
rate_slab = [(1, 50), (2, 120), (3, 200)]  # just for demo

total_material_cost = 0

for i in range(num_materials):
    print(f"\n--- Raw Material {i+1} ---")
    name = input("  Enter Material Name: ")
    quantity = float(input("  Enter Quantity (kg): "))
    price_per_kg = float(input("  Enter Price per kg: Rs."))
    
    cost = quantity * price_per_kg
    total_material_cost += cost
    
    # Store as nested list [name, qty, price, cost]
    materials.append([name, quantity, price_per_kg, cost])
    print(f"  -> {name} Cost = Rs.{cost:.2f}")

print("\n--- Labor Details ---")
num_workers = int(input("Enter Number of Workers: "))
hours_per_worker = float(input("Enter Working Hours per Worker: "))
wage_per_hour = float(input("Enter Wage per Hour: Rs."))

total_labor_cost = num_workers * hours_per_worker * wage_per_hour

# Machine & Overhead - Tuple unpacking
overhead_data
