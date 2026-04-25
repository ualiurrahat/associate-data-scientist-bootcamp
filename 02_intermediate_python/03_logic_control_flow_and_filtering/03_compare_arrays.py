# -*- coding: utf-8 -*-

"""
Exercise: Compare arrays
Course: Intermediate Python (DataCamp)
Section: Logic, Control Flow and Filtering
Date: 2026-04-25
Student: Md. Ualiur Rahman Rahat

Description:
Use comparison operators with NumPy arrays for element-wise comparisons.

Key Concepts:
- NumPy arrays support vectorized comparisons
- Comparison returns boolean array of same shape
- Element-wise operations: compares each corresponding element

Original Exercise Instructions:
- Which areas in my_house are >= 18?
- Which areas in my_house are smaller than your_house?
"""

import numpy as np

# Create arrays (areas of kitchen, living room, bedroom, bathroom)
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than or equal to 18
print(my_house >= 18)
# Returns: [ True  True False False]
# Kitchen(18) and Living(20) qualify

# my_house less than your_house
print(my_house < your_house)
# Returns: [False  True  True False]
# Living and Bedroom are smaller in my house

# Key Takeaways:
# 1. NumPy comparisons are element-wise (vectorized)
# 2. Output is boolean array with same length as input
# 3. No loops needed - much faster than Python lists
# 4. Can compare arrays directly (broadcasting rules apply)
# 5. Great for filtering data later