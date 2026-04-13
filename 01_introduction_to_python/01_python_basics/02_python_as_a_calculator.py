# -*- coding: utf-8 -*-

"""
Exercise: Python as a Calculator
Course: Introduction to Python (DataCamp)
Section: Python Basics
Date: 2026-04-11
Student: Md. Ualiur Rahman Rahat

Description:
-----------
Python can perform basic arithmetic operations: addition (+), subtraction (-),
multiplication (*), and division (/). This exercise practices writing custom
print() statements with arithmetic inside.

Key Concepts:
------------
1. Python evaluates mathematical expressions following standard operator precedence
   (PEMDAS: Parentheses, Exponents, Multiplication/Division, Addition/Subtraction)
2. Each print() statement outputs on a new line
3. Comments (#) are ignored by Python — they're for humans to read

Original Exercise Instructions:
-------------------------------
1. Print the result of subtracting 5 from 5 under # Subtraction using print()
2. Print the result of multiplying 3 by 5 under # Multiplication

Learning Note from Student:
--------------------------
The code was pre-filled with addition (4+5) and division (10/2) examples.
I added subtraction (5-5) and multiplication (3*5) as instructed.
"""

# Example 1: Addition and Division (provided by DataCamp)
print(4 + 5)   # Addition: 4 + 5 = 9
print(10 / 2)  # Division: 10 / 2 = 5.0 (note: result is a float)

# Example 2: Subtraction (my solution to instruction #1)
print(5 - 5)   # Subtraction: 5 - 5 = 0

# Example 3: Multiplication (my solution to instruction #2)
print(3 * 5)   # Multiplication: 3 * 5 = 15

# ============================================================================
# Additional Practice (self-added after completing exercise):
# ============================================================================

print("\n--- Additional Practice ---")  # \n creates a new line

# Combining multiple operations in one print statement
print("Combined operations:")
print(5 + 3 * 2)      # Multiplication happens first: 3*2=6, then 5+6=11
print((5 + 3) * 2)    # Parentheses first: (5+3)=8, then 8*2=16

# Using variables to store results (preview of next section)
addition_result = 10 + 20
subtraction_result = 50 - 15
print(f"Addition: {addition_result}, Subtraction: {subtraction_result}")

# ============================================================================
# Key Takeaways:
# ============================================================================
# 1. Python can be used as an interactive calculator
# 2. Different operations have different precedence — use parentheses to control order
# 3. Comments help organize code and explain intent
# 4. print() can display numbers, strings, and results of calculations
# 5. Division always produces a float (decimal number) in Python 3