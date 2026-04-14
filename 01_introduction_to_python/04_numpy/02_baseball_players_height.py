# -*- coding: utf-8 -*-

"""
Exercise: Baseball Players' Height
Course: Introduction to Python (DataCamp)
Section: NumPy
Date: 2026-04-14
Student: Md. Ualiur Rahman Rahat

Description:
-----------
NumPy excels at vectorized operations - applying an operation to all elements at once.
This is much faster than using loops in pure Python.

Key Concepts:
------------
1. Vectorized operations: array * scalar applies to every element
2. No need for explicit loops (faster and cleaner)
3. 1 inch = 0.0254 meters (conversion factor)

Original Exercise Instructions:
-------------------------------
1. Create numpy array from height_in list
2. Print the array
3. Convert inches to meters using multiplication
4. Print the converted array

Learning Note from Student:
--------------------------
The beauty of NumPy: np_height_in * 0.0254 multiplies EVERY element!
In pure Python, you'd need a loop: [h * 0.0254 for h in height_in]
NumPy vectorization is much faster for large datasets.
"""

# Import numpy
import numpy as np

# Sample height data in inches (would be loaded from MLB data)
height_in = [72, 74, 70, 69, 73, 71, 75, 68, 72, 74]

# Create a numpy array from height_in: np_height_in
np_height_in = np.array(height_in)

# Print out np_height_in
print("Heights in inches:")
print(np_height_in)

# Convert np_height_in to meters: np_height_m
# Multiply every element by 0.0254 (inches to meters conversion)
np_height_m = np_height_in * 0.0254

# Print np_height_m
print("\nHeights in meters:")
print(np_height_m)


# ============================================================================
# Additional Practice (self-added):
# ============================================================================

print("\n--- Vectorized Operations ---")

# Multiple operations at once
np_height_cm = np_height_in * 2.54  # Inches to centimeters
print(f"Heights in cm: {np_height_cm}")

# Combining arrays (element-wise)
np_weight_kg = np.array([180, 200, 190, 185, 195, 188, 210, 175, 192, 198])
bmi = np_weight_kg / (np_height_m ** 2)  # BMI calculation vectorized!
print(f"BMI values: {bmi}")

# Comparison with pure Python loop (conceptual)
print("\nVectorized vs Loop (conceptual):")
print("NumPy vectorized: array * scalar (fast, C-optimized)")
print("Python loop: [x * 0.0254 for x in list] (slower)")

# Operations between arrays
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
print(f"\na = {a}")
print(f"b = {b}")
print(f"a + b = {a + b}")
print(f"a * b = {a * b}")
print(f"a ** b = {a ** b}")

# Universal functions (ufuncs)
print(f"\nnp.sqrt(a) = {np.sqrt(a)}")
print(f"np.exp(a) = {np.exp(a)}")
print(f"np.log(a) = {np.log(a)}")


# ============================================================================
# Key Takeaways:
# ============================================================================
# 1. NumPy vectorization: operation applies to ALL elements
# 2. array * scalar → multiply each element by scalar
# 3. array1 * array2 → element-wise multiplication
# 4. Vectorized operations are much faster than Python loops
# 5. Conversion factors (0.0254 for inches→meters) work element-wise
# 6. This is the foundation of efficient data science calculations