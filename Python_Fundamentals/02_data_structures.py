"""
The Big 4: Lists, Dictionaries, Tuples, Sets
"""

# =============================================================================
# SECTION 1: Lists - Ordered, Mutable, Allows Duplicates
# =============================================================================

print("=" * 60)
print("SECTION 1: Lists")
print("=" * 60)

# Creating lists
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, None]  # Can mix types
empty = []

print(f"Numbers: {numbers}")
print(f"Mixed types: {mixed}")
print(f"Empty list: {empty}")


# Accessing elements (same as strings - 0-indexed)
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print(f"\nAccessing elements in {fruits}:")
print(f"  fruits[0] = '{fruits[0]}'")      # First
print(f"  fruits[-1] = '{fruits[-1]}'")    # Last
print(f"  fruits[1:4] = {fruits[1:4]}")    # Slice

# Lists are MUTABLE (can be changed)
print(f"\nMutability:")
fruits[0] = "apricot"  # Change first element
print(f"  After fruits[0] = 'apricot': {fruits}")

# Adding elements
print(f"\nAdding elements:")
fruits.append("fig")           # Add to end
print(f"  .append('fig'): {fruits}")

fruits.insert(1, "blueberry")  # Insert at index 1
print(f"  .insert(1, 'blueberry'): {fruits}")

more_fruits = ["grape", "honeydew"]
fruits.extend(more_fruits)     # Add multiple items
print(f"  .extend(['grape', 'honeydew']): {fruits}")

# Removing elements
print(f"\nRemoving elements:")
fruits.pop()         # Remove and return last item
print(f"  .pop(): {fruits}")

fruits.pop(0)        # Remove at index
print(f"  .pop(0): {fruits}")

fruits.remove("cherry")  # Remove by value (first occurrence)
print(f"  .remove('cherry'): {fruits}")

# List operations
nums = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"\nList operations on {nums}:")
print(f"  len(nums) = {len(nums)}")
print(f"  min(nums) = {min(nums)}")
print(f"  max(nums) = {max(nums)}")
print(f"  sum(nums) = {sum(nums)}")
print(f"  1 in nums = {1 in nums}")
print(f"  nums.count(1) = {nums.count(1)}")  # Count occurrences
print(f"  nums.index(5) = {nums.index(5)}")  # Find index of value

# Sorting
print(f"\nSorting:")
nums_copy = nums.copy()  # Make a copy first
nums_copy.sort()
print(f"  .sort() (modifies in place): {nums_copy}")

nums_copy.sort(reverse=True)
print(f"  .sort(reverse=True): {nums_copy}")

# sorted() returns NEW list, original unchanged
print(f"  sorted(nums) = {sorted(nums)}")
print(f"  Original nums still: {nums}")

# List comprehensions - VERY IMPORTANT!
print(f"\nList Comprehensions (Pythonic way to create lists):")

# Basic: [expression for item in iterable]
squares = [x**2 for x in range(1, 6)]
print(f"  [x**2 for x in range(1, 6)] = {squares}")

# With condition: [expression for item in iterable if condition]
evens = [x for x in range(10) if x % 2 == 0]
print(f"  [x for x in range(10) if x % 2 == 0] = {evens}")

# Transform strings
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print(f"  [word.upper() for word in {words}] = {upper_words}")


# =============================================================================
# SECTION 2: Dictionaries - Key-Value Pairs, Unordered*, Mutable
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 2: Dictionaries")
print("=" * 60)

# Creating dictionaries
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "is_student": False
}

print(f"Person: {person}")

# Accessing values
print(f"\nAccessing values:")
print(f"  person['name'] = '{person['name']}'")
print(f"  person.get('age') = {person.get('age')}")

# .get() is safer - returns None if key missing (or default value)
print(f"  person.get('salary') = {person.get('salary')}")  # None
print(f"  person.get('salary', 0) = {person.get('salary', 0)}")  # Default 0

# Adding/Updating values
print(f"\nAdding/Updating:")
person["email"] = "alice@example.com"  # Add new key
print(f"  Added 'email': {person}")

person["age"] = 31  # Update existing
print(f"  Updated 'age': {person}")

