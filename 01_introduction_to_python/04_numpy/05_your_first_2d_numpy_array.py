# -*- coding: utf-8 -*-

"""
Exercise: Your First 2D NumPy Array
Course: Introduction to Python (DataCamp)
Section: NumPy
Date: 2026-04-14
Student: Md. Ualiur Rahman Rahat

Description:
-----------
2D NumPy arrays represent matrices or tabular data.
They are created from lists of lists (each inner list = one row).
The .shape attribute returns (rows, columns).

Key Concepts:
------------
1. 2D array from list of lists: np.array([[row1], [row2]])
2. .shape attribute: (n_rows, n_columns)
3. Each inner list must have the same length
4. All elements must be same type (or coerced)

Original Exercise Instructions:
-------------------------------
1. Create 2D numpy array from baseball list of lists
2. Print the type of the array
3. Print the shape attribute

Learning Note from Student:
--------------------------
Shape is crucial for understanding your data dimensions.
(4, 2) means 4 rows (players) and 2 columns (height, weight)
This is the foundation of tabular data in data science.
"""

import numpy as np

# Baseball data: each sublist = [height (cm), weight (kg)]
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the type of np_baseball
print(f"Type: {type(np_baseball)}")
print(f"Data type of elements: {np_baseball.dtype}")

# Print out the shape of np_baseball
print(f"Shape: {np_baseball.shape}")  # (4, 2) = 4 rows, 2 columns

# Print the actual array
print(f"\nArray contents:")
print(np_baseball)


# ============================================================================
# Additional Practice (self-added):
# ============================================================================

print("\n--- Creating 2D Arrays ---")

# Different ways to create 2D arrays
# Method 1: From list of lists
matrix1 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])
print("Method 1 (list of lists):")
print(matrix1)
print(f"Shape: {matrix1.shape}")

# Method 2: Reshaping a 1D array
arr_1d = np.arange(12)  # [0,1,2,3,4,5,6,7,8,9,10,11]
matrix2 = arr_1d.reshape(3, 4)  # 3 rows, 4 columns
print(f"\nMethod 2 (reshape):\n{matrix2}")

# Method 3: Special arrays
zeros = np.zeros((3, 4))  # 3x4 matrix of zeros
ones = np.ones((2, 3))    # 2x3 matrix of ones
identity = np.eye(3)       # 3x3 identity matrix
print(f"\nMethod 3 (special arrays):")
print(f"np.zeros((3,4)):\n{zeros}")
print(f"\nnp.ones((2,3)):\n{ones}")
print(f"\nnp.eye(3):\n{identity}")

# Understanding shape
print("\n--- Understanding .shape ---")
print(f"matrix1 shape: {matrix1.shape} = {matrix1.shape[0]} rows, {matrix1.shape[1]} cols")
print(f"Total elements: {matrix1.size}")
print(f"Number of dimensions: {matrix1.ndim}")


# ============================================================================
# Key Takeaways:
# ============================================================================
# 1. 2D arrays = lists of lists (each inner list is a row)
# 2. .shape returns (rows, columns) - crucial for data understanding
# 3. .dtype shows the data type of elements
# 4. .size shows total number of elements (rows × columns)
# 5. .ndim shows number of dimensions (2 for 2D arrays)
# 6. 2D arrays are the foundation for pandas DataFrames