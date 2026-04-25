# -*- coding: utf-8 -*-

"""
Exercise: Loop over list of lists
Course: Intermediate Python (DataCamp)
Section: Loops
Date: 2026-04-25
Student: Md. Ualiur Rahman Rahat

Description:
Iterate through nested lists, accessing inner elements by index.

Key Concepts:
- Each iteration gives a sublist
- Access nested elements with [0], [1], etc.
- String formatting with indices

Original Exercise Instructions:
- Loop through each sublist of house
- Print "the x is y sqm" where x is room name, y is area
"""

# house list of lists (room name and area in sqm)
house = [
    ["hallway", 11.25],
    ["kitchen", 18.0],
    ["living room", 20.0],
    ["bedroom", 10.75],
    ["bathroom", 9.50]
]

# Build a for loop from scratch
for items in house:
    print("the " + str(items[0]) + " is " + str(items[1]) + " sqm")

# Key Takeaways:
# 1. Nested lists store structured data
# 2. items[0] accesses first element (room name)
# 3. items[1] accesses second element (area)
# 4. Each sublist can be unpacked: for room, area in house:
# 5. List of lists = primitive table structure (pre-pandas)