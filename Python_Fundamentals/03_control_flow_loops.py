"""
Python Fundamentals - Part 3: Control Flow and Loops
=====================================================

Control flow determines WHAT code runs and WHEN.
Loops determine HOW MANY TIMES code runs.

These are the building blocks of all programs!
"""

# =============================================================================
# SECTION 1: Conditional Statements (if/elif/else)
# =============================================================================

print("=" * 60)
print("SECTION 1: Conditional Statements")
print("=" * 60)

# Basic if statement
age = 20

print(f"Age: {age}")

if age >= 18:
    print("You are an adult")

# if-else
temperature = 35

print(f"\nTemperature: {temperature}")

if temperature > 30:
    print("It is hot!")
else:
    print("It is not hot")

# if-elif-else (multiple conditions)
score = 85

print(f"\nScore: {score}")

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Grade: {grade}")

# Nested conditions
print("\nNested conditions:")
user_type = "admin"
is_active = True

if user_type == "admin":
    if is_active:
        print("  Active admin - full access")
    else:
        print("  Inactive admin - limited access")
else:
    print("  Regular user")


# =============================================================================
# SECTION 2: Comparison and Logical Operators
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 2: Comparison and Logical Operators")
print("=" * 60)

a, b = 10, 20

# Comparison operators
print(f"a = {a}, b = {b}")
print(f"\nComparison operators:")
print(f"  a == b  (equal): {a == b}")
print(f"  a != b  (not equal): {a != b}")
print(f"  a < b   (less than): {a < b}")
print(f"  a > b   (greater than): {a > b}")
print(f"  a <= b  (less or equal): {a <= b}")
print(f"  a >= b  (greater or equal): {a >= b}")

# Logical operators: and, or, not
print(f"\nLogical operators:")
x = True
y = False

print(f"  x = {x}, y = {y}")
print(f"  x and y: {x and y}")  # Both must be True
print(f"  x or y: {x or y}")    # At least one True
print(f"  not x: {not x}")      # Opposite

# Combining conditions
age = 25
has_license = True

print(f"\nCombining conditions:")
print(f"  age = {age}, has_license = {has_license}")

if age >= 18 and has_license:
    print("  You can drive!")

# Chained comparisons (Python special!)
print(f"\nChained comparisons (Pythonic!):")
score = 75
print(f"  score = {score}")
print(f"  60 <= score <= 80: {60 <= score <= 80}")  # Instead of: score >= 60 and score <= 80

# Identity operators: is, is not
print(f"\nIdentity operators (is vs ==):")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"  list1 = {list1}")
print(f"  list2 = {list2}")
print(f"  list3 = list1")
print(f"  list1 == list2: {list1 == list2}")  # Same content? Yes
print(f"  list1 is list2: {list1 is list2}")  # Same object? No
print(f"  list1 is list3: {list1 is list3}")  # Same object? Yes

# Use 'is' for None checks
value = None
if value is None:
    print("  value is None (use 'is' for None checks)")


# =============================================================================
# SECTION 3: For Loops
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 3: For Loops")
print("=" * 60)

# Basic for loop - iterate over a sequence
print("Basic for loop over a list:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"  {fruit}")

# for loop with range()
print("\nUsing range():")
print("  range(5) -> 0 to 4:")
for i in range(5):
    print(f"    i = {i}")

print("\n  range(2, 6) -> 2 to 5:")
for i in range(2, 6):
    print(f"    i = {i}")

print("\n  range(0, 10, 2) -> 0 to 8, step 2:")
for i in range(0, 10, 2):
    print(f"    i = {i}")

print("\n  range(5, 0, -1) -> 5 to 1, countdown:")
for i in range(5, 0, -1):
    print(f"    i = {i}")

# Iterating over strings
print("\nIterating over a string:")
for char in "Python":
    print(f"  {char}")

# Iterating over dictionaries
print("\nIterating over dictionaries:")
person = {"name": "Alice", "age": 30, "city": "NYC"}

print("  Keys only:")
for key in person:
    print(f"    {key}")

print("\n  Keys and values:")
for key, value in person.items():
    print(f"    {key}: {value}")

# enumerate() - get index AND value
print("\nenumerate() - index and value together:")
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"  Index {index}: {color}")

# Start from different index
print("\nenumerate() starting from 1:")
for index, color in enumerate(colors, start=1):
    print(f"  Item {index}: {color}")

# zip() - iterate over multiple sequences together
print("\nzip() - parallel iteration:")
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"  {name} is {age} years old")

