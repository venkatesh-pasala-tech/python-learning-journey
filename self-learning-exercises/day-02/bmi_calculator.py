# BMI Calculator
# Date: October 25, 2024
# Calculate Body Mass Index from height and weight

print("=== BMI Calculator ===")
print()

# Get user input
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Display result
print(f"\nYour BMI is: {bmi:.2f}")

# Interpret BMI
if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal weight")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")

print("\nBMI Ranges:")
print("Underweight: < 18.5")
print("Normal: 18.5 - 24.9")
print("Overweight: 25 - 29.9")
print("Obese: >= 30")