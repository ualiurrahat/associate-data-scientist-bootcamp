# -*- coding: utf-8 -*-

"""
Exercise: Familiar Functions
Course: Introduction to Python (DataCamp)
Section: Functions and Packages
Date: 2026-04-14
Student: Md. Ualiur Rahman Rahat

Description:
-----------
Python has many built-in functions that are available without importing anything.
Common built-in functions include: print(), type(), len(), int(), str(), float(), bool().
Functions take inputs (arguments) and may return outputs.

Key Concepts:
------------
1. type() - returns the data type of an object
2. len() - returns the length (number of items) of a sequence
3. int() - converts a value to an integer data type
4. Functions can be nested (e.g., print(type(var1)))

Original Exercise Instructions:
-------------------------------
1. Print the type of var1 using print() and type()
2. Print the length of var1 using len() inside print()
3. Convert var2 (boolean) to an integer and store in out2

Learning Note from Student:
--------------------------
Boolean to integer conversion: True becomes 1, False becomes 0.
This is useful in data science for converting categorical data.
"""

# Create variables var1 and var2
var1 = [1, 2, 3, 4]  # This is a list
var2 = True           # This is a boolean

# Print out type of var1
# type(var1) returns <class 'list'>, then print() displays it
print(type(var1))

# Print out length of var1
# len(var1) returns 4 (the list has 4 elements)
print(len(var1))

# Convert var2 to an integer: out2
# True converts to 1, False would convert to 0
out2 = int(var2)

# Verify the conversion
print(f"out2 value: {out2}")  # Output: 1
print(f"out2 type: {type(out2)}")  # Output: <class 'int'>


# ============================================================================
# Additional Practice (self-added):
# ============================================================================

# More built-in functions
print("\n--- More Built-in Functions ---")

# str() - convert to string
num = 42
num_str = str(num)
print(f"str(42) = '{num_str}' (type: {type(num_str)})")

# float() - convert to float
int_num = 10
float_num = float(int_num)
print(f"float(10) = {float_num} (type: {type(float_num)})")

# bool() - convert to boolean
print(f"bool(0) = {bool(0)}")      # False (zero is False)
print(f"bool(5) = {bool(5)}")      # True (non-zero is True)
print(f"bool('') = {bool('')}")    # False (empty string)
print(f"bool('hi') = {bool('hi')}")  # True (non-empty string)

# max() and min() - find extremes
numbers = [5, 2, 8, 1, 9]
print(f"max({numbers}) = {max(numbers)}")
print(f"min({numbers}) = {min(numbers)}")

# sum() - add all elements
print(f"sum({numbers}) = {sum(numbers)}")


# ============================================================================
# Key Takeaways:
# ============================================================================
# 1. Built-in functions are always available without importing
# 2. type() reveals what kind of data you're working with
# 3. len() works on sequences: lists, strings, tuples, etc.
# 4. Conversion functions: int(), float(), str(), bool()
# 5. Boolean to int: True = 1, False = 0 (useful for binary encoding)
# 6. Functions can be nested: print(type(x)) executes from innermost to outermost