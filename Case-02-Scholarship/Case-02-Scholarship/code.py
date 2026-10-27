# Case-02: University Scholarship Allocation - Priority Based
# Full Implementation

print("=== University Scholarship Allocation System (Case-02) ===")

eligible_students = []

num_students = int(input("Enter number of applicants: "))

for i in range(num_students):
    print(f"\n--- Applicant {i+1} ---")
    name = input("Enter student name: ")
    maths = int(input("Enter Maths marks (0-100): "))
    science = int(input("Enter Science marks (0-100): "))
    english = int(input("Enter English marks (0-100): "))
    attendance = int(input("Enter attendance percentage: "))
    income = int(input("Enter family annual income: "))
    
    aggregate = (maths + science + english) / 3
    
    # Eligibility Criteria
    if maths >= 50 and science >= 50 and english >= 50 and aggregate >= 75 and attendance >= 75 and income <= 300000:
        print(f"{name} -> Eligible! Aggregate: {aggregate:.2f}%")
        eligible_students.append([name, aggregate, attendance, income])
    else:
        print(f"{name} -> Not Eligible. Aggregate: {aggregate:.2f}%")

# Sorting Logic: Higher Aggregate First, If Same then Higher Attendance First
for i in range(len(eligible_students)):
    for j in range(0, len(eligible_students) - i - 1):
        if eligible_students[j][1] < eligible_students[j+1][1]:
            eligible_students[j], eligible_students[j+1] = eligible_students[j+1], eligible_students[j]
        elif eligible_students[j][1] == eligible_students[j+1][1]:
            if eligible_students[j][2] < eligible_students[j+1][2]:
                eligible_students[j], eligible_students[j+1] =
