# Love Calculator
# Date: October 26, 2024
# Calculate love compatibility score (just for fun!)

print("=== Love Calculator ===")
print()

name1 = input("Enter first name: ").lower()
name2 = input("Enter second name: ").lower()

# Combine names
combined = name1 + name2

# Count TRUE letters
true_count = 0
true_count += combined.count('t')
print(true_count)
true_count += combined.count('r')
print(true_count)
true_count += combined.count('u')
print(true_count)
true_count += combined.count('e')
print(true_count)

# Count LOVE letters
love_count = 0
love_count += combined.count('l')
print(love_count)
love_count += combined.count('o')
print(love_count)
love_count += combined.count('v')
print(love_count)
love_count += combined.count('e')
print(love_count)

# Calculate score
score = int(str(true_count) + str(love_count))

print()
print(f"Love Score: {score}")
print()

# Message based on score
if score < 10 or score > 90:
    print("Your love is like coke and mentos - explosive! 💥")
elif score >= 40 and score <= 50:
    print("You're alright together. 👍")
else:
    print("You make a good couple! ❤️")