# Nested loops
print("\nNested loops (multiplication table):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"  {i} x {j} = {i*j}")
    print()  # Empty line between rows


# =============================================================================
# SECTION 4: While Loops
# =============================================================================

print("=" * 60)
print("SECTION 4: While Loops")
print("=" * 60)

# Basic while loop
print("Basic while loop:")
count = 0
while count < 5:
    print(f"  count = {count}")
    count += 1

# While with condition
print("\nWhile with condition (simulate user input):")
attempts = 0
max_attempts = 3
password = "secret"
entered = ""

while entered != password and attempts < max_attempts:
    attempts += 1
    # Simulating wrong then correct password
    if attempts < 3:
        entered = "wrong"
        print(f"  Attempt {attempts}: Wrong password")
    else:
        entered = "secret"
        print(f"  Attempt {attempts}: Correct!")

# Infinite loops (be careful!)
print("\nInfinite loop with break:")
counter = 0
while True:  # This would run forever without break!
    print(f"  counter = {counter}")
    counter += 1
    if counter >= 3:
        print("  Breaking out!")
        break


# =============================================================================
# SECTION 5: Loop Control: break, continue, else
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 5: Loop Control")
print("=" * 60)

# break - exit the loop immediately
print("break - exit loop early:")
for num in range(10):
    if num == 5:
        print(f"  Found 5, breaking!")
        break
    print(f"  {num}")

# continue - skip to next iteration
print("\ncontinue - skip iteration:")
for num in range(6):
    if num == 3:
        print(f"  Skipping 3")
        continue
    print(f"  {num}")

# else clause on loops (runs if loop completes without break)
print("\nelse clause on loops:")

print("  Searching for 7 in [1,2,3,4,5]:")
for num in [1, 2, 3, 4, 5]:
    if num == 7:
        print("    Found 7!")
        break
else:
    print("    7 not found (else ran because no break)")

print("\n  Searching for 3 in [1,2,3,4,5]:")
for num in [1, 2, 3, 4, 5]:
    if num == 3:
        print("    Found 3!")
        break
else:
    print("    Not found")  # This will not print

# pass - do nothing (placeholder)
print("\npass - placeholder:")
for i in range(3):
    if i == 1:
        pass  # TODO: handle this case later
    else:
        print(f"  i = {i}")


# =============================================================================
# SECTION 6: Comprehensions (Pythonic Loops!)
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 6: Comprehensions")
print("=" * 60)

# List comprehension vs regular loop
print("List comprehension vs regular loop:")

# Traditional way
squares_traditional = []
for x in range(1, 6):
    squares_traditional.append(x ** 2)

# List comprehension (Pythonic!)
squares_comprehension = [x ** 2 for x in range(1, 6)]

print(f"  Traditional: {squares_traditional}")
print(f"  Comprehension: {squares_comprehension}")

# With condition
print("\nWith condition (even numbers only):")
evens = [x for x in range(10) if x % 2 == 0]
print(f"  {evens}")

# With if-else (conditional expression)
print("\nWith if-else:")
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
print(f"  {labels}")

# Dictionary comprehension
print("\nDictionary comprehension:")
squares_dict = {x: x**2 for x in range(1, 6)}
print(f"  {squares_dict}")

# Set comprehension
print("\nSet comprehension:")
unique_lengths = {len(word) for word in ["hello", "world", "python", "code"]}
print(f"  {unique_lengths}")

# Nested comprehension (2D list/matrix)
print("\nNested comprehension (3x3 matrix):")
matrix = [[i*3 + j for j in range(1, 4)] for i in range(3)]
for row in matrix:
    print(f"  {row}")


# =============================================================================
# SECTION 7: Common Patterns
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 7: Common Patterns")
print("=" * 60)

# Pattern 1: Find first match
print("Pattern 1 - Find first match:")
numbers = [1, 3, 5, 8, 9, 11]
for num in numbers:
    if num % 2 == 0:
        print(f"  First even number: {num}")
        break
else:
    print("  No even number found")

# Pattern 2: Collect matching items
print("\nPattern 2 - Collect matching items:")
evens = [num for num in numbers if num % 2 == 0]
print(f"  All even numbers: {evens}")

# Pattern 3: Transform all items
print("\nPattern 3 - Transform all items:")
doubled = [num * 2 for num in numbers]
print(f"  Doubled: {doubled}")

# Pattern 4: Count occurrences
print("\nPattern 4 - Count occurrences:")
text = "hello world"
vowel_count = sum(1 for char in text if char in "aeiou")
print(f"  Vowels in '{text}': {vowel_count}")

# Pattern 5: Check if any/all match
print("\nPattern 5 - any() and all():")
numbers = [2, 4, 6, 8]
print(f"  numbers = {numbers}")
print(f"  any(x > 5 for x in numbers): {any(x > 5 for x in numbers)}")  # At least one > 5?
print(f"  all(x % 2 == 0 for x in numbers): {all(x % 2 == 0 for x in numbers)}")  # All even?


# =============================================================================
# SECTION 8: Practice Exercises
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 8: Practice Exercises")
print("=" * 60)

print("""
Try these exercises:

1. FIZZBUZZ (Classic interview question!):
   - Print numbers 1-20
   - For multiples of 3, print "Fizz"
   - For multiples of 5, print "Buzz"
   - For multiples of both, print "FizzBuzz"

2. SUM OF DIGITS:
   - Given a number like 1234
   - Calculate sum of digits (1+2+3+4 = 10)
   - Hint: Convert to string and iterate

3. FIND PRIME NUMBERS:
   - Print all prime numbers from 2 to 50
   - A prime is only divisible by 1 and itself

4. PATTERN PRINTING:
   - Print this pattern:
   *
   **
   ***
   ****
   *****

5. LIST FILTERING:
   - Given: ["apple", "banana", "apricot", "cherry", "avocado"]
   - Find all words starting with 'a'
   - Use list comprehension

6. NESTED LOOP CHALLENGE:
   - Create a 5x5 multiplication table
""")


# =============================================================================
# SUMMARY
# =============================================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
Key Takeaways:
--------------
1. if/elif/else: Choose which code to run
   - Use 'and', 'or', 'not' for combining conditions
   - Use 'is' for None checks, '==' for value comparison

2. for loops: Iterate over sequences
   - range(n) for counting
   - enumerate() for index + value
   - zip() for parallel iteration

3. while loops: Repeat while condition is True
   - Be careful of infinite loops!
   - Use break to exit early

4. Loop control:
   - break: Exit loop immediately
   - continue: Skip to next iteration
   - else: Runs if loop completes without break

5. Comprehensions: Pythonic way to create collections
   - [expr for item in iterable if condition]
   - More readable and often faster!

6. Useful functions:
   - any(): True if any element is True
   - all(): True if all elements are True

Next: Functions Deep Dive
""")
