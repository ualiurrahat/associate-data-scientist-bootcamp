# -*- coding: utf-8 -*-

"""
Exercise: Inner Workings of Lists
Course: Introduction to Python (DataCamp)
Section: Python Lists
Date: 2026-04-11
Student: Md. Ualiur Rahman Rahat

Description:
-----------
In Python, variables are references (pointers) to objects in memory.
When you assign list2 = list1, both variables point to the SAME list.
Changes to one affect the other because they reference the same object.

Key Concepts:
------------
1. Assignment copies the reference, not the list contents
2. To create an independent copy, use: list_copy = original[:] or list(original)
3. This is called "shallow copy" (enough for simple lists)
4. "Deep copy" needed for nested lists (copy module)

Original Exercise Instructions:
-------------------------------
Change the assignment so areas_copy is an explicit copy (independent).
After fix, changing areas_copy should NOT affect areas.

Learning Note from Student:
--------------------------
This is different from C++ where = copies values (unless using pointers).
Python's behavior is more like Java (references).
For data science, always explicitly copy when you want independent data.
"""

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
print("Original areas:", areas)

# BAD WAY (reference copy) — uncomment to see effect
# areas_copy = areas  # Both point to same list

# GOOD WAY (explicit copy) — using slice [:]
areas_copy = areas[:]  # Creates independent copy

# Alternative good ways:
# areas_copy = areas.copy()  # Python 3.3+
# areas_copy = list(areas)   # Using list constructor

# Change areas_copy (modify first element)
areas_copy[0] = 5.0

# Print areas — with explicit copy, original remains unchanged
print("\nAfter modifying areas_copy (first element → 5.0):")
print("areas (original):", areas)        # Unchanged: [11.25, 18.0, 20.0, 10.75, 9.50]
print("areas_copy (copy):", areas_copy)  # Changed: [5.0, 18.0, 20.0, 10.75, 9.50]


# ============================================================================
# Additional Practice (self-added):
# ============================================================================

print("\n--- Reference vs Copy Demonstration ---")

# Reference assignment (both point to same list)
list_a = [1, 2, 3]
list_b = list_a  # list_b references the SAME list
list_b[0] = 999
print("Reference assignment:")
print(f"  list_a: {list_a}")  # Changed! [999, 2, 3]
print(f"  list_b: {list_b}")  # [999, 2, 3]
print(f"  Same object? {list_a is list_b}")  # True

# Independent copy (different lists)
list_c = [1, 2, 3]
list_d = list_c[:]  # Independent copy
list_d[0] = 999
print("\nIndependent copy:")
print(f"  list_c: {list_c}")  # Unchanged [1, 2, 3]
print(f"  list_d: {list_d}")  # [999, 2, 3]
print(f"  Same object? {list_c is list_d}")  # False

# For nested lists: need deep copy
import copy
nested_original = [[1, 2], [3, 4]]
shallow_copy = nested_original[:]  # Outer list copied, inner lists referenced
deep_copy = copy.deepcopy(nested_original)  # Everything copied

shallow_copy[0][0] = 999  # Modifies original's inner list!
deep_copy[1][0] = 888     # Does NOT modify original

print("\nNested list copying:")
print(f"  Original: {nested_original}")
print(f"  Shallow copy changed original? Yes (inner list shared)")
print(f"  Deep copy changed original? No (fully independent)")


# ============================================================================
# Key Takeaways:
# ============================================================================
# 1. Python variables are references (pointers to objects)
# 2. list2 = list1 makes both point to the SAME list
# 3. Use list2 = list1[:] to create an independent copy
# 4. Alternative copies: .copy(), list(), copy.copy()
# 5. For nested lists, use copy.deepcopy() for full independence
# 6. This is crucial in data science when you want to preserve original data
# 7. Always ask: "Do I want a reference or a copy?"