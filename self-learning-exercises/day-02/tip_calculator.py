# Tip Calculator
# Date: October 25, 2024
# Calculate tip and split bill among multiple people

print("=== Tip Calculator ===")
print()

# Get input
bill = float(input("What was the total bill? $"))
tip_percent = int(input("What percentage tip would you like to give (10, 12, or 15)? "))
people = int(input("How many people to split the bill? "))

# Calculate
tip_amount = bill * (tip_percent / 100)
total_bill = bill + tip_amount
per_person = total_bill / people

# Display results
print()
print(f"Bill amount: ${bill:.2f}")
print(f"Tip ({tip_percent}%): ${tip_amount:.2f}")
print(f"Total bill: ${total_bill:.2f}")
print(f"Each person pays: ${per_person:.2f}")