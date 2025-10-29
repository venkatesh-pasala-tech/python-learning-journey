# Day 3 - Control Flow and Logical Operators
# Date: October 26, 2024
# Course: Jose Portilla - Complete Python Bootcamp
# Topics: if/elif/else, comparison operators, logical operators

print("=== Day 3 Practice Programs ===")
print()

# Program 1: Basic If-Else
print("Program 1: Basic If-Else")
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult!")
else:
    print("You are a minor.")
print()

# Program 2: If-Elif-Else
print("Program 2: If-Elif-Else (Grade Calculator)")
score = int(input("Enter your test score (0-100): "))

if score >= 90:
    print("Grade: A - Excellent!")
elif score >= 80:
    print("Grade: B - Good job!")
elif score >= 70:
    print("Grade: C - Satisfactory")
elif score >= 60:
    print("Grade: D - Need improvement")
else:
    print("Grade: F - Failed")
print()

# Program 3: Comparison Operators
print("Program 3: Comparison Operators")
num1 = 10
num2 = 20

print(f"{num1} > {num2}: {num1 > num2}")
print(f"{num1} < {num2}: {num1 < num2}")
print(f"{num1} == {num2}: {num1 == num2}")
print(f"{num1} != {num2}: {num1 != num2}")
print(f"{num1} >= 10: {num1 >= 10}")
print(f"{num2} <= 20: {num2 <= 20}")
print()

# Program 4: Logical Operators (AND)
print("Program 4: Logical Operators - AND")
age = 25
has_license = True

if age >= 18 and has_license:
    print("You can drive!")
else:
    print("You cannot drive.")
print()

# Program 5: Logical Operators (OR)
print("Program 5: Logical Operators - OR")
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("It's the weekend! 🎉")
else:
    print("It's a weekday. Time to work!")
print()

# Program 6: Logical Operators (NOT)
print("Program 6: Logical Operators - NOT")
is_raining = False

if not is_raining:
    print("Great weather for a walk!")
else:
    print("Better stay inside.")
print()

# Program 7: Nested Conditionals
print("Program 7: Nested Conditionals")
age = int(input("Enter age: "))
height = int(input("Enter height in cm: "))

if age >= 12:
    if height >= 120:
        print("You can ride the rollercoaster! 🎢")
    else:
        print("You're old enough but too short. Sorry!")
else:
    print("You're too young to ride.")
print()

# Program 8: Multiple Conditions
print("Program 8: Multiple Conditions (Ticket Pricing)")
age = int(input("Enter your age: "))

if age < 12:
    ticket_price = 5
    print(f"Child ticket: ${ticket_price}")
elif age <= 18:
    ticket_price = 10
    print(f"Youth ticket: ${ticket_price}")
elif age < 65:
    ticket_price = 15
    print(f"Adult ticket: ${ticket_price}")
else:
    ticket_price = 7
    print(f"Senior ticket: ${ticket_price}")
print()

# Program 9: Combining Logical Operators
print("Program 9: Complex Logic")
age = 25
income = 50000
credit_score = 720

# Loan approval logic
if (age >= 21 and age <= 65) and (income >= 30000) and (credit_score >= 650):
    print("Loan APPROVED! ✅")
else:
    print("Loan DENIED. ❌")

    # Explain why
    if age < 21 or age > 65:
        print("Reason: Age not in eligible range")
    if income < 30000:
        print("Reason: Income too low")
    if credit_score < 650:
        print("Reason: Credit score too low")
print()

# Program 10: Odd or Even
print("Program 10: Odd or Even Checker")
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is EVEN")
else:
    print(f"{number} is ODD")
print()

print("=== Day 3 Practice Complete! ===")