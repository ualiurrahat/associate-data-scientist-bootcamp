# -*- coding: utf-8 -*-

"""
Exercise: Subset and Conquer
Course: Introduction to Python (DataCamp)
Section: Python Lists
Date: 2026-04-11
Student: Md. Ualiur Rahman Rahat

Description:
-----------
Subsetting means selecting specific elements from a list.
Python uses zero-based indexing (first element is index 0).
Negative indexing counts from the end (-1 is last element).

Key Concepts:
------------
1. Zero-based indexing: list[0] = first element
2. Positive indices: 0, 1, 2, 3... (start from beginning)
3. Negative indices: -1, -2, -3... (start from end)
4. Index must be within range (otherwise IndexError)

Original Exercise Instructions:
-------------------------------
1. Print the second element from areas (value 11.25)
2. Print the last element (9.50) using negative indexing
3. Print the living room area (20.0)

Learning Note from Student:
--------------------------
Similar to C++ arrays:
- Both use zero-based indexing
- Both have index bounds (don't go out of range)

Different from C++:
- Python has negative indexing (C++ doesn't)
- Negative indices are very convenient for last elements
"""

# Create the areas list (room names + areas alternating)
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
# Index 1 = second element (0=hallway, 1=11.25)
print(areas[1])  # Output: 11.25

# Print out last element from areas
# Index -1 = last element (9.50)
print(areas[-1])  # Output: 9.50

# Print out the area of the living room
# living room is at index 4, its area is at index 5
# But using negative: count from end -5 = 20.0
# Verification: len=10, -5 = index 5 (20.0)
print(areas[-5])  # Output: 20.0


# ============================================================================
# Additional Practice (self-added):
# ============================================================================

print("\n--- Index Exploration ---")

# Display all elements with their positive and negative indices
for i in range(len(areas)):
    print(f"Index {i:2d} (or {-len(areas)+i:2d}): {areas[i]}")

# Trying different index types
print(f"\nFirst element (index 0): {areas[0]}")
print(f"First element (index -10): {areas[-10]}")  # Same as index 0

# What happens with invalid index? (Uncomment to see error)
# print(areas[20])  # IndexError: list index out of range

# Practical use: Getting last element without knowing list length
print(f"Last element: {areas[-1]}")
print(f"Second to last: {areas[-2]}")


# ============================================================================
# Key Takeaways:
# ============================================================================
# 1. Python uses zero-based indexing (first element = index 0)
# 2. Negative indices count from the end (-1 = last element)
# 3. IndexError occurs if you try to access outside the list range
# 4. Negative indexing is cleaner than calculating length-1
# 5. Use positive indices from start, negative from end