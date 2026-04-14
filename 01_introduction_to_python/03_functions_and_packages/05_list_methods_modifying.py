# -*- coding: utf-8 -*-

"""
Exercise: List Methods (Modifying)
Course: Introduction to Python (DataCamp)
Section: Functions and Packages
Date: 2026-04-14
Student: Md. Ualiur Rahman Rahat

Description:
-----------
Some list methods MODIFY the list they're called on (in-place operations).
These methods return None, not a new list.

Key Concepts:
------------
1. .append() - adds element to END of list (modifies original)
2. .reverse() - reverses list IN-PLACE (modifies original)
3. These methods return None (unlike sorted() which returns a new list)
4. Method chaining is NOT possible with these (since they return None)

Original Exercise Instructions:
-------------------------------
1. Use .append() twice to add 24.5 and 15.45
2. Print areas after appending
3. Use .reverse() to reverse the order
4. Print areas again after reversal

Learning Note from Student:
--------------------------
Important distinction:
- sorted(list) returns NEW list (original unchanged)
- list.reverse() modifies IN-PLACE (original changed, returns None)
- This is a common source of bugs for beginners!
"""

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
print("Original list:")
print(areas)

# Use append twice to add poolhouse and garage size
# .append() adds to the END of the list
areas.append(24.5)   # Add poolhouse size
areas.append(15.45)  # Add garage size

# Print out areas after appending
print("\nAfter appending 24.5 and 15.45:")
print(areas)

# Reverse the orders of the elements in areas
# .reverse() modifies the list IN-PLACE
areas.reverse()

# Print out areas after reversal
print("\nAfter reverse():")
print(areas)


# ============================================================================
# Additional Practice (self-added):
# ============================================================================

print("\n--- More Modifying List Methods ---")

# .insert() - insert at specific position
colors = ["red", "blue", "green"]
print(f"Original: {colors}")
colors.insert(1, "yellow")  # Insert at index 1
print(f"After insert(1, 'yellow'): {colors}")

# .remove() - remove first matching element
colors.remove("blue")
print(f"After remove('blue'): {colors}")

# .pop() - remove and return last element (or at index)
last = colors.pop()
print(f"Popped: {last}, remaining: {colors}")

# .extend() - add multiple elements (vs .append() which adds one)
numbers = [1, 2, 3]
numbers.extend([4, 5, 6])  # Add multiple
print(f"After extend([4,5,6]): {numbers}")

# Compare .append() vs .extend()
list_a = [1, 2, 3]
list_a.append([4, 5])  # Adds list as ONE element
print(f".append([4,5]): {list_a}")  # [1, 2, 3, [4, 5]]

list_b = [1, 2, 3]
list_b.extend([4, 5])   # Adds each element individually
print(f".extend([4,5]): {list_b}")   # [1, 2, 3, 4, 5]

# .sort() - sort in-place (vs sorted() which returns new)
unsorted = [3, 1, 4, 1, 5]
unsorted.sort()  # Modifies original
print(f"\nAfter .sort(): {unsorted}")

# Common mistake (uncomment to see)
# result = areas.append(99)  # result will be None!
# print(result)  # None


# ============================================================================
# Key Takeaways:
# ============================================================================
# 1. .append() adds ONE element to the end (modifies original)
# 2. .extend() adds MULTIPLE elements (iterable) to end
# 3. .reverse() reverses IN-PLACE (original list changes)
# 4. .sort() sorts IN-PLACE (vs sorted() returns new list)
# 5. Modifying methods return None (can't chain them)
# 6. Always check whether a method modifies in-place or returns a new object
# 7. .append() vs .extend(): one adds element, other adds each item individually