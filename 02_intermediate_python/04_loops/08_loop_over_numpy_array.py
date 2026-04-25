# -*- coding: utf-8 -*-

"""
Exercise: Loop over NumPy array
Course: Intermediate Python (DataCamp)
Section: Loops
Date: 2026-04-25
Student: Md. Ualiur Rahman Rahat

Description:
Loop through 1D and 2D NumPy arrays using different approaches.

Key Concepts:
- 1D arrays: direct iteration works like lists
- 2D arrays: need np.nditer() for element-wise iteration
- Proper array creation and manipulation

Original Exercise Instructions:
- Import numpy as np
- Loop over np_height printing "x inches"
- Loop over np_baseball using np.nditer()
"""

import numpy as np

# Create sample baseball data (heights in inches, weights in pounds)
np_height = np.array([74, 72, 75, 71, 73, 78, 70, 72, 76, 74])
np_baseball = np.column_stack((np_height, np.array([215, 210, 220, 195, 205, 230, 190, 200, 225, 215])))

# For loop over np_height (1D array)
print("Heights:")
for height in np_height:
    print(f"{height} inches")

print("\nAll baseball data (height, weight):")
# For loop over np_baseball (2D array) using nditer
for value in np.nditer(np_baseball):
    print(value)

# Key Takeaways:
# 1. 1D NumPy arrays behave like lists in for loops
# 2. 2D arrays: direct iteration loops over rows, not elements
# 3. np.nditer() flattens array for element-wise iteration
# 4. nditer works for any dimension array
# 5. NumPy operations are usually vectorized (avoid loops if possible)