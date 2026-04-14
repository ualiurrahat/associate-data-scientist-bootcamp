# -*- coding: utf-8 -*-

"""
Exercise: Baseball Data in 2D Form
Course: Introduction to Python (DataCamp)
Section: NumPy
Date: 2026-04-14
Student: Md. Ualiur Rahman Rahat

Description:
-----------
Converting data to 2D NumPy arrays unlocks powerful operations.
The shape attribute reveals the structure of your data.

Key Concepts:
------------
1. 2D arrays from nested lists
2. .shape attribute shows dimensions
3. Structured data = rows (observations) × columns (features)

Original Exercise Instructions:
-------------------------------
1. Create 2D numpy array from baseball (list of lists)
2. Print the shape attribute

Learning Note from Student:
--------------------------
In data science terminology:
- Each row = one observation (one baseball player)
- Each column = one feature (height, weight, age, etc.)
Understanding shape is the first step in EDA (Exploratory Data Analysis)
"""

import numpy as np

# Baseball data would be loaded from MLB database
# This is sample data - real data would have 1000+ rows
baseball = [
    [72, 180],   # Player 1: height 72in, weight 180lb
    [74, 200],   # Player 2: height 74in, weight 200lb
    [70, 190],   # Player 3
    [69, 185],   # Player 4
    [73, 195],   # Player 5
    [71, 188],   # Player 6
    [75, 210],   # Player 7
    [68, 175],   # Player 8
]

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the shape of np_baseball
print(f"Shape of np_baseball: {np_baseball.shape}")
print(f"  → {np_baseball.shape[0]} players (rows)")
print(f"  → {np_baseball.shape[1]} measurements per player (columns)")
print(f"  → Total data points: {np_baseball.size}")

# Print first few rows to see structure
print(f"\nFirst 5 rows of data:")
print(np_baseball[:5])


# ============================================================================
# Additional Practice (self-added):
# ============================================================================

print("\n--- Working with 2D Array Shape ---")

# Create a larger sample dataset
np.random.seed(42)  # For reproducibility
n_players = 100
np_baseball_large = np.random.randint(65, 80, size=(n_players, 3))  # 100 players, 3 features
# Add column names for context
print(f"Large dataset shape: {np_baseball_large.shape}")
print(f"  {np_baseball_large.shape[0]} observations (players)")
print(f"  {np_baseball_large.shape[1]} features (height, weight, age)")

# Reshape operations
print(f"\nReshaping examples:")
arr = np.arange(12)
print(f"Original 1D: {arr}, shape: {arr.shape}")

arr_2d = arr.reshape(3, 4)
print(f"Reshape to (3,4):\n{arr_2d}")

arr_2d_alt = arr.reshape(4, 3)
print(f"\nReshape to (4,3):\n{arr_2d_alt}")

arr_2d_auto = arr.reshape(2, -1)  # -1 auto-calculates dimension
print(f"\nReshape with -1 (auto): {arr_2d_auto.shape}")

# Flattening 2D back to 1D
flattened = arr_2d.flatten()
print(f"\nFlattened: {flattened}")


# ============================================================================
# Key Takeaways:
# ============================================================================
# 1. .shape returns (rows, columns) for 2D arrays
# 2. Rows = observations/players/samples
# 3. Columns = features/measurements/variables
# 4. .size = rows × columns (total data points)
# 5. reshape() changes dimensions while preserving data
# 6. flatten() converts 2D array to 1D
# 7. Understanding shape is essential for data manipulation