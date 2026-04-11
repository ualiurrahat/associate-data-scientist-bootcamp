#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Exercise: Extend a List
Course: Introduction to Python (DataCamp)
Section: Python Lists
Date: 2026-04-11
Student: Md. Ualiur Rahman Rahat

Description:
-----------
The + operator concatenates (joins) two lists into a new list.
Original lists remain unchanged — + creates a new list.
Can also use .extend() method to modify in-place.

Key Concepts:
------------
1. list1 + list2 creates a new combined list
2. Original lists are not modified
3. Can chain multiple + operations
4. Alternative: .append() for single item, .extend() for multiple

Original Exercise Instructions:
-------------------------------
1. Add ["poolhouse", 24.5] to areas → areas_1
2. Add ["garage", 15.45] to areas_1 → areas_2

Learning Note from Student:
--------------------------
C++ vector concatenation requires insert() or loop.
Python's + operator is very readable for list concatenation.
The + creates a copy (memory) — for large lists, .extend() is more efficient.
"""

# Create the areas list after previous changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

print("Original areas:")
print(areas)

# Add poolhouse data to areas, new list is areas_1
# + creates a NEW list (areas unchanged)
areas_1 = areas + ["poolhouse", 24.5]
print("\nAfter adding poolhouse (areas_1):")
print(areas_1)

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage", 15.45]
print("\nAfter adding garage (areas_2):")
print(areas_2)

# Verify original areas is unchanged
print("\nOriginal areas (still unchanged):")
print(areas)


# ============================================================================
# Additional Practice (self-added):
# ============================================================================

print("\n--- Different Ways to Extend Lists ---")

# Method 1: + operator (creates new list)
original = [1, 2, 3]
new_list = original + [4, 5]
print(f"Using + : {original} + [4,5] = {new_list}")
print(f"Original unchanged: {original}")

# Method 2: .extend() method (modifies original in-place)
original.extend([6, 7])
print(f"\nUsing .extend(): {original}")

# Method 3: .append() for single items
original.append(8)
print(f"Using .append(): {original}")

# Method 4: Using += operator (same as .extend() for lists)
original += [9, 10]
print(f"Using += : {original}")

# Performance note for data science (large lists):
# .extend() is more memory-efficient than + for large lists
# + creates a copy, .extend() modifies in-place


# ============================================================================
# Key Takeaways:
# ============================================================================
# 1. + concatenates lists into a NEW list
# 2. Original lists remain unchanged when using +
# 3. .extend() modifies the original list (no copy)
# 4. .append() adds a single element
# 5. For data science with large datasets, prefer .extend() for memory efficiency