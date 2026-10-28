# Case 04 - Employee Payroll and Deduction Analysis

print("----- Employee Payroll System -----")
n = int(input("Enter number of employees: "))

# Nested list to store all employees
payroll = []

for i in range(n):
    print(f"\nEmployee {i+1}")
    name = input("Enter name: ")
    basic = float(input("Enter basic pay: "))
    hra = float(input("Enter HRA: "))
    da = float(input("Enter DA: "))
    ot_hours = float(input("Enter overtime hours: "))
    ot_rate = float(input("Enter overtime rate: "))
    incentive = float(input("Enter incentive: "))

    if basic < 0 or hra < 0 or da < 0:
        print("Invalid pay! Skipping")
        continue

    # Gross Salary
    ot_pay = ot_hours * ot_rate
    gross = basic + hra + da + ot_pay + incentive

    # Deductions
    pf = basic * 12 / 100

    # Progressive deduction
    if gross <= 10000:
        tax = 0
    elif gross <= 20000:
        tax = (gross - 10000) * 10 / 100
    elif gross <= 30000:
        tax = (10000 * 10 / 100) + (gross - 20000) * 15 / 100
    else:
        tax = (10000 * 10 / 100) + (10000 * 15 / 100) + (gross - 30000) * 20 / 100

    total_ded = pf + tax
    net = gross - total_ded

    if net >= 50000:
        grade = "HIGH EARNER"
    elif net >= 30000:
        grade = "MID EARNER"
    else:
        grade = "LOW EARNER"

    # Formatted Salary Statement
    print(f"\n--- Salary Slip for {name} ---")
    print(f"Gross: {gross:.2f}")
    print(f"PF: {pf:.2f}, Tax: {tax:.2f}")
    print(f"Total Deduction: {total_ded:.2f}")
    print(f"Net Salary: {net:.2f}")
    print(f"Grade: {grade}")

    payroll.append([name, gross, total_ded, net, grade])

print("\n===== Final Payroll Report =====")
for data in payroll:
    name, gross, ded, net, grade = data
    print(f"{name} | Gross: {gross} | Net: {net} | {grade}")
