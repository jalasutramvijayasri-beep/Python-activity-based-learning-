# Case 02 - Progressive Electricity Billing
# Using only: variables, data types, loops, conditionals, lists, nested lists, tuples, unpacking

def calculate_bill(units):
    # Slabs using tuples and unpacking
    slabs = [(100, 1.5), (100, 2.5), (100, 4.0)]
    remaining = units
    energy = 0.0

    for limit, rate in slabs:
        if remaining <= 0:
            break
        use_units = limit if remaining > limit else remaining
        energy = energy + use_units * rate
        remaining = remaining - use_units

    if remaining > 0:
        energy = energy + remaining * 6.0

    # Fixed charges, surcharges, rebates
    fixed = 50.0
    
    if energy > 1000:
        surcharge = energy * 0.10
    else:
        surcharge = 0.0

    if units < 100:
        rebate = 25.0
    else:
        rebate = 0.0

    total = energy + fixed + surcharge - rebate
    return energy, fixed, surcharge, rebate, total
