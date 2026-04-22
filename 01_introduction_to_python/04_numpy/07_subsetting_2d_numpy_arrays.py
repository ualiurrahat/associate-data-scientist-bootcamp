# -*- coding: utf-8 -*-

"""
Exercise: Subsetting 2D NumPy Arrays
Course: Introduction to Python (DataCamp)
Section: NumPy
Date: 2026-04-14
Student: Md. Ualiur Rahman Rahat

Description:
-----------
2D array subsetting uses [rows, columns] syntax.
: means "all" (like slice everything).
Comma separates row selection from column selection.

Key Concepts:
------------
1. Syntax: array[rows, columns]
2. array[row_index, :] → entire row
3. array[:, column_index] → entire column
4. array[row_index, column_index] → single element
5. array[start:stop, start:stop] → submatrix

Original Exercise Instructions:
-------------------------------
1. Print the 50th row (index 49)
2. Create np_weight_lb from second column (index 1)
3. Print height of 124th player (index 123, column 0)

Learning Note from Student:
--------------------------
The comma is crucial! It's what distinguishes 2D from 1D subsetting.
: before comma = all rows, : after comma = all columns.
This is one of the most important NumPy patterns to memorize.
"""

import numpy as np

# Create sample data: 100 players, 3 columns (height, weight, age)
np.random.seed(42)
np_baseball = np.random.randint(65, 80, size=(100, 3))
np_baseball[:, 1] = np.random.randint(150, 250, 100)  # weight
np_baseball[:, 2] = np.random.randint(20, 40, 100)    # age

print("2D Array Subsetting Demonstration")
print("=" * 50)

# Print out the 50th row (index 49, since 0-based)
print(f"\n50th row (index 49): {np_baseball[49, :]}")
print(f"  → Height: {np_baseball[49, 0]} inches")
print(f"  → Weight: {np_baseball[49, 1]} lbs")
print(f"  → Age: {np_baseball[49, 2]} years")

# Select the entire second column (index 1) - weight column
np_weight_lb = np_baseball[:, 1]
print(f"\nSecond column (weights): {np_weight_lb[:10]}... (showing first 10)")
print(f"Weight column shape: {np_weight_lb.shape}")

# Print out height of 124th player
# Note: With 100 players, index 123 doesn't exist, so use index 23
if np_baseball.shape[0] > 123:
    height_124th = np_baseball[123, 0]
else:
    height_124th = np_baseball[23, 0]  # Using index 23 as example
    print(f"\nHeight of 24th player (index 23): {height_124th} inches")
    


# ============================================================================
# Additional Practice (self-added):
# ============================================================================

print("\n--- 2D Subsetting Patterns ---")

# Create a clear example matrix
matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12],
                   [13, 14, 15, 16]])
print("Matrix:")
print(matrix)

print("\n--- Row Selection ---")
print(f"Row 0 (first row): {matrix[0, :]}")
print(f"Row 2 (third row): {matrix[2, :]}")
print(f"Rows 1-2: {matrix[1:3, :]}")

print("\n--- Column Selection ---")
print(f"Column 0 (first column): {matrix[:, 0]}")
print(f"Column 2 (third column): {matrix[:, 2]}")
print(f"Columns 1-2: {matrix[:, 1:3]}")

print("\n--- Submatrix (rows AND columns) ---")
print(f"Rows 1-2, Columns 1-2:\n{matrix[1:3, 1:3]}")
print(f"First 2 rows, last 2 columns:\n{matrix[:2, 2:4]}")

print("\n--- Single Elements ---")
print(f"Element at (row 1, col 2): {matrix[1, 2]}")
print(f"Element at (row 3, col 0): {matrix[3, 0]}")

print("\n--- Fancy Indexing ---")
print(f"Rows [0,2], Columns [1,3]:\n{matrix[[0,2], :][:, [1,3]]}")
# Simpler: matrix[np.ix_([0,2], [1,3])]


# ============================================================================
# Key Takeaways:
# ============================================================================
# 1. 2D subsetting uses [rows, columns] with comma separator
# 2. : alone means "all" (all rows or all columns)
# 3. Single row: array[row_index, :]
# 4. Single column: array[:, column_index]
# 5. Submatrix: array[start:stop, start:stop]
# 6. Single element: array[row_index, column_index]
# 7. The comma is what makes it 2D subsetting!