# Case 06 - Railway Fare with Distance and Class Rules

# Distance slabs (limit, rate) - tuples
slabs = [(100, 2.0), (200, 1.5), (99999, 1.0)]

# Class list: (ClassName, Multiplier) - tuples
classes = [
    ("GENERAL", 1.0),
    ("SLEEPER", 1.5),
    ("AC_3TIER", 2.5),
    ("AC_2TIER", 3.5),
    ("AC_FIRST", 5.0)
]

print("----- Railway Fare Calculator -----")
n = int(input("Enter number of passengers: "))

passenger_list = [] # nested list

for i in range(n):
    print(f"\nPassenger {i+1}")
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    dist = float(input("Enter distance km: "))
    t_class = input("Enter class (GENERAL/SLEEPER/AC_3TIER/AC_2TIER/AC_FIRST): ").upper()

    if age < 0 or dist <= 0:
        print("Invalid! Skipping")
        continue

    # Find class multiplier
    mult = 0
    found = False
    for c_name, c_mult in classes:
        if c_name == t_class:
            mult = c_mult
            found = True
            break
    if not found:
        print("Invalid class!")
        continue

    # Base fare calculation
    base = 0.0
    rem = dist
    for limit, rate in slabs:
        if rem <= 0:
            break
        if rem > limit:
            d = limit
        else:
            d = rem
        base = base + d * rate
        rem = rem - limit

    fare = base * mult

    # Age rule
    if age < 5:
        final = 0
        rule = "FREE <5"
