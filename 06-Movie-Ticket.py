# 06-Movie-Ticket.py
print("=== MOVIE TICKET BOOKING ===")
movies = [("Avatar",150), ("Kalki",200), ("Pushpa",180)]
for i,(name,price) in enumerate(movies):
    print(f"{i+1}. {name} - Rs.{price}")
choice = int(input("Choose Movie: "))
qty = int(input("Tickets Qty: "))
name,price = movies[choice-1]
total = price*qty
if qty>=5:
    total *= 0.9
print(f"Total: Rs.{total} - Enjoy Movie!")
