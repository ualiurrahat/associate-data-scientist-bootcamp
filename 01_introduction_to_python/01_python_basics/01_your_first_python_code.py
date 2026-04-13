# -*- coding: utf-8 -*-

"""
Exercise: Your First Python Code
Course: Introduction to Python (DataCamp)
Section: Python Basics
Date: 2026-04-11
Student: Md. Ualiur Rahman Rahat

Description:
-----------
This is the traditional "first program" exercise in Python.
The goal is simply to run existing code and observe the output.
No new code needs to be written — just understand that print() displays output.

Key Concept:
-----------
print() is a built-in Python function that outputs text or values to the console.
Anything inside the parentheses is evaluated first, then displayed.

Original Exercise Instructions:
-------------------------------
Hit the run code button to see the output of print(5 / 8).

Learning Note from Student:
--------------------------
Coming from C++ background, I notice Python's print() is simpler — no need for
std::cout or << operators. The syntax is more readable.
"""

# The print() function evaluates 5 / 8 (which equals 0.625) and displays it
print(5 / 8)

# ============================================================================
# Additional Practice (self-added after completing exercise):
# ============================================================================

# Print different arithmetic operations to see how print() handles them
print(10 + 3)   # Addition
print(10 - 3)   # Subtraction
print(10 * 3)   # Multiplication
print(10 / 3)   # Division (returns float: 3.333...)
print(10 // 3)  # Integer division (returns int: 3)
print(10 % 3)   # Modulo (returns remainder: 1)

# ============================================================================
# Key Takeaways:
# ============================================================================
# 1. print() is the most basic way to see output in Python
# 2. Python can evaluate expressions inside print() before displaying them
# 3. Division (/) always returns a float, even if the result is a whole number