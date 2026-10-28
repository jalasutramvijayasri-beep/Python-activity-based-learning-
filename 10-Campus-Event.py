# 10-Campus-Event.py
# Case 10: Campus Event Budgeting and Resource Planning

print("="*70)
print("    CAMPUS EVENT BUDGETING AND RESOURCE PLANNING - CASE 10")
print("="*70)

# Input
event_name = input("Enter Event Name: ")
event_days = int(input("Enter Number of Event Days: "))
expected_audience = int(input("Enter Expected Audience: "))

# Venue Tuple (venue, per_day_cost, capacity)
venues = [
    ("Auditorium", 10000, 500),
    ("Open Ground", 15000, 1000),
    ("Seminar Hall", 5000, 200),
    ("Classroom", 2000, 60)
]

print("\nAvailable Venues:")
for i, (name, cost, cap) in enumerate(venues, 1):
    print(f"  {i}. {name} - Rs.{cost}/day | Capacity: {cap}")

venue_choice = int(input("Choose Venue (1-4): "))
venue_name, venue_cost_per_day, venue_capacity = venues[venue_choice-1]

total_venue_cost = venue_cost_per_day * event_days

# Resources - Nested List [resource, quantity, unit_price, total]
resources = []

print("\n--- Resources Planning ---")
num_resources = int(input("Enter Number of Resource Types: "))

total_resource_cost = 0
for i in range(num_resources):
    print(f"\nResource {i+1}:")
    r_name = input("  Enter Resource Name (Sound/Stage/Lights/Food): ")
    r_qty = int(input("  Enter Quantity: "))
    r_price = float(input("  Enter Price per Unit: Rs."))
    r_total = r_qty * r_price
    total_resource_cost += r_total
    resources.append([r_name, r_qty, r_price, r_total])
    print(f"  -> Cost: Rs.{r_total:.2f}")

# Staff / Volunteers
print("\n--- Staff Cost ---")
num_staff = int(input("
