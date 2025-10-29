# Day 3 - Control Flow and Logical Operators

**Date:** October 26, 2024  
**Duration:** [Your hours] hours  
**Course:** Jose Portilla - Complete Python Bootcamp

## 📚 Topics Learned

### 1. If-Else Statements

**Basic structure:**
```python
if condition:
    # Code runs if condition is True
else:
    # Code runs if condition is False
```

**Example:**
```python
age = 20
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

### 2. If-Elif-Else (Multiple Conditions)

**Structure:**
```python
if condition1:
    # Code for condition1
elif condition2:
    # Code for condition2
elif condition3:
    # Code for condition3
else:
    # Code if none above are True
```

**Example:**
```python
score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")
```

**Important:** Only ONE block executes (first True condition)

### 3. Comparison Operators

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `>`      | Greater than | `10 > 5` | True |
| `<`      | Less than | `10 < 5` | False |
| `==`     | Equal to | `10 == 10` | True |
| `!=`     | Not equal to | `10 != 5` | True |
| `>=`     | Greater than or equal | `10 >= 10` | True |
| `<=`     | Less than or equal | `5 <= 10` | True |

**Common mistake:** `=` vs `==`
- `=` is assignment: `x = 5` (store 5 in x)
- `==` is comparison: `x == 5` (check if x equals 5)

### 4. Logical Operators

#### AND (`and`)
**Both conditions must be True**
```python
age = 25
has_license = True

if age >= 18 and has_license:
    print("Can drive")  # Only prints if BOTH are True
```

**Truth table:**
```
True and True = True
True and False = False
False and True = False
False and False = False
```

#### OR (`or`)
**At least one condition must be True**
```python
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("Weekend!")  # Prints if EITHER is True
```

**Truth table:**
```
True or True = True
True or False = True
False or True = True
False or False = False
```

#### NOT (`not`)
**Reverses the condition**
```python
is_raining = False

if not is_raining:
    print("Go outside!")  # Prints because NOT False = True
```

**Truth table:**
```
not True = False
not False = True
```

### 5. Nested Conditionals

**If statements inside if statements:**
```python
age = 25
height = 150

if age >= 18:
    if height >= 140:
        print("You can ride!")
    else:
        print("Too short")
else:
    print("Too young")
```

**Can also be written with `and`:**
```python
if age >= 18 and height >= 140:
    print("You can ride!")
```

### 6. Combining Multiple Conditions

**Complex logic:**
```python
if (age >= 21 and age <= 65) and (income > 30000 or has_cosigner):
    print("Eligible")
```

**Use parentheses `()` to make logic clear!**

### 7. Common Patterns

#### Pattern 1: Range Check
```python
if 18 <= age <= 65:  # Pythonic way!
    print("Working age")
```

#### Pattern 2: Multiple Options
```python
if choice in ['Y', 'y', 'yes', 'Yes']:
    print("You said yes")
```

#### Pattern 3: Odd/Even Check
```python
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

## 💻 Projects Built

### 1. Leap Year Checker
**What it does:**
- Takes a year as input
- Determines if it's a leap year
- Explains the rules

**Leap year rules:**
1. If divisible by 4 → Usually leap year
2. EXCEPT if divisible by 100 → NOT leap year
3. EXCEPT if divisible by 400 → IS leap year

**Key concepts:**
- Nested if statements
- Modulus operator (%)
- Complex conditional logic

**Learning:** Real-world date/calendar logic

### 2. Pizza Order System
**What it does:**
- Takes size, pepperoni, cheese choices
- Calculates total price
- Different prices for different options

**Key concepts:**
- Multiple if statements
- Nested conditions (pepperoni price depends on size)
- Building up a total (bill += amount)

**Learning:** Real-world pricing logic, order systems

### 3. Love Calculator
**What it does:**
- Takes two names
- Counts specific letters
- Generates "compatibility" score
- Shows message based on score

**Key concepts:**
- String manipulation (.count())
- Combining conditions
- Multiple elif conditions
- String concatenation for numbers

**Learning:** String methods + conditionals together

### 4. Grade Calculator
**What it does:**
- Takes test score
- Assigns letter grade (A, B, C, D, F)
- Uses elif for multiple ranges

**Key concepts:**
- If-elif-else chain
- Range checking
- Proper ordering of conditions (highest first!)

**Learning:** Academic grading systems

## 🔑 Key Learnings

### Critical Concepts:

1. **Indentation Matters!**
```python
# Correct
if x > 5:
    print("Big")  # 4 spaces indent

# Wrong - will cause error
if x > 5:
print("Big")  # No indent
```

