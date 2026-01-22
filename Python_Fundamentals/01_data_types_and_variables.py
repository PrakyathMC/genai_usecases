"""
Python Fundamentals - Part 1: Data Types and Variables
======================================================

This is where everything starts. Understanding data types is crucial
because EVERYTHING in Python is an object with a type.

Run this file section by section to learn!
"""

# =============================================================================
# SECTION 1: Basic Data Types
# =============================================================================

print("=" * 60)
print("SECTION 1: Basic Data Types")
print("=" * 60)

# Python has these fundamental types:

# 1. Integers (int) - whole numbers

age = 25
year = 2025
negative_number = -100

print(f"Integer examples: {age}, {year}, {negative_number}")
print(f"Type: {type(age)} ")

# 2. Floats (float) - decimal numbers

price = 99.99
pi = 3.14159
scientific = 2.5e-3

print(f"\nFloat Examples: {price}, {pi}, {scientific}")
print(f"Type: {type(price)}")

# 3. Strings (str) - text
name = "Python"
message = 'Hello, World!'  # Single or double quotes work
multiline = """This is a
multiline string"""

print(f"\nString examples: {name}, {message}")
print(f"Type: {type(name)}")

# 4. Booleans (bool) - True or False
is_active = True
is_finished = False

print(f"\nBoolean examples: {is_active}, {is_finished}")
print(f"Type: {type(is_active)}")

# 5. None - represents "nothing" or "no value"
result = None

print(f"\nNone example: {result}")
print(f"Type: {type(result)}")


# =============================================================================
# SECTION 2: Type Checking and Conversion
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 2: Type Checking and Conversion")
print("=" * 60)

# Check types with type() and isinstance()
x = 42

print(f"type(x) = {type(x)}")
print(f"isinstance(x, int) = {isinstance(x, int)}")
print(f"isinstance(x, str) = {isinstance(x, str)}")

# Type conversion (casting)
# String to int
num_str = "123"
num_int = int(num_str)
print(f"\nString '{num_str}' to int: {num_int}")

# Int to string
num = 456
num_as_str = str(num)
print(f"Int {num} to string: '{num_as_str}'")

# String to float
price_str = "99.99"
price_float = float(price_str)
print(f"String '{price_str}' to float: {price_float}")

# Float to int (truncates, doesn't round!)
decimal = 9.99
whole = int(decimal)
print(f"Float {decimal} to int: {whole}  # Notice: truncated, not rounded!")

# To bool (Truthy and Falsy values)
print("\n--- Truthy and Falsy ---")
print(f"bool(1) = {bool(1)}")       # True - non-zero numbers are truthy
print(f"bool(0) = {bool(0)}")       # False - zero is falsy
print(f"bool('hello') = {bool('hello')}")  # True - non-empty strings
print(f"bool('') = {bool('')}")     # False - empty string is falsy
print(f"bool([1,2]) = {bool([1,2])}")  # True - non-empty list
print(f"bool([]) = {bool([])}")     # False - empty list is falsy
print(f"bool(None) = {bool(None)}") # False - None is falsy


# =============================================================================
# SECTION 3: Variables and Assignment
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 3: Variables and Assignment")
print("=" * 60)

# Basic assignment
x = 10
y = 20

# Multiple assignment (same value)
a = b = c = 0
print(f"Multiple assignment: a={a}, b={b}, c={c}")

# Multiple assignment (different values) - tuple unpacking
x, y, z = 1, 2, 3
print(f"Tuple unpacking: x={x}, y={y}, z={z}")

# Swap variables (Python makes this easy!)
a = "first"
b = "second"
print(f"\nBefore swap: a='{a}', b='{b}'")
a, b = b, a  # This is the Pythonic way!
print(f"After swap: a='{a}', b='{b}'")

# Augmented assignment operators
count = 10
count += 5   # Same as: count = count + 5
print(f"\ncount += 5: {count}")

count -= 3   # Same as: count = count - 3
print(f"count -= 3: {count}")

count *= 2   # Same as: count = count * 2
print(f"count *= 2: {count}")

