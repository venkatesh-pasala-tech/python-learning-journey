# Day 1 - Python Basics Practice
# Date: October 24, 2024
# Course: Jose Portilla - Complete Python Bootcamp
# Topics: input(), print(), variables

print("=== Day 1 Practice Programs ===")
print()

# Program 1: Simple greeting
print("Program 1: Greeting")
name = input("What's your name? ")
print("Hello, " + name + "!")
print("Welcome to Python programming!")
print()

# Program 2: Age calculator
print("Program 2: Age Calculator")
birth_year = input("What year were you born? ")
current_year = 2024
age = current_year - int(birth_year)
print("You are approximately " + str(age) + " years old!")
print()

# Program 3: Favorite things
print("Program 3: Favorite Things")
color = input("What's your favorite color? ")
food = input("What's your favorite food? ")
print("So you like " + color + " and " + food + "!")
print("That's awesome!")
print()

# Program 4: Simple calculator (addition)
print("Program 4: Simple Calculator")
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
result = int(num1) + int(num2)
print("The sum is: " + str(result))

print()
print("=== Day 1 Complete! ===")