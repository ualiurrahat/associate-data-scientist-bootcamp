# -*- coding: utf-8 -*-

"""
Exercise: Replace List Elements
Course: Introduction to Python (DataCamp)
Section: Python Lists
Date: 2026-04-11
Student: Md. Ualiur Rahman Rahat

Description:
-----------
Lists are mutable (changeable) in Python.
You can replace elements by assigning a new value to a specific index.
Works for single elements or slices.

Key Concepts:
------------
1. Assignment to index: list[index] = new_value
2. Assignment to slice: list[start:end] = [new_values]
3. Mutable = can be changed after creation
4. Immutable = cannot be changed (strings, tuples)

Original Exercise Instructions:
-------------------------------
1. Update bathroom area to 10.50 using negative indexing
2. Change "living room" to "chill zone" (positive indexing)

Learning Note from Student:
--------------------------
C++ arrays are also mutable (you can assign to index).
But Python allows slice assignment (replace multiple at once).
Strings in Python are immutable (can't change characters) — different from lists.
"""

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, 
         "bedroom", 10.75, "bathroom", 9.50]

print("Original list:")
print(areas)

# Correct the bathroom area using negative indexing
# Last element (index -1) is currently 9.50, change to 10.50
areas[-1] = 10.50
print("\nAfter bathroom area update:")
print(areas)

# Change "living room" to "chill zone" using positive indexing
# "living room" is at index 4
areas[4] = "chill zone"
print("\nAfter renaming living room:")
print(areas)


# ============================================================================
# Additional Practice (self-added):
# ============================================================================

print("\n--- Advanced Replacement Techniques ---")

# Replace multiple elements at once (slice assignment)
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(f"Original numbers: {numbers}")

# Replace indices 2 through 4 (excludes index 5)
numbers[2:5] = [30, 40, 50]
print(f"After slice replacement: {numbers}")

# Replace with fewer elements (list shrinks)
numbers[0:2] = [10]  # Replaces 2 elements with 1
print(f"After replacing with fewer: {numbers}")

# Replace with more elements (list expands)
numbers[1:2] = [20, 25, 30]  # Replaces 1 element with 3
print(f"After replacing with more: {numbers}")

# Practical data science example: cleaning data
sensor_readings = [101, 102, 999, 104, 105, 999, 107]
print(f"\nSensor readings (999 = error): {sensor_readings}")

# Replace error values (999) with None (missing data indicator)
for i in range(len(sensor_readings)):
    if sensor_readings[i] == 999:
        sensor_readings[i] = None
print(f"After cleaning: {sensor_readings}")


# ============================================================================
# Key Takeaways:
# ============================================================================
# 1. Lists are mutable (can be changed after creation)
# 2. Assign to index: list[index] = new_value
# 3. Assign to slice: list[start:end] = [values] (can change list length)
# 4. Negative indexing works for assignment too
# 5. Data cleaning often involves replacing values in lists
# 6. Strings are immutable — can't do string[0] = 'x' (would cause error)