# Removing
print(f"\nRemoving:")
removed_value = person.pop("is_student")  # Remove and return value
print(f"  .pop('is_student') returned: {removed_value}")
print(f"  Dict now: {person}")

# Dictionary methods
print(f"\nDictionary methods:")
print(f"  .keys() = {list(person.keys())}")
print(f"  .values() = {list(person.values())}")
print(f"  .items() = {list(person.items())}")

# Checking membership
print(f"\nMembership:")
print(f"  'name' in person = {'name' in person}")
print(f"  'salary' in person = {'salary' in person}")

# Iterating over dictionaries
print(f"\nIterating:")
print("  Iterating over keys:")
for key in person:
    print(f"    {key}: {person[key]}")

print("\n  Iterating over items (key-value pairs):")
for key, value in person.items():
    print(f"    {key} = {value}")

# Dictionary comprehensions
print(f"\nDictionary Comprehensions:")
squares_dict = {x: x**2 for x in range(1, 6)}
print(f"  {{x: x**2 for x in range(1, 6)}} = {squares_dict}")

# Nested dictionaries
print(f"\nNested Dictionaries:")
users = {
    "user1": {"name": "Alice", "age": 30},
    "user2": {"name": "Bob", "age": 25}
}
print(f"  users['user1']['name'] = '{users['user1']['name']}'")


# =============================================================================
# SECTION 3: Tuples - Ordered, IMMUTABLE, Allows Duplicates
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 3: Tuples")
print("=" * 60)

# Creating tuples
coordinates = (10, 20)
rgb = (255, 128, 0)
single = (42,)  # Note the comma! Without it, it is just an int
mixed_tuple = (1, "hello", 3.14)

print(f"Coordinates: {coordinates}")
print(f"RGB: {rgb}")
print(f"Single element tuple: {single}, type: {type(single)}")
print(f"Without comma: {(42)}, type: {type((42))}")  # Just an int!

# Accessing elements (same as lists)
print(f"\nAccessing:")
print(f"  coordinates[0] = {coordinates[0]}")
print(f"  coordinates[-1] = {coordinates[-1]}")

# Tuples are IMMUTABLE - cannot be changed!
print(f"\nImmutability:")
print("  coordinates[0] = 5  # This would raise TypeError!")
# coordinates[0] = 5  # Uncomment to see the error

# Tuple unpacking - VERY useful!
print(f"\nTuple Unpacking:")
x, y = coordinates
print(f"  x, y = {coordinates} -> x={x}, y={y}")

# Swap using tuple unpacking
a, b = 1, 2
a, b = b, a
print(f"  Swap: a, b = b, a -> a={a}, b={b}")

# Unpacking with * (rest operator)
first, *rest = [1, 2, 3, 4, 5]
print(f"  first, *rest = [1,2,3,4,5] -> first={first}, rest={rest}")

*start, last = [1, 2, 3, 4, 5]
print(f"  *start, last = [1,2,3,4,5] -> start={start}, last={last}")

# When to use tuples vs lists?
print(f"\nTuple vs List:")
print("""
  Use TUPLES when:
    - Data should not change (coordinates, RGB values)
    - Returning multiple values from a function
    - Dictionary keys (lists cannot be keys!)
    - Slightly more memory efficient

  Use LISTS when:
    - Data needs to be modified
    - Order matters and items will be added/removed
""")


# =============================================================================
# SECTION 4: Sets - Unordered, Mutable, NO Duplicates
# =============================================================================

print("=" * 60)
print("SECTION 4: Sets")
print("=" * 60)

# Creating sets
numbers = {1, 2, 3, 4, 5}
from_list = set([1, 2, 2, 3, 3, 3])  # Duplicates removed!
empty_set = set()  # NOT {} - that creates an empty dict!

print(f"Numbers: {numbers}")
print(f"From list with duplicates: {from_list}")
print(f"Empty set: {empty_set}")
print(f"Note: {{}} creates {type({})}, not a set!")

# Sets automatically remove duplicates
duplicates = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = set(duplicates)
print(f"\nRemoving duplicates: {duplicates} -> {unique}")

