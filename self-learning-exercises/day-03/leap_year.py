# Leap Year Checker
# Date: October 26, 2024
# Determines if a given year is a leap year

print("=== Leap Year Checker ===")
print()

year = int(input("Enter a year: "))

# Leap year logic:
# Divisible by 4 AND (not divisible by 100 OR divisible by 400)

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a LEAP YEAR! 🎉")
        else:
            print(f"{year} is NOT a leap year.")
    else:
        print(f"{year} is a LEAP YEAR! 🎉")
else:
    print(f"{year} is NOT a leap year.")

print()
print("Leap year rules:")
print("- Divisible by 4: Usually a leap year")
print("- EXCEPT if divisible by 100: Not a leap year")
print("- EXCEPT if divisible by 400: IS a leap year")
print()
print("Examples:")
print("2024: Leap year (divisible by 4)")
print("2100: NOT leap year (divisible by 100, not by 400)")
print("2000: Leap year (divisible by 400)")