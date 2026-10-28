# Case 05 - Multi-Plan Telecommunications Cost Optimization

# Plans as tuples: (Plan Name, Rent, Free Data GB, Free Calls min, Free SMS, Validity)
# Using tuple operations and unpacking
plans = [
    ("PLAN_BASIC_199", 199, 2, 100, 50, 28),
    ("PLAN_STANDARD_399", 399, 5, 300, 100, 56),
    ("PLAN_PREMIUM_599", 599, 10, 500, 200, 84),
    ("PLAN_UNLIMITED_799", 799, 20, 1000, 300, 84)
]

# Rate for excess usage - tuple
rates = (20, 1.0, 1.0)  # Data per GB, Call per min, SMS per sms
data_rate, call_rate, sms_rate = rates  # unpacking

print("----- Telecom Cost Optimization -----")
used_data = float(input("Enter data used in GB: "))
used_calls = float(input("Enter calls used in minutes: "))
used_sms = float(input("Enter SMS used: "))
need_validity = int(input("Enter required validity days: "))
budget = float(input("Enter your budget Rs: "))

# Validation
if used_data < 0 or used_calls < 0 or used_sms < 0:
    print("Invalid! Usage cannot be negative")
else:
    results = []  # nested list

    print("\n--- Plan Evaluation ---")
    for plan in plans:
        p_name, p_rent, p_free_data, p_free_calls, p_free_sms, p_validity = plan

        # 1. Validity constraint
        if p_validity < need_validity:
            print(f"{p_name}: REJECTED - Validity {p_validity} < {need_validity}")
            continue

        # 2. Excess charges calculation
        excess_data = used_data - p_free_data if used_data > p_free_data else 0
        excess_calls = used_calls - p_free_calls if used_calls > p_free_calls else 0
        excess_sms = used_sms - p_free_sms if used_sms > p_free_sms else 0

        excess_cost = (excess_data * data_rate) + (excess_calls * call_rate) + (excess_sms * sms_rate)
        total_cost = p_rent + excess_cost

        # 3. Budget constraint
        if total_cost <= budget:
            status = "ELIGIBLE"
        else:
            status = "OVER BUDGET"

        print(f"{p_name} | Total Rs.{total_cost:.2f} (Rent {p_rent} + Excess {excess_cost:.2f}) - {status}")
        
        # Store in nested list
        results.append([p_name, total_cost, status, excess_cost])

    # 4. Identify most economical eligible plan
    print("\n===== FINAL RESULT =====")
    best_cost = 999999
    best_plan_name = ""

    for r in results:  # loop through nested list
        name, total, status, excess = r
        if status == "ELIGIBLE" and total < best_cost:
            best_cost = total
            best_plan_name = name

    if best_plan_name != "":
        print(f"Most Economical Eligible Plan: {best_plan_name}")
        print(f"Total Cost: Rs.{best_cost:.2f} within budget Rs.{budget}")
    else:
        print("No eligible plan found within your budget and validity!")
        print("Suggestion: Increase budget or reduce usage.")
