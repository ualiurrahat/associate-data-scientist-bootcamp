# -*- coding: utf-8 -*-

"""
Exercise: Visualize all walks
Course: Intermediate Python (DataCamp)
Section: Case Study: Hacker Statistics
Date: 2026-04-25
Student: Md. Ualiur Rahman Rahat

Description:
Convert list of walks to NumPy array and transpose for proper visualization.

Key Concepts:
- np.array() converts list of lists to 2D array
- np.transpose() swaps rows and columns
- Proper orientation for plotting multiple time series

Original Exercise Instructions:
- Convert all_walks to NumPy array np_aw
- Plot np_aw (each walk as separate line)
- Clear plot with plt.clf()
- Transpose np_aw to np_aw_t and plot again
"""

import numpy as np
import matplotlib.pyplot as plt

# Set seed for reproducibility
np.random.seed(123)

# Initialize and populate all_walks
all_walks = []
for i in range(5):
    random_walk = [0]
    for x in range(100):
        step = random_walk[-1]
        dice = np.random.randint(1, 7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1, 7)
        random_walk.append(step)
    all_walks.append(random_walk)

# Convert all_walks to NumPy array: np_aw
np_aw = np.array(all_walks)
print(f"Shape before transpose: {np_aw.shape}")  # (5, 101)

# Plot np_aw and show (rows=walks, columns=steps - wrong orientation)
plt.plot(np_aw)
plt.title('Before Transpose (Each Row is a Walk)')
plt.show()

# Clear the figure
plt.clf()

# Transpose np_aw: np_aw_t (swap rows and columns)
np_aw_t = np.transpose(np_aw)
print(f"Shape after transpose: {np_aw_t.shape}")  # (101, 5)

# Plot np_aw_t and show (columns=walks, rows=steps - correct!)
plt.plot(np_aw_t)
plt.title('After Transpose (Each Column is a Walk)')
plt.xlabel('Step Number')
plt.ylabel('Position')
plt.show()

# Key Takeaways:
# 1. Original shape: (walks, steps) - wrong for plotting
# 2. Transposed shape: (steps, walks) - each column is one walk
# 3. plt.plot() expects each time series as column
# 4. Transpose aligns data for proper visualization
# 5. Shows all walks on same plot for comparison