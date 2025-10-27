# Day 2 - Data Types and String Manipulation
# Date: October 25, 2024
# Course: Jose Portilla - Complete Python Bootcamp
# Topics: Data types, string manipulation, type conversion

print("=== Day 2 Practice Programs ===")
print()

# Program 1: Data Types
print("Program 1: Data Types")
name = "Venkatesh"  # String
age = 35  # Integer
height = 5.9  # Float
is_learning = True  # Boolean

print(f"Name: {name} (type: {type(name)})")
print(f"Age: {age} (type: {type(age)})")
print(f"Height: {height} (type: {type(height)})")
print(f"Learning Python: {is_learning} (type: {type(is_learning)})")
print()

# Program 2: Type Conversion
print("Program 2: Type Conversion")
age_str = "35"
age_int = int(age_str)
age_float = float(age_str)

print(f"String: {age_str} (type: {type(age_str)})")
print(f"Integer: {age_int} (type: {type(age_int)})")
print(f"Float: {age_float} (type: {type(age_float)})")
print()

# Program 3: String Manipulation
print("Program 3: String Manipulation")
first_name = "venkatesh"
last_name = "pasala"

# Capitalize
print(f"Capitalized: {first_name.capitalize()} {last_name.capitalize()}")
# Upper case
print(f"Upper: {first_name.upper()}")
# Lower case
print(f"Lower: {first_name.lower()}")
# Title case
full_name = first_name + " " + last_name
print(f"Title: {full_name.title()}")
print()

# Program 4: F-strings (String Formatting)
print("Program 4: F-strings")
name = "Venkatesh"
age = 35
city = "Royersford"
print(f"My name is {name}, I'm {age} years old, and I live in {city}.")
print(f"Next year I'll be {age + 1} years old!")
print()

# Program 5: Mathematical Operations
print("Program 5: Math Operations")
num1 = 10
num2 = 3
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")  # Float division
print(f"{num1} // {num2} = {num1 // num2}")  # Integer division
print(f"{num1} % {num2} = {num1 % num2}")  # Modulus
print(f"{num1} ** {num2} = {num1 ** num2}")  # Power
print()

print("=== Day 2 Practice Complete! ===")