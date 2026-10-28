# Case 03 - Hospital Billing
policy = [("SENIOR", 20), ("CHILD", 15), ("BPL", 30), ("GENERAL", 0)]

def get_concession(category):
    for cat, percent in policy:
        if cat == category:
            return percent
    return 0

print("Hospital Billing System")
n = int(input("Enter number of patients: "))
all_patients = []

for i in range(n):
    name = input("Enter patient name: ")
    age = int(input("Enter age: "))
    cat = input("Enter category GENERAL/SENIOR/CHILD/BPL: ").upper()
    if age >= 60: cat = "SENIOR"
    elif age <= 12: cat = "CHILD"
    
    cons = float(input("Consultation charge: "))
    diag = float(input("Diagnostic charge: "))
    treat = float(input("Treatment charge: "))
    pay = input("Payment type CASH/INSURANCE: ").upper()

    if cons < 0 or diag < 0 or treat < 0:
        print("Invalid charges! Skipping")
        continue

    total_before = cons + diag + treat
    concession = total_before * get_concession(cat) / 100
    total_after = total_before - concession

    if total_after > 50000:
        cls = "HIGH COST - NEEDS CLAIM"
    elif total_after > 20000:
        cls = "MEDIUM COST"
    else:
        cls = "LOW COST"

    print(f"Total: Rs.{total_after:.2f}, Class: {cls}")
    all_patients.append([name, cat, total_after, cls])

print("\nFinal Report")
for name, cat, total, cls in all_patients:
    print(f"{name} | {cat} | {total} | {cls}")
