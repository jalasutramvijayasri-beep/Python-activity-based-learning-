# Case 10 - Campus Event Financial Planning & Profitability
# Syllabus only: variables, operators, if-else, loops, lists, tuples, unpacking

print("----- Campus Event Financial Planning -----")

# 1. Inputs - Fixed Costs
print("--- Fixed Costs ---")
venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
publicity = float(input("Enter publicity cost: "))
transport = float(input("Enter transport cost: "))

# 2. Inputs - Variable Cost Per Person
print("\n--- Variable Costs Per Person ---")
catering = float(input("Enter catering cost per person: "))
certificate = float(input("Enter certificate & kit cost per person: "))
sitting = float(input("Enter sitting/other per person: "))

# 3. Participants & Income
participants = int(input("\nEnter expected number of participants: "))
reg_fee = float(input("Enter registration fee per person: "))
sponsorship = float(input("Enter sponsorship amount: "))
target_profit = float(input("Enter target profit %: "))

if participants <= 0 or reg_fee < 0:
    print("Invalid input!")
else:
    # 4. Calculations
    fixed_cost = venue + equipment + publicity + transport
    var_per_person = catering + certificate + sitting
    total_variable = var_per_person * participants
    total_cost = fixed_cost + total_variable

    total_reg_income = reg_fee * participants
    total_income = total_reg_income + sponsorship

    profit = total_income - total_cost

    if total_cost > 0:
        profit_per = profit * 100 / total_cost
    else:
        profit_per = 0

    # Per person break-up
    print(f"\n--- Cost Breakup ---")
    print(f"Fixed Cost: Rs.{fixed_cost:.2f}")
    print(f"Variable Cost ({var_per_person} x {participants}): Rs.{total_variable:.2f}")
    print(f"Total Cost: Rs.{total_cost:.2f}")
    print(f"Cost Per Participant: Rs.{total_cost / participants:.2f}")

    print(f"\n--- Income Breakup ---")
    print(f"Registration Income: Rs.{total_reg_income:.2f}")
    print(f"Sponsorship: Rs.{sponsorship:.2f}")
    print(f"Total Income: Rs.{total_income:.2f}")

    # 5. Profitability Status
    print(f"\n--- Profitability Report ---")
    print(f"Profit: Rs.{profit:.2f} ({profit_per:.2f}%)")

    if profit_per >= target_profit:
        print(f"Status: MEETS Target Profit {target_profit}%")
    elif profit >= 0:
        print(f"Status: Below Target but in Profit")
    else:
        print(f"Status: LOSS - Need more funds")

    # 6. Break-even Analysis
    margin_per_person = reg_fee - var_per_person
    print(f"\n--- Break-Even Analysis ---")
    print(f"Margin Per Person (Fee - Variable): Rs.{margin_per_person:.2f}")

    if margin_per_person <= 0:
        print("Cannot break-even! Registration fee is less than variable cost per person")
        print(f"Minimum fee required: Rs.{var_per_person + 1:.2f}")
    else:
        # Fixed - Sponsorship = need from participants margin
        needed_from_reg = fixed_cost - sponsorship
        if needed_from_reg <= 0:
            print("Already break-even with sponsorship alone!")
            min_participants = 0
        else:
            min_participants = needed_from_reg / margin_per_person
            # Round up
            if min_participants != int(min_participants):
                min_participants = int(min_participants) + 1
            else:
                min_participants = int(min_participants)
            
            print(f"Minimum Participants Needed for Break-Even: {min_participants}")
            
            if participants >= min_participants:
                print(f"Current {participants} is sufficient for break-even")
            else:
                print(f"Need {min_participants - participants} more participants")

    # 7. Shortfall Handling
    if profit < 0:
        shortfall = -profit
        print(f"\nShortfall Amount: Rs.{shortfall:.2f}")
        extra_fee_needed = shortfall / participants
        print(f"To cover loss, increase fee by Rs.{extra_fee_needed:.2f} per person")
        print(f"New Suggested Fee: Rs.{reg_fee + extra_fee_needed:.2f}")

print("\n----- End of Planning -----")
