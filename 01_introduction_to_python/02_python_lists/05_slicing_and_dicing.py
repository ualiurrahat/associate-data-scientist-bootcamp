#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Exercise: Slicing and Dicing
Course: Introduction to Python (DataCamp)
Section: Python Lists
Date: 2026-04-11
Student: Md. Ualiur Rahman Rahat

Description:
-----------
Slicing selects multiple elements from a list using [start:end] syntax.
Start index is INCLUDED, end index is EXCLUDED.
Omitting start means "from beginning", omitting end means "until end".

Key Concepts:
------------
1. Syntax: list[start:end] (end is exclusive)
2. list[:n] = first n elements (from beginning to index n-1)
3. list[n:] = elements from index n to end
4. list[:] = full copy of list
5. Slicing never raises IndexError (returns empty list if out of bounds)

Original Exercise Instructions:
-------------------------------
1. Create 'downstairs' with first 6 elements of areas
2. Create 'upstairs' with last 4 elements (using slice without end index)
3. Print both lists

Learning Note from Student:
--------------------------
C++ doesn't have built-in slicing (requires loops or copy algorithms).
Python's slicing is very readable and powerful for data manipulation.
The exclusive end index takes getting used to (off-by-one awareness).
"""

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, 
         "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs (first 6 elements)
# Start omitted (default 0), end = 6 (stops BEFORE index 6)
downstairs = areas[:6]

# Use slicing to create upstairs (last 4 elements)
# Start = 6 (from index 6 onward), end omitted (goes to end)
upstairs = areas[6:]

# Print out downstairs and upstairs
print("Downstairs:", downstairs)
print("Upstairs:", upstairs)


# ============================================================================
# Additional Practice (self-added):
# ============================================================================

print("\n--- Slicing Exploration ---")

# Different slice patterns
print(f"Full list: {areas[:]}")           # Entire list (copy)
print(f"First 3 elements: {areas[:3]}")   # Indices 0,1,2
print(f"Last 3 elements: {areas[-3:]}")   # Indices -3,-2,-1
print(f"Middle 4 elements: {areas[3:7]}") # Indices 3,4,5,6
print(f"Every other element: {areas[::2]}")  # Step of 2 (preview of extended slicing)

# Slicing with negative indices
print(f"From index -5 to end: {areas[-5:]}")

# Slicing beyond bounds (no error, returns what exists)
print(f"Beyond bounds (safe): {areas[15:20]}")  # Returns empty list

# Practical use: Getting first and last elements using slices
first_three = areas[:3]
last_three = areas[-3:]
print(f"\nFirst three: {first_three}")
print(f"Last three: {last_three}")


# ============================================================================
# Key Takeaways:
# ============================================================================
# 1. Slicing uses [start:end] where end is EXCLUDED
# 2. Omitted start = beginning of list
# 3. Omitted end = end of list
# 4. Slicing is safe (never causes IndexError)
# 5. Creates a NEW list (doesn't modify original)
# 6. Useful for splitting data into training/test sets (data science)