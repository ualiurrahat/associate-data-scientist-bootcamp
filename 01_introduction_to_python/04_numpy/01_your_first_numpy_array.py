# -*- coding: utf-8 -*-

"""
Exercise: Your First NumPy Array
Course: Introduction to Python (DataCamp)
Section: NumPy
Date: 2026-04-14
Student: Md. Ualiur Rahman Rahat

Description:
-----------
NumPy (Numerical Python) is a powerful package for numerical computing.
NumPy arrays are similar to Python lists but optimized for mathematical operations.
The standard convention is to import numpy as 'np'.

Key Concepts:
------------
1. Import convention: import numpy as np
2. np.array() converts a Python list to a NumPy array
3. NumPy arrays are homogeneous (all elements same type)
4. type() shows the data type (numpy.ndarray)

Original Exercise Instructions:
-------------------------------
1. Import numpy as np
2. Create numpy array from baseball list
3. Print the type of the numpy array

Learning Note from Student:
--------------------------
NumPy arrays are the foundation of data science in Python.
The 'as np' alias is universal - you'll see it everywhere.
"""

# Import the numpy package with standard alias 'np'
import numpy as np

# Regular Python list of baseball player heights (in cm)
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Create a numpy array from baseball: np_baseball
# np.array() converts Python list to NumPy array
np_baseball = np.array(baseball)

# Print out type of np_baseball
# Output: <class 'numpy.ndarray'>
print(type(np_baseball))

# Also print the array to see how it looks
print(f"NumPy array: {np_baseball}")


# ============================================================================
# Additional Practice (self-added):
# ============================================================================

# Creating numpy arrays from different data types
int_list = [1, 2, 3, 4, 5]
float_list = [1.5, 2.5, 3.5]
bool_list = [True, False, True]

np_ints = np.array(int_list)
np_floats = np.array(float_list)
np_bools = np.array(bool_list)

print(f"\nInteger array: {np_ints}")
print(f"Float array: {np_floats}")
print(f"Boolean array: {np_bools}")

# NumPy arrays are homogeneous (all elements same type)
# Mixed types get converted automatically
mixed = np.array([1, 2.5, 3])  # All become float
print(f"\nMixed types become float: {mixed}")
print(f"Data type: {mixed.dtype}")

# Creating arrays from ranges
range_array = np.arange(0, 10, 2)  # start, stop, step
print(f"\nnp.arange(0, 10, 2): {range_array}")

# Creating arrays of zeros or ones
zeros = np.zeros(5)
ones = np.ones(5)
print(f"np.zeros(5): {zeros}")
print(f"np.ones(5): {ones}")


# ============================================================================
# Key Takeaways:
# ============================================================================
# 1. Import numpy as np (standard convention used worldwide)
# 2. np.array(list) converts Python list to NumPy array
# 3. NumPy arrays have type numpy.ndarray
# 4. Arrays are homogeneous (unlike Python lists)
# 5. Mixed types get promoted (int → float → string)
# 6. NumPy is the foundation for pandas, scikit-learn, and many DS libraries