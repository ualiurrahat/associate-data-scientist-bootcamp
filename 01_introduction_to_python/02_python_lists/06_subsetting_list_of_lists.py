#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Exercise: Subsetting Lists of Lists
Course: Introduction to Python (DataCamp)
Section: Python Lists
Date: 2026-04-11
Student: Md. Ualiur Rahman Rahat

Description:
-----------
When a list contains other lists, use double indexing to access inner elements.
First index selects the inner list (row), second index selects element within that list.

Key Concepts:
------------
1. Syntax: outer_list[row_index][column_index]
2. First index = which inner list
3. Second index = which element inside that inner list
4. Can chain multiple indices for deeper nesting

Original Exercise Instructions:
-------------------------------
Subset the house list to get the float 9.50 (bathroom area).

Learning Note from Student:
--------------------------
Similar to 2D arrays in C++: array[row][column].
But Python lists of lists can have inner lists of different lengths.
Data science often uses this for matrices or tabular data.
"""

# House information as list of lists
# Each inner list: [room_name (str), area (float)]
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Subset the house list to get bathroom area (9.50)
# Step 1: house[4] = ["bathroom", 9.50]
# Step 2: house[4][1] = 9.50
bathroom_area = house[4][1]
print(bathroom_area)  # Output: 9.5


# ============================================================================
# Additional Practice (self-added):
# ============================================================================

print("\n--- List of Lists Access Patterns ---")

# Access each room's name and area
print("All rooms and their areas:")
for i in range(len(house)):
    room_name = house[i][0]
    room_area = house[i][1]
    print(f"  {room_name}: {room_area}")

# Different ways to get the same value
print(f"\nBathroom area (positive index): {house[4][1]}")
print(f"Bathroom area (negative index): {house[-1][1]}")
print(f"Bathroom area (nested variable): {house[4][-1]}")

# Deeper nesting example (3 levels)
deep_list = [
    [["a1", "a2"], ["a3", "a4"]],
    [["b1", "b2"], ["b3", "b4"]]
]
print(f"\nDeep nesting example: {deep_list[0][1][0]}")  # Output: a3

# Data science application: matrix/table representation
# Rows = observations, Columns = features
data_matrix = [
    [25, 65, 70],   # Person 1: [age, weight, height]
    [30, 72, 68],   # Person 2
    [22, 58, 65]    # Person 3
]
print(f"\nPerson 2's weight: {data_matrix[1][1]}")


# ============================================================================
# Key Takeaways:
# ============================================================================
# 1. Use double brackets: outer[row][column]
# 2. First index selects the inner list (row)
# 3. Second index selects element within that list (column)
# 4. Works for any depth of nesting (triple, quadruple, etc.)
# 5. Fundamental for matrix operations in data science