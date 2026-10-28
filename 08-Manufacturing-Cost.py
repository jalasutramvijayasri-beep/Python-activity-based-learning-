# Case 08 - Manufacturing Cost and Profitability Report

print("----- Manufacturing Cost Calculator -----")
n = int(input("Enter number of products: "))

product_list = [] # nested list

for i in range(n):
    print(f"\nProduct {i+1}")
    name = input("Enter product name: ")
    material = float(input("Enter material cost: "))
    labour = float(input("Enter labour charges: "))
    wastage_per = float(input("Enter wastage %: "))
    machine = float(input("Enter machine & overhead cost: "))
    units = int(input("Enter number of units produced: "))
    selling_price = float(input("Enter selling price per unit: "))
    target_profit = float(input("Enter profit target %: "))

    if material < 0 or labour < 0 or units <= 0:
        print("Invalid input! Skipping")
        continue

    # 1. Wastage cost
    wastage_cost = material * wastage_per / 100

    # 2. Total manufacturing cost
    total_material_cost = material + wastage_cost
    total_production_cost = total_material_cost + labour + machine

    # 3. Cost per unit
    cost_per_unit = total_production_cost / units

    # 4. Profit calculation
    total_selling = selling_price * units
    total_profit = total_selling - total_production_cost

    if total_production_cost > 0:
        profit_per = total_profit * 100 / total_production_cost
    else:
        profit_per = 0

    # 5. Profitability status
    if profit_per >= target_profit:
        status = "MEETS Target"
    elif profit_per >= 0:
        status = "Below Target but Profit"
    else:
        status = "LOSS"

    print(f"\n--- Profit Report for {name} ---")
    print(f"Material + Wastage ({wastage_per}%): {total_material_cost:.2f}")
    print(f"Total Production Cost: {total_production_cost:.2f}")
    print(f"Cost Per Unit: {cost_per_unit:.2f}")
    print(f"Selling Total: {total_selling:.2f}")
    print(f"Profit: {total_profit:.2f} ({profit_per:.2f}%)")
    print(f"Status: {status}")

    product_list.append([name, total_production_cost, cost_per_unit, total_profit, profit_per, status])

# Final Summary
print("\n===== Manufacturing Summary Report =====")
total_cost_all = 0
total_profit_all = 0

for p in product_list:
    p_name, p_total_cost, p_unit_cost, p_profit, p_per, p_status = p
    print(f"{p_name} | Cost Rs.{p_total_cost:.2f} | Unit Rs.{p_unit_cost:.2f} | Profit {p_per:.2f}% | {p_status}")
    total_cost_all = total_cost_all + p_total_cost
    total_profit_all = total_profit_all + p_profit

print(f"\nTotal Products: {len(product_list)}")
print(f"Overall Production Cost: Rs.{total_cost_all:.2f}")
print(f"Overall Profit: Rs.{total_profit_all:.2f}")

# Most profitable product
if product_list:
    best = product_list[0]
    for p in product_list:
        if p[4] > best[4]: # compare profit %
            best = p
    print(f"\nMost Profitable: {best[0]} with {best[4]:.2f}% profit")