2. **Order Matters in elif!**
```python
# Wrong - will never reach elif!
if score >= 60:
    print("Pass")
elif score >= 90:  # Never reached because 90 >= 60!
    print("Excellent")

# Correct - highest first
if score >= 90:
    print("Excellent")
elif score >= 60:
    print("Pass")
```

3. **== vs =**
```python
x = 5      # Assignment (storing value)
x == 5     # Comparison (checking value)
```

4. **Boolean is True/False, not string**
```python
is_raining = True      # Correct - boolean
is_raining = "True"    # Wrong - string!
```

### Common Patterns Mastered:

✅ Basic if-else decisions
✅ Multiple options with elif
✅ Combining conditions with and/or
✅ Nested conditionals
✅ Range checking
✅ Odd/even detection
✅ Input validation

## 🐛 Challenges Faced

### Challenge 1: Indentation Errors
**Problem:** Forgot to indent after if statement
```python
# Wrong
if age >= 18:
print("Adult")  # IndentationError!
```

**Solution:** Always indent 4 spaces after `:`
```python
# Correct
if age >= 18:
    print("Adult")
```

### Challenge 2: Using = instead of ==
**Problem:** Used single = in condition
```python
if age = 18:  # SyntaxError!
```

**Solution:** Use == for comparison
```python
if age == 18:  # Correct
```

### Challenge 3: elif Order
**Problem:** Put conditions in wrong order

**Solution:** Always order from most specific to least specific (highest to lowest for numbers)

### Challenge 4: Logical Operator Confusion
**Problem:** Mixed up and/or logic

**Solution:** 
- AND = Both must be true
- OR = At least one must be true
- Test with simple examples

## ✅ Accomplishments

- ✅ Mastered if-elif-else statements
- ✅ Understood all comparison operators
- ✅ Learned logical operators (and, or, not)
- ✅ Built leap year checker (complex nested logic!)
- ✅ Created pizza ordering system
- ✅ Made love calculator (fun!)
- ✅ Applied conditionals in real projects
- ✅ Can now make programs that DECIDE! 🧠

## 💡 "Aha!" Moments

1. **Programs can now make decisions!** Before Day 3, programs just executed line by line. Now they can CHOOSE what to do!

2. **Order matters in elif!** Never thought about this - need to put most specific conditions first.

3. **Modulus (%) is super useful!** For checking divisibility, odd/even, patterns.

4. **Can combine conditions powerfully** with and/or to create complex logic.

## 🎯 Tomorrow's Goals (Day 4)

- Learn about lists (collections of items)
- Understand list indexing
- Learn list methods (append, remove, etc.)
- Random module for randomness
- Build programs with lists
- Continue Udemy course

## 💭 Reflection

Day 3 was mind-blowing! Programs can now make DECISIONS based on conditions. The leap year checker was challenging but felt amazing when it worked. Nested if statements are tricky but make sense. Logical operators (and, or, not) are super powerful. 

Starting to feel like a real programmer - my programs are getting smarter! The love calculator was fun and showed how you can combine string methods with conditionals.

**Feeling:** Excited and confident! Programs are becoming intelligent! 🧠

**Best moment:** When the leap year checker correctly handled all the edge cases (2000, 2100, 2024)!

**Quote of the day:** "Code is like humor. When you have to explain it, it's bad." - Cory House

---

**Day 3: COMPLETE ✅**  
**Streak: 3 days 🔥🔥🔥**  
**Total programs built: 13+**  
**Momentum: BUILDING! 🚀**
```

---

## 📦 COMMIT YOUR WORK (Ctrl+K → Commit and Push!)

### Commit Message:
```
Day 3: Control flow, logical operators, and decision-making programs

Topics learned:
- If, elif, else statements
- Comparison operators (>, <, ==, !=, >=, <=)
- Logical operators (and, or, not)
- Nested conditionals
- Boolean logic

Projects:
- Leap Year Checker - complex nested logic
- Pizza Order System - multi-option pricing
- Love Calculator - string + conditionals
- Grade Calculator - multiple conditions

Programs can now make DECISIONS! 🧠

Completed 10+ practice exercises and multiple projects.
```

**Steps:**
1. **Ctrl+K** (open commit dialog)
2. **Check all day-03 files**
3. **Paste commit message above**
4. **Click "Commit and Push"** ← Don't forget PUSH this time! 😊
5. **Verify on GitHub** → 3 GREEN SQUARES! 🟢🟢🟢

---

## 🎉 THREE-DAY STREAK ACHIEVED!

### Your Progress So Far:
```
Day 1: Variables, input, print ✅
Day 2: Data types, strings, math ✅
Day 3: Control flow, logic ✅

Combined Powers:
→ Can get user input
→ Can manipulate data
→ Can make decisions
→ Can build SMART programs! 🧠