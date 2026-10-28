# 01-Scholarship.py

name = input("Enter Name: ")
percentage = float(input("Enter Percentage: "))
income = float(input("Enter Family Income: "))
attendance = float(input("Enter Attendance: "))

if percentage >= 75 and income <= 200000 and attendance >= 75:
    print(f"\n{name} is ELIGIBLE")
    if percentage >= 90:
        print("Amount: Rs.50000")
    elif percentage >= 80:
        print("Amount: Rs.30000")
    else:
        print("Amount: Rs.15000")
else:
    print(f"\n{name} is NOT ELIGIBLE")
