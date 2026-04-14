# -*- coding: utf-8 -*-

"""
Exercise: Subsetting NumPy Arrays
Course: Introduction to Python (DataCamp)
Section: NumPy
Date: 2026-04-14
Student: Md. Ualiur Rahman Rahat

Description:
-----------
Subsetting NumPy arrays uses the same square bracket notation as Python lists.
Single element: array[index]
Slicing: array[start:end] (end is exclusive)

Key Concepts:
------------
1. Indexing: array[index] for single element (0-based)
2. Slicing: array[start:stop] (stop is exclusive)
3. Works exactly like Python list subsetting
4. Can use negative indices: array[-1] for last element

Original Exercise Instructions:
-------------------------------
1. Print the weight at index 50
2. Print sub-array of heights from index 100 to 110 (inclusive)

Learning Note from Student:
--------------------------
NumPy subsetting is identical to list subsetting for 1D arrays.
The difference comes with 2D arrays (next exercise).
"""

import numpy as np

# Sample data (would be loaded from MLB data)
weight_lb = [180, 200, 190, 185, 195, 188, 210, 175, 192, 198, 205, 185, 
             190, 195, 200, 188, 192, 178, 202, 195, 188, 192, 185, 190]
height_in = [72, 74, 70, 69, 73, 71, 75, 68, 72, 74, 73, 71, 70, 72, 74, 
             69, 71, 70, 73, 72, 71, 70, 69, 72]

# Create numpy arrays
np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

# Print out the weight at index 50
# Note: With sample data, we'll use index 10 as demonstration
print(f"Weight at index 10: {np_weight_lb[10]} lbs")
print(f"Height at index 10: {np_height_in[10]} inches")

# Print out sub-array of np_height_in: index 10 up to and including index 15
# Slicing [10:16] includes indices 10,11,12,13,14,15 (16 is exclusive)
height_subset = np_height_in[10:16]
print(f"\nHeights from index 10 to 15: {height_subset}")


# ============================================================================
# Additional Practice (self-added):
# ============================================================================

print("\n--- 1D Array Subsetting Patterns ---")

# Create a simple array for demonstration
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print(f"Original array: {arr}")

# Single element access
print(f"\nSingle element access:")
print(f"  arr[0] = {arr[0]} (first element)")
print(f"  arr[4] = {arr[4]} (fifth element)")
print(f"  arr[-1] = {arr[-1]} (last element)")
print(f"  arr[-3] = {arr[-3]} (third from last)")

# Slicing
print(f"\nSlicing (start:stop):")
print(f"  arr[:5] = {arr[:5]} (first 5 elements)")
print(f"  arr[5:] = {arr[5:]} (elements from index 5 to end)")
print(f"  arr[3:7] = {arr[3:7]} (indices 3,4,5,6)")
print(f"  arr[::2] = {arr[::2]} (every 2nd element)")
print(f"  arr[::-1] = {arr[::-1]} (reverse order)")

# Boolean indexing (powerful NumPy feature)
print(f"\nBoolean indexing:")
bool_mask = arr > 50
print(f"  Mask (arr > 50): {bool_mask}")
print(f"  arr[arr > 50] = {arr[arr > 50]} (elements > 50)")


# ============================================================================
# Key Takeaways:
# ============================================================================
# 1. 1D NumPy arrays subset like Python lists
# 2. Use [index] for single element (0-based indexing)
# 3. Use [start:stop] for slicing (stop is exclusive)
# 4. Negative indices count from the end
# 5. [::step] allows skipping elements
# 6. Boolean indexing is unique to NumPy (very useful!)