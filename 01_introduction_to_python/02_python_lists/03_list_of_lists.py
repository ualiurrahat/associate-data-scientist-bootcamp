#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Exercise: List of Lists
Course: Introduction to Python (DataCamp)
Section: Python Lists
Date: 2026-04-11
Student: Md. Ualiur Rahman Rahat

Description:
-----------
A list can contain other lists as its elements.
This creates a nested or 2D structure (list of lists).
Each inner list can represent a record or row of data.

Key Concepts:
------------
1. Lists can contain other lists (nested lists)
2. Each inner list is a separate list object
3. This creates a hierarchical/tabular data structure
4. Access pattern: outer_list[index][inner_index]

Original Exercise Instructions:
-------------------------------
1. Create a list of lists called 'house'
2. Each inner list: [room_name, area]
3. Include: hallway, kitchen, living room, bedroom, bathroom (in order)
4. Print the house list

Learning Note from Student:
--------------------------
This is like a 2D array or a table:
- Each row is a list [room_name, area]
- Multiple rows form the complete dataset
- Much more organized than a flat alternating list
- Similar to a CSV file or database table structure
"""

# Predefined area measurements
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create a list of lists (nested list structure)
# Each inner list represents one room: [room_name_string, area_float]
house = [
    ["hallway", hall],
    ["kitchen", kit],
    ["living room", liv],
    ["bedroom", bed],
    ["bathroom", bath]
]

# Print the list of lists
# Output: [['hallway', 11.25], ['kitchen', 18.0], ['living room', 20.0], ['bedroom', 10.75], ['bathroom', 9.5]]
print(house)


# ============================================================================
# Additional Practice (self-added):
# ============================================================================

# Accessing elements in a list of lists
print(f"\n--- Accessing nested list elements ---")
print(f"First room: {house[0]}")           # ['hallway', 11.25]
print(f"First room name: {house[0][0]}")   # 'hallway'
print(f"First room area: {house[0][1]}")   # 11.25
print(f"Third room area: {house[2][1]}")   # 20.0

# Iterating through a list of lists
print(f"\n--- House rooms (iterated) ---")
for room in house:
    print(f"{room[0]}: {room[1]} sq units")

# Creating a list of lists from scratch (student gradebook example)
gradebook = [
    ["Math", 85],
    ["Physics", 90],
    ["Computer Science", 95],
    ["English", 88]
]
print(f"\nGradebook: {gradebook}")

# Finding the length of outer and inner lists
print(f"\nNumber of rooms: {len(house)}")
print(f"Items in first room record: {len(house[0])}")

# List of lists with 3 columns (extended example)
extended_house = [
    ["hallway", hall, "entrance area"],
    ["kitchen", kit, "cooking space"],
    ["living room", liv, "main living area"]
]
print(f"\nExtended house data (3 columns): {extended_house}")


# ============================================================================
# Key Takeaways:
# ============================================================================
# 1. List of lists creates tabular/2D data structure
# 2. Each inner list is a row/record
# 3. Access using double indexing: list[row][column]
# 4. More organized than flat alternating lists
# 5. This is the foundation for more complex data structures (pandas DataFrames later)
# 6. You can iterate through rows using for loops