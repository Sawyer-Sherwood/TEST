name = input("Name: ").strip().capitalize()
snack = input("Snack: ").strip().title()
price = float(input("Price: ").strip())
quantity = int(input("Quantity: ").strip())

subtotal = price * quantity
discount = subtotal * 0.10 if subtotal >= 10.00 else 0.00
final_total = subtotal - discount

print("####OUTPUT####")
print(f"Customer: {name}")
print(f"Snack: {snack}")
print(f"Quantity: {quantity}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Discount: ${discount:.2f}")
print(f"Final total: ${final_total:.2f}")

