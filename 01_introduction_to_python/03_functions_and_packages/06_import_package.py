# -*- coding: utf-8 -*-

"""
Exercise: Import Package
Course: Introduction to Python (DataCamp)
Section: Functions and Packages
Date: 2026-04-14
Student: Md. Ualiur Rahman Rahat

Description:
-----------
Packages are collections of modules that contain functions, classes, and variables.
The math package provides mathematical constants and functions.
Use 'import package_name' to access everything in the package.

Key Concepts:
------------
1. import math - makes all math functions available
2. Access functions using dot notation: math.pi, math.sqrt()
3. Constants like pi are attributes of the math package
4. ** is exponentiation operator (power)

Original Exercise Instructions:
-------------------------------
1. Import the math package
2. Calculate circumference: C = 2 * radius * pi
3. Calculate area: A = pi * radius**2
4. Print both results

Learning Note from Student:
--------------------------
Circumference formula: 2πr
Area formula: πr²
Using math.pi is more accurate than typing 3.14
"""

# Import the math package
import math

# Radius of the circle
radius = 0.43

# Calculate C (circumference): 2 * π * r
C = 2 * radius * math.pi

# Calculate A (area): π * r²
# ** is exponentiation: radius**2 means radius squared
A = math.pi * radius ** 2

print(f"Radius: {radius}")
print(f"Circumference: {C}")
print(f"Area: {A}")


# ============================================================================
# Additional Practice (self-added):
# ============================================================================

print("\n--- More math Package Functions ---")

# Square root
print(f"math.sqrt(16) = {math.sqrt(16)}")

# Trigonometric functions (angles in radians)
angle_degrees = 45
angle_radians = math.radians(angle_degrees)
print(f"sin({angle_degrees}°) = {math.sin(angle_radians)}")
print(f"cos({angle_degrees}°) = {math.cos(angle_radians)}")

# Constants
print(f"math.pi = {math.pi}")
print(f"math.e = {math.e}")  # Euler's number
print(f"math.tau = {math.tau}")  # 2π (tau constant)

# Logarithmic functions
print(f"math.log(100, 10) = {math.log(100, 10)}")  # log base 10
print(f"math.log(16, 2) = {math.log(16, 2)}")      # log base 2
print(f"math.log1p(0.095) = {math.log1p(0.095)}")  # log(1+x) (accurate for small x)

# Exponential
print(f"math.exp(2) = {math.exp(2)}")  # e^2
print(f"math.expm1(0.095) = {math.expm1(0.095)}")  # e^x - 1 (accurate for small x)

# Rounding
x = 3.14159
print(f"math.floor({x}) = {math.floor(x)}")  # Round down
print(f"math.ceil({x}) = {math.ceil(x)}")    # Round up
print(f"math.trunc({x}) = {math.trunc(x)}")  # Truncate decimal


# ============================================================================
# Key Takeaways:
# ============================================================================
# 1. Use 'import package' to import entire package
# 2. Access package contents with dot notation: package.function()
# 3. math.pi is more precise than typing 3.14
# 4. ** is exponentiation operator (a**b = a to the power b)
# 5. Packages organize code into reusable modules
# 6. The math package has many useful functions: sqrt, sin, cos, log, etc.