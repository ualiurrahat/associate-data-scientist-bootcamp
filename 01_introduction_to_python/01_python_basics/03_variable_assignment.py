# -*- coding: utf-8 -*-

"""
Exercise: Variable Assignment
Course: Introduction to Python (DataCamp)
Section: Python Basics
Date: 2026-04-11
Student: Md. Ualiur Rahman Rahat

Description:
-----------
Variables store values that can be used and reused later.
The assignment operator (=) gives a value to a variable name.
Unlike math, '=' means "assign" not "equals".

Key Concepts:
------------
1. Variable creation: name = value
2. Variables can be used in place of their values
3. print() displays whatever value the variable holds

Original Exercise Instructions:
-------------------------------
1. Create a variable 'savings' with value 100
2. Print the 'savings' variable

Learning Note from Student:
--------------------------
Very similar to C++ variable declaration but simpler:
- No need to specify data type (Python infers it)
- No semicolon required
- No 'int' keyword needed
"""

# Create a variable 'savings' and assign it the integer value 100
savings = 100

# Print the value stored in the 'savings' variable
# This will output: 100
print(savings)

# ============================================================================
# Additional Practice (self-added):
# ============================================================================

# Multiple assignments in one line (Python-specific feature)
x, y, z = 10, 20, 30
print(f"Multiple assignment: x={x}, y={y}, z={z}")

# Reassigning variables (old value is lost)
savings = 200
print(f"savings after reassignment: {savings}")

# ============================================================================
# Key Takeaways:
# ============================================================================
# 1. Python variables are created when you first assign a value to them
# 2. No declaration keyword needed (unlike C++'s 'int', 'float', etc.)
# 3. Variables can be reassigned to different values (and different types!)
# 4. '=' is assignment, not equality (that's '==' for comparison later)