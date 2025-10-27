# Day 2 - Data Types and String Manipulation

**Date:** October 25, 2024  
**Duration:** [Your hours] hours  
**Course:** Jose Portilla - Complete Python Bootcamp

## 📚 Topics Learned

### 1. Data Types
- **String (str)** - Text data: `"hello"`
- **Integer (int)** - Whole numbers: `42`
- **Float** - Decimal numbers: `3.14`
- **Boolean (bool)** - True/False values

**Check type:**
```python
type(variable_name)  # Returns the data type
```

### 2. Type Conversion
- **int()** - Convert to integer
- **float()** - Convert to float
- **str()** - Convert to string
- **bool()** - Convert to boolean

**Examples:**
```python
age_str = "35"
age_int = int(age_str)  # Converts "35" to 35

price = 19.99
price_str = str(price)  # Converts 19.99 to "19.99"
```

### 3. String Manipulation
- **Concatenation:** `"Hello" + " " + "World"`
- **f-strings:** `f"My age is {age}"`
- **Methods:**
  - `.upper()` - UPPERCASE
  - `.lower()` - lowercase
  - `.capitalize()` - Capitalize first letter
  - `.title()` - Title Case Each Word
  - `.strip()` - Remove whitespace
  - `.replace()` - Replace characters

### 4. Mathematical Operations
```python
10 + 3   # Addition = 13
10 - 3   # Subtraction = 7
10 * 3   # Multiplication = 30
10 / 3   # Division = 3.333...
10 // 3  # Integer division = 3
10 % 3   # Modulus (remainder) = 1
10 ** 3  # Power = 1000
```

### 5. F-strings (Formatted Strings)
**Best way to format strings!**
```python
name = "Venkatesh"
age = 35
print(f"My name is {name} and I'm {age} years old")
print(f"Next year: {age + 1}")
```

## 💻 Projects Built

### 1. BMI Calculator
**What it does:**
- Takes weight (kg) and height (m) as input
- Calculates BMI = weight / (height²)
- Displays BMI category (Underweight/Normal/Overweight/Obese)

**Key concepts used:**
- Float input
- Mathematical operations (power)
- Conditional statements (if/elif/else)
- String formatting

**Learning:** Real-world application of math and data types

### 2. Tip Calculator
**What it does:**
- Takes bill amount, tip percentage, and number of people
- Calculates total with tip
- Splits bill equally among people
- Shows amount each person pays

**Key concepts used:**
- Float arithmetic
- Percentage calculations
- Division
- Formatted output (2 decimal places)

**Learning:** Practical financial calculation, rounding numbers

## 🔑 Key Learnings

### Important Concepts:
1. **Type matters!** - Can't do math with strings
2. **Convert before calculate** - Use int() or float() on input()
3. **F-strings are powerful** - Best way to format output
4. **Rounding:** Use `:.2f` in f-strings for 2 decimals

### Common Patterns:
```python
# Getting number input (IMPORTANT!)
age = int(input("Enter age: "))  # Convert to int immediately

# Formatting money
print(f"${amount:.2f}")  # Shows 2 decimal places

# String formatting with variables
print(f"Text {variable} more text {expression}")
```

## 🐛 Challenges Faced

### Challenge 1: Type Errors
**Problem:** Tried to calculate with string input
```python
# Wrong
age = input("Age: ")
next_year = age + 1  # ERROR! Can't add int to string
```

**Solution:** Convert immediately
```python
# Correct
age = int(input("Age: "))
next_year = age + 1  # Works!
```

### Challenge 2: Decimal Places
**Problem:** Calculator showing too many decimals (19.9999999)

**Solution:** Use f-strings with formatting
```python
print(f"${amount:.2f}")  # Shows exactly 2 decimals
```

### Challenge 3: Division Types
**Problem:** Confused about / vs //

**Solution:**
- `/` = Regular division (gives float): `10 / 3 = 3.333...`
- `//` = Integer division (gives int): `10 // 3 = 3`

## ✅ Accomplishments

- ✅ Mastered data types and type conversion
- ✅ Learned string manipulation methods
- ✅ Built BMI calculator from scratch
- ✅ Built tip calculator with proper formatting
- ✅ Understood f-strings and formatting
- ✅ Applied math operations in real projects

## 🎯 Tomorrow's Goals (Day 3)

- Learn about conditional statements (if/else) in depth
- Learn about comparison operators
- Learn about logical operators (and, or, not)
- Build decision-making programs
- Continue Udemy course

## 💭 Reflection

Excellent progress today! Data types make much more sense now. The projects were fun and practical. BMI and tip calculators are things I could actually use. F-strings are SO much better than concatenation with +. Excited to learn conditionals tomorrow!

**Feeling:** Confident and motivated! 🔥

**Best moment:** When the tip calculator worked perfectly and split the bill correctly!

**Quote of the day:** "Practice makes permanent. Make sure you're practicing right!"

---

**Day 2: COMPLETE ✅**  
**Streak: 2 days 🔥🔥**
```

---

## Step 2: If You Also Did Udemy Course Work

**In `udemy-exercises/100-days-python-bootcamp/`:**

Make sure your course files are there. If you created them elsewhere, move them into the appropriate day folder.

---

## 📦 COMMIT YOUR WORK (5 min)

### Now Let's Save Everything to GitHub!

**Step 1: Check What Changed**

Press **Ctrl+K** (or click green checkmark ✓)

You should see:
- `self-learning-exercises/day-02/` (new folder)
- `practice.py` (new)
- `bmi_calculator.py` (new)
- `tip_calculator.py` (new)
- `notes.md` (new)
- Maybe files in `udemy-exercises/` too

**Step 2: Select All Files**

Check ✓ all the new files

**Step 3: Write Commit Message**
```
Day 2: Data types, string manipulation, BMI & Tip calculators

Topics learned:
- Data types (int, float, string, bool)
- Type conversion
- String manipulation methods
- F-strings and formatting
- Mathematical operations

Projects:
- BMI Calculator - health calculation with categories
- Tip Calculator - bill splitting application

Completed practice exercises and Udemy Day 2 lessons.
```

**Step 4: Commit and Push**

Click **"Commit and Push"**

**Step 5: Verify on GitHub**

1. Go to: `github.com/venkateshpasala/python-learning-journey`
2. Click on `self-learning-exercises/`
3. You should see `day-02/` folder!
4. Check your profile - **2 GREEN SQUARES!** 🟢🟢

---

## 🎉 CELEBRATE YOUR PROGRESS!

### After 2 Days:
- ✅ **2-day streak** 🔥🔥
- ✅ **2 green squares** on GitHub
- ✅ **6+ programs written** (Day 1: 4, Day 2: 2+ projects)
- ✅ **Professional workflow established**
- ✅ **Portfolio growing daily**

### Skills Acquired:
```
Day 1: Variables, input, print ✅
Day 2: Data types, strings, math, formatting ✅

Combined: You can now build basic calculators and interactive programs!