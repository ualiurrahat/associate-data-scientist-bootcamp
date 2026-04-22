# -*- coding: utf-8 -*-

"""
Exercise: 2D Arithmetic
Course: Introduction to Python (DataCamp)
Section: NumPy
Date: 2026-04-14
Student: Md. Ualiur Rahman Rahat

Description:
-----------
2D NumPy arrays support element-wise operations like 1D arrays.
Addition: array1 + array2 adds corresponding elements.
Multiplication: array * scalar multiplies every element.

Key Concepts:
------------
1. Element-wise addition: same shape arrays add position by position
2. Broadcasting: scalar multiplies all elements
3. Shape matters: arrays must have compatible shapes for operations

Original Exercise Instructions:
-------------------------------
1. Add np_baseball and updated arrays (player updates)
2. Create conversion array for metric conversion
3. Multiply np_baseball by conversion array

Learning Note from Student:
--------------------------
Broadcasting is powerful: [0.0254, 0.453592, 1] multiplies:
- Column 0 (height) by 0.0254 (inches → meters)
- Column 1 (weight) by 0.453592 (pounds → kg)
- Column 2 (age) by 1 (unchanged)
"""

import numpy as np

# Create sample baseball data: 10 players, 3 columns [height(in), weight(lb), age(years)]
np.random.seed(42)
np_baseball = np.random.randint(65, 80, size=(10, 3))
np_baseball[:, 1] = np.random.randint(150, 250, 10)
np_baseball[:, 2] = np.random.randint(20, 40, 10)

print("Original baseball data (inches, lbs, years):")
print(np_baseball)
print(f"Shape: {np_baseball.shape}")

# Create 'updated' array (changes in height, weight, age for each player)
# Simulating off-season changes
updated = np.random.randint(-2, 3, size=(10, 3))
print(f"\nUpdates (changes) array:")
print(updated)

# Add np_baseball and updated (element-wise addition)
np_baseball_updated = np_baseball + updated
print(f"\nAfter applying updates:")
print(np_baseball_updated)

# Create conversion array for metric conversion
# [height: inches→meters, weight: pounds→kilograms, age: unchanged]
conversion = np.array([0.0254, 0.453592, 1])

# Multiply np_baseball by conversion (broadcasting)
# Each column gets multiplied by its corresponding conversion factor
np_baseball_metric = np_baseball * conversion
print(f"\nAfter metric conversion (meters, kg, years):")
print(np_baseball_metric)


# ============================================================================
# Additional Practice (self-added):
# ============================================================================

print("\n--- 2D Array Operations ---")

# Element-wise operations on same shape arrays
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(f"A =\n{A}")
print(f"B =\n{B}")
print(f"A + B =\n{A + B}")
print(f"A * B =\n{A * B} (element-wise, NOT matrix multiplication)")
print(f"A / B =\n{A / B}")

# Matrix multiplication (dot product) - different from element-wise
print(f"\nMatrix multiplication A @ B:\n{A @ B}")

# Broadcasting examples
print("\n--- Broadcasting ---")
scalar = 2
print(f"A * {scalar} =\n{A * scalar}")

col_vector = np.array([10, 20])
print(f"A + {col_vector} (add to each col):\n{A + col_vector}")

row_vector = np.array([[10], [20]])
print(f"A + \n{row_vector} (add to each row):\n{A + row_vector}")

# Statistical operations on 2D arrays
print("\n--- Statistical Operations ---")
print(f"Mean of all values: {np.mean(np_baseball)}")
print(f"Mean of each column: {np.mean(np_baseball, axis=0)}")
print(f"Mean of each row: {np.mean(np_baseball, axis=1)}")
print(f"Sum of each column: {np.sum(np_baseball, axis=0)}")
print(f"Max of each column: {np.max(np_baseball, axis=0)}")


# ============================================================================
# Key Takeaways:
# ============================================================================
# 1. Array addition: element-wise (position by position)
# 2. Broadcasting: scalar applies to all elements
# 3. Array * array = element-wise multiplication (not matrix multiplication)
# 4. For matrix multiplication: use @ or np.dot()
# 5. axis=0 = column-wise operations, axis=1 = row-wise operations
# 6. Conversion arrays are powerful for unit transformations
# 7. Vectorized operations are much faster than loops