count //= 3  # Same as: count = count // 3 (floor division)
print(f"count //= 3: {count}")


# =============================================================================
# SECTION 4: String Operations (Very Important!)
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 4: String Operations")
print("=" * 60)

text = "Hello, Python World!"

# Length
print(f"String: '{text}'")
print(f"Length: {len(text)}")

# Indexing (0-based)
print(f"\nIndexing:")
print(f"  text[0] = '{text[0]}'")   # First character
print(f"  text[-1] = '{text[-1]}'") # Last character
print(f"  text[7] = '{text[7]}'")   # 8th character

# Slicing [start:end:step]
print(f"\nSlicing:")
print(f"  text[0:5] = '{text[0:5]}'")     # First 5 chars
print(f"  text[7:13] = '{text[7:13]}'")   # Characters 7-12
print(f"  text[:5] = '{text[:5]}'")       # From start to 5
print(f"  text[7:] = '{text[7:]}'")       # From 7 to end
print(f"  text[::2] = '{text[::2]}'")     # Every 2nd character
print(f"  text[::-1] = '{text[::-1]}'")   # Reversed!

# String methods
name = "  john doe  "
print(f"\nString methods on '{name}':")
print(f"  .strip() = '{name.strip()}'")       # Remove whitespace
print(f"  .upper() = '{name.strip().upper()}'")
print(f"  .lower() = '{name.strip().lower()}'")
print(f"  .title() = '{name.strip().title()}'")
print(f"  .replace('john', 'jane') = '{name.strip().replace('john', 'jane')}'")

# Split and Join
sentence = "Python is awesome"
words = sentence.split()  # Split by whitespace
print(f"\nSplit: '{sentence}'.split() = {words}")

joined = "-".join(words)
print(f"Join: '-'.join({words}) = '{joined}'")

# String formatting (3 ways - f-strings are best!)
name = "Alice"
age = 30

# Method 1: f-strings (Python 3.6+) - RECOMMENDED
print(f"\nf-string: My name is {name} and I am {age} years old")

# Method 2: .format()
print("format(): My name is {} and I am {} years old".format(name, age))

# Method 3: % formatting (old style)
print("%% formatting: My name is %s and I am %d years old" % (name, age))

# f-string tricks
price = 49.99
quantity = 3
print(f"\nf-string tricks:")
print(f"  Expression: {price * quantity}")
print(f"  Formatting: ${price:.2f}")  # 2 decimal places
print(f"  Padding: {age:05d}")        # Pad with zeros


# =============================================================================
# SECTION 5: Numbers and Math Operations
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 5: Numbers and Math Operations")
print("=" * 60)

a, b = 17, 5

print(f"a = {a}, b = {b}")
print(f"\nBasic operations:")
print(f"  a + b = {a + b}")   # Addition
print(f"  a - b = {a - b}")   # Subtraction
print(f"  a * b = {a * b}")   # Multiplication
print(f"  a / b = {a / b}")   # Division (always returns float!)
print(f"  a // b = {a // b}") # Floor division (integer result)
print(f"  a % b = {a % b}")   # Modulo (remainder)
print(f"  a ** b = {a ** b}") # Exponentiation (power)

# Useful built-in functions
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"\nBuilt-in math functions on {numbers}:")
print(f"  min() = {min(numbers)}")
print(f"  max() = {max(numbers)}")
print(f"  sum() = {sum(numbers)}")
print(f"  abs(-5) = {abs(-5)}")
print(f"  round(3.7) = {round(3.7)}")
print(f"  round(3.14159, 2) = {round(3.14159, 2)}")


# =============================================================================
# SUMMARY
# =============================================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
Key Takeaways:
--------------
1. Python has 5 basic types: int, float, str, bool, None

2. Everything in Python is an object with a type

3. Use type() to check type, isinstance() for type checking

4. Strings are immutable - methods return NEW strings

5. f-strings are the best way to format strings

6. // is floor division, % is modulo (remainder)

7. Falsy values: 0, 0.0, '', [], {}, None, False
   Everything else is Truthy

Next: Data Structures (lists, dicts, tuples, sets)
""")
