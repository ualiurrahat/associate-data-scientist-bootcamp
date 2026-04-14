# -*- coding: utf-8 -*-

"""
Exercise: Selective Import
Course: Introduction to Python (DataCamp)
Section: Functions and Packages
Date: 2026-04-14
Student: Md. Ualiur Rahman Rahat

Description:
-----------
Selective imports allow you to import only specific functions from a package.
Syntax: from package import function
This allows you to use the function directly without package prefix.

Key Concepts:
------------
1. from math import pi - imports only pi (not entire math package)
2. Use pi directly, not math.pi
3. Saves typing and can make code cleaner
4. Multiple imports: from math import pi, sqrt, exp

Original Exercise Instructions:
-------------------------------
1. Selectively import only pi from math package
2. Use pi directly to calculate circumference and area

Learning Note from Student:
--------------------------
Trade-off:
- import math → math.pi (clearer where pi comes from)
- from math import pi → pi (shorter, but less explicit)
Both have their place depending on code context.
"""

# Import pi function from math package (selective import)
from math import pi

# Radius of the circle
radius = 0.43

# Calculate C (circumference) using pi directly (no math. prefix)
C = 2 * radius * pi

# Calculate A (area) using pi directly
A = pi * radius ** 2

print(f"Radius: {radius}")
print(f"Circumference: {C}")
print(f"Area: {A}")


# ============================================================================
# Additional Practice (self-added):
# ============================================================================

print("\n--- Multiple Selective Imports ---")

# Import multiple functions at once
from math import sqrt, pow, factorial, e

# Now use them directly
print(f"sqrt(25) = {sqrt(25)}")
print(f"pow(2, 10) = {pow(2, 10)}")
print(f"factorial(5) = {factorial(5)}")
print(f"e = {e}")

print("\n--- Import with Alias ---")

# Import with alias (rename) - useful for long names or avoiding conflicts
from math import sqrt as square_root
print(f"sqrt with alias: square_root(100) = {square_root(100)}")

print("\n--- Comparison of Import Styles ---")

# Style 1: Full import (explicit)
import math
print(f"Full import: math.sqrt(16) = {math.sqrt(16)}")

# Style 2: Selective import (direct)
from math import sqrt
print(f"Selective: sqrt(16) = {sqrt(16)}")

# Style 3: Import all (NOT recommended - pollutes namespace)
# from math import *  # Avoid this!
print("Avoid 'from math import *' - causes naming conflicts")

# When to use which style:
print("\n--- When to Use Each Import Style ---")
print("import math       : Use when using many math functions")
print("from math import x: Use when using 1-2 specific functions")
print("from math import *: NEVER (except interactive exploration)")
print("import math as m  : Use to shorten long package names")


# ============================================================================
# Key Takeaways:
# ============================================================================
# 1. 'from package import function' imports only specific items
# 2. Selective imports allow using function without package prefix
# 3. Multiple items: from math import pi, sqrt, exp
# 4. Aliases: from math import sqrt as sq (renames the import)
# 5. Avoid 'from package import *' (causes namespace pollution)
# 6. Selective imports are cleaner when you need few functions
# 7. Full imports are better when you need many functions from same package