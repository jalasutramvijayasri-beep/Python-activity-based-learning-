# 03-Hospital-Billing.py
# Case-03: Hospital Billing System

print("="*60)
print("      HOSPITAL BILLING SYSTEM - CASE 03")
print("="*60)

patient_name = input("Enter Patient Name: ")
patient_id = input("Enter Patient ID: ")
disease = input("Enter Disease/Department: ")
days = int(input("Enter No. of Days Admitted: "))
room_type = input("Enter Room Type (General/Private/ICU): ").lower()

print("\n" + "-"*60)
print(f"Patient: {patient_name} | ID: {patient_id}")
print(f"Disease: {disease} | Days: {days} | Room: {room_type}")
print("-"*60)

# Room Charges per day
if room_type == "general":
    room_charge = 1000
elif room_type == "private":
    room_charge = 3000
elif room_type == "icu":
    room_charge = 7000
else:
    room_charge = 1000
    print("Invalid Room Type! Taking General as default")

# Other Charges
doctor_fee = 2000
lab_fee = float(input("Enter Lab Test Charges: "))
medicine_fee = float(input("Enter Medicine Charges: "))

room_total = room_charge * days
sub_total = room_total + doctor_fee + lab_fee + medicine_fee

# Discount based on days
if days > 10:
    discount = sub_total * 0.10
elif days > 5:
    discount = sub_total * 0.05
else:
    discount = 0

total_bill = sub_total - discount
gst = total_bill * 0.05
final_bill = total_bill + gst

print("\n--- BILL BREAKDOWN ---")
print(f"Room Charges ({days} x {room_charge}) : Rs.{room_total}")
print(f"Doctor Fee                 
