# Pizza Order System
# Date: October 26, 2024
# Calculate pizza order cost with multiple options

print("=== Pizza Order System ===")
print()
print("Welcome to Python Pizza Deliveries!")
print()

# Get order details
size = input("What size pizza? (S/M/L): ").upper()
pepperoni = input("Add pepperoni? (Y/N): ").upper()
extra_cheese = input("Add extra cheese? (Y/N): ").upper()

# Initialize bill
bill = 0

# Size pricing
if size == "S":
    bill += 15
    print("Small pizza: $15")
elif size == "M":
    bill += 20
    print("Medium pizza: $20")
elif size == "L":
    bill += 25
    print("Large pizza: $25")
else:
    print("Invalid size!")

# Pepperoni pricing
if pepperoni == "Y":
    if size == "S":
        bill += 2
        print("Pepperoni (small): $2")
    else:
        bill += 3
        print("Pepperoni (M/L): $3")

# Extra cheese pricing
if extra_cheese == "Y":
    bill += 1
    print("Extra cheese: $1")

# Display total
print()
print(f"Total bill: ${bill}")
print("Thank you for your order! 🍕")