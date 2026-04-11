#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Exercise: Other Variable Types
Course: Introduction to Python (DataCamp)
Section: Python Basics
Date: 2026-04-11
Student: Md. Ualiur Rahman Rahat

Description:
-----------
Python has several built-in data types beyond integers (int).
The most common are:
- float: decimal numbers (e.g., 3.14, 0.5, -2.7)
- str: text/strings (e.g., "Hello", 'Python', "123")
- bool: logical True/False values (note capital T and F)

Key Concepts:
------------
1. float: numbers with decimal points
2. str: text inside quotes (single '' or double "")
3. bool: only True or False (not true/false/TRUE/FALSE)

Original Exercise Instructions:
-------------------------------
1. Create float 'half' with value 0.5
2. Create string 'intro' with value "Hello! How are you?"
3. Create boolean 'is_good' with value True

Learning Note from Student:
--------------------------
Unlike C++:
- Python strings can use single OR double quotes (C++ primarily double)
- Boolean values are True/False (C++ uses true/false lowercase)
- No need for 'std::string' or special includes
"""

# Float: numbers with decimal points
half = 0.5

# String: text enclosed in quotes (double quotes used here)
intro = "Hello! How are you?"

# Boolean: logical values (must be capitalized)
is_good = True

# Print all three to verify
print(f"half (float): {half}")
print(f"intro (string): {intro}")
print(f"is_good (boolean): {is_good}")

# ============================================================================
# Additional Practice (self-added):
# ============================================================================

# Different ways to create strings
single_quoted = 'Single quotes work too'
double_quoted = "Double quotes are common"
multi_line = """This string
spans multiple
lines"""

print(f"\nString variations:")
print(f"Single: {single_quoted}")
print(f"Double: {double_quoted}")
print(f"Multi-line:\n{multi_line}")

# Boolean operations (preview of logical operators)
print(f"\nBoolean basics:")
print(f"True and False: {True and False}")
print(f"True or False: {True or False}")
print(f"not True: {not True}")

# Check types using type() function
print(f"\nType checking:")
print(f"half is {type(half)}")
print(f"intro is {type(intro)}")
print(f"is_good is {type(is_good)}")

# ============================================================================
# Key Takeaways:
# ============================================================================
# 1. Python has multiple data types for different kinds of data
# 2. float = decimal numbers, str = text, bool = True/False
# 3. Strings can use 'single' or "double" quotes — be consistent
# 4. Boolean values MUST be capitalized (True/False, not true/false)
# 5. Use type() to check what type a variable is