# Adding and removing
print(f"\nAdding/Removing:")
numbers.add(6)
print(f"  .add(6): {numbers}")

numbers.discard(1)  # Remove if exists (no error if missing)
print(f"  .discard(1): {numbers}")

# Set operations - VERY powerful!
print(f"\nSet Operations:")
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(f"  a = {a}")
print(f"  b = {b}")
print(f"  Union (a | b): {a | b}")           # All elements
print(f"  Intersection (a & b): {a & b}")    # Common elements
print(f"  Difference (a - b): {a - b}")      # In a but not b
print(f"  Symmetric diff (a ^ b): {a ^ b}")  # In a or b, not both

# Membership testing is FAST with sets!
print(f"\nMembership (very fast with sets):")
large_list = list(range(10000))
large_set = set(range(10000))
print(f"  9999 in large_set = {9999 in large_set}")  # O(1) - instant!
# 9999 in large_list would be O(n) - much slower for large lists

# Set comprehensions
evens_set = {x for x in range(10) if x % 2 == 0}
print(f"\nSet Comprehension: {{x for x in range(10) if x % 2 == 0}} = {evens_set}")


# =============================================================================
# SECTION 5: Comparing Data Structures
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 5: Comparison Summary")
print("=" * 60)

print("""
+-------------+----------+-----------+------------+------------------+
| Structure   | Ordered  | Mutable   | Duplicates | Use Case         |
+-------------+----------+-----------+------------+------------------+
| List        | Yes      | Yes       | Yes        | General purpose  |
| Dictionary  | Yes*     | Yes       | Keys: No   | Key-value lookup |
| Tuple       | Yes      | No        | Yes        | Fixed data       |
| Set         | No       | Yes       | No         | Unique items     |
+-------------+----------+-----------+------------+------------------+

* Dictionaries maintain insertion order since Python 3.7

Common Operations Cheat Sheet:
------------------------------
| Operation      | List      | Dict           | Tuple    | Set       |
|----------------|-----------|----------------|----------|-----------|
| Create empty   | []        | {}             | ()       | set()     |
| Add item       | .append() | d[key]=val     | N/A      | .add()    |
| Remove item    | .remove() | .pop(key)      | N/A      | .discard()|
| Access         | lst[i]    | d[key]         | tup[i]   | N/A       |
| Check exists   | x in lst  | key in d       | x in tup | x in s    |
| Length         | len(lst)  | len(d)         | len(tup) | len(s)    |
""")


# =============================================================================
# SECTION 6: Practice Exercises
# =============================================================================

print("=" * 60)
print("SECTION 6: Practice Exercises")
print("=" * 60)

print("""
Try these exercises:

1. LIST PRACTICE:
   - Create a list of numbers 1-10
   - Remove all even numbers using list comprehension
   - Square the remaining numbers

2. DICTIONARY PRACTICE:
   - Create a dict mapping names to ages for 3 people
   - Add a new person
   - Find the oldest person using max() with a key function

3. TUPLE PRACTICE:
   - Create a function that returns (min, max, average) of a list
   - Use tuple unpacking to get the results

4. SET PRACTICE:
   - Given two lists: [1,2,3,4] and [3,4,5,6]
   - Find elements in both lists
   - Find elements in first but not second
   - Find all unique elements

5. REAL WORLD SCENARIO:
   - Given a list of words, count frequency of each word
   - Hint: Use a dictionary!
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
1. Lists: Your go-to for ordered, changeable collections
   - Use list comprehensions for elegant code!

2. Dictionaries: Perfect for key-value relationships
   - O(1) lookup time - very fast!
   - Use .get() for safe access

3. Tuples: Immutable sequences
   - Great for returning multiple values
   - Use tuple unpacking!

4. Sets: Unique items only, super fast membership testing
   - Perfect for removing duplicates
   - Set operations (union, intersection) are powerful

5. Choose the right structure for the job:
   - Need order + changes? -> List
   - Need key-value pairs? -> Dictionary
   - Need immutability? -> Tuple
   - Need uniqueness? -> Set

Next: Control Flow and Loops
""")
