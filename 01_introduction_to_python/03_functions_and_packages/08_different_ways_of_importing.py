# -*- coding: utf-8 -*-

"""
Exercise: Different Ways of Importing
Course: Introduction to Python (DataCamp)
Section: Functions and Packages
Date: 2026-04-14
Student: Md. Ualiur Rahman Rahat

Description:
-----------
This exercise tests understanding of different import patterns.
The correct answer to the multiple-choice question is:

"from scipy.linalg import inv as my_inv"

Key Concepts:
------------
1. Import entire package: import scipy
2. Import subpackage: import scipy.linalg
3. Import specific function: from scipy.linalg import inv
4. Import with alias: from scipy.linalg import inv as my_inv

Original Exercise Instructions (Question):
------------------------------------------
Which import allows using the function as: my_inv([[1,2], [3,4]])?

Answer: from scipy.linalg import inv as my_inv ✓

Explanation:
- 'as my_inv' creates an alias (renames the function)
- Without alias, you'd call it 'inv()'
- With alias, you call it 'my_inv()'
- This is useful for avoiding naming conflicts or shortening names

Learning Note from Student:
--------------------------
Aliasing with 'as' is very common in data science:
- import pandas as pd
- import numpy as np
- import matplotlib.pyplot as plt
"""

# This is a demonstration - scipy may not be installed
# The actual code would be:
# from scipy.linalg import inv as my_inv
# result = my_inv([[1, 2], [3, 4]])

print("Demonstration of Import Aliasing")
print("=" * 50)
print("\nThe correct import statement is:")
print("from scipy.linalg import inv as my_inv")
print("\nThis allows calling the function as:")
print("my_inv([[1, 2], [3, 4]])")


# ============================================================================
# Additional Practice (self-added):
# ============================================================================

print("\n--- Common Import Aliases in Data Science ---")
print("import numpy as np           # NumPy for numerical computing")
print("import pandas as pd          # Pandas for data manipulation")
print("import matplotlib.pyplot as plt  # Plotting")
print("import seaborn as sns        # Statistical visualization")
print("import sklearn as sk         # Machine learning")

print("\n--- Import Patterns Comparison ---")

# Pattern 1: Direct import (no alias)
print("\n1. from math import sqrt")
print("   Use: sqrt(16)")

# Pattern 2: Import with alias
print("\n2. from math import sqrt as square_root")
print("   Use: square_root(16)")

# Pattern 3: Import package with alias
print("\n3. import math as m")
print("   Use: m.sqrt(16)")

# Pattern 4: Import submodule
print("\n4. from math import sqrt, pow, pi")
print("   Use: sqrt(16), pow(2,3), pi")

# Pattern 5: Import everything (not recommended)
print("\n5. from math import *")
print("   Use: sqrt(16) (but namespace pollution!)")

print("\n--- When to Use Aliases ---")

# Scenario: Avoid name conflict
def sqrt(x):
    """Custom sqrt function (different from math.sqrt)"""
    return x ** 0.5

# Import with alias to avoid conflict
from math import sqrt as math_sqrt

print(f"Custom sqrt(16): {sqrt(16)}")
print(f"Math sqrt(16): {math_sqrt(16)}")

# Scenario: Shorten long package names
# Instead of:
# import very_long_package_name_here
# very_long_package_name_here.some_function()

# Use:
# import very_long_package_name_here as vln
# vln.some_function()


# ============================================================================
# Key Takeaways:
# ============================================================================
# 1. 'as' creates an alias (renames the import)
# 2. Aliases help avoid naming conflicts
# 3. Common data science libraries use standard aliases (np, pd, plt)
# 4. from package.subpackage import function as alias
# 5. The question required 'my_inv' as the function name → use 'as my_inv'
# 6. Without 'as', you'd need to call it 'inv()', not 'my_inv()'
# 7. Aliases make code shorter while remaining readable (with standard conventions)