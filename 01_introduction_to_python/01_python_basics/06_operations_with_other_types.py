#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Exercise: Operations with Other Types
Course: Introduction to Python (DataCamp)
Section: Python Basics
Date: 2026-04-11
Student: Md. Ualiur Rahman Rahat

Description:
-----------
Different data types behave differently with the same operators.
- int + int = int (addition)
- str + str = str (concatenation — strings are joined together)
- type() reveals what data type a variable is

Key Concepts:
------------
1. type() function returns the data type of a variable
2. + works differently for numbers (addition) vs strings (concatenation)
3. Different types cannot always be combined (TypeError)

Original Exercise Instructions:
-------------------------------
1. Add savings and new_savings to calculate total_savings
2. Use type() to print the type of total_savings
3. Add intro to itself and store in doubleintro
4. Print doubleintro

Learning Note from Student:
--------------------------
This was surprising: adding two strings just sticks them together!
In C++, 'string + string' does the same thing (concatenation).
But Python's type() function is very handy for debugging.
"""

# Pre-filled values from DataCamp
savings = 100
new_savings = 40

# Part 1: Integer addition
# Both are ints, so + performs mathematical addition
total_savings = savings + new_savings
print(total_savings)        # Output: 140

# Part 2: Check the type of total_savings
# Since both operands were ints, result is also int
print(type(total_savings))  # Output: <class 'int'>

# Part 3: String concatenation
intro = "Hello! How are you?"

# When using + with strings, they are concatenated (joined together)
# This does NOT add numbers — it combines text
doubleintro = intro + intro
print(doubleintro)          # Output: Hello! How are you?Hello! How are you?

# ============================================================================
# Additional Practice (self-added):
# ============================================================================

print("\n--- Type Exploration ---")

# Different types produce different type() results
example_int = 42
example_float = 3.14
example_str = "42"  # Note: this is text, not a number!
example_bool = True

print(f"42 is {type(example_int)}")
print(f"3.14 is {type(example_float)}")
print(f'"42" is {type(example_str)}')
print(f"True is {type(example_bool)}")

print("\n--- Type Behavior Differences ---")

# String multiplication (Python-specific feature!)
print("ha" * 3)              # Output: hahaha
print("=" * 20)              # Output: ====================

# What happens with mixed types? (Uncomment to see error)
# result = "100" + 50  # TypeError: can only concatenate str (not "int") to str

# Fix: convert types explicitly
str_to_int = int("100") + 50  # Convert string "100" to integer 100
print(f"After conversion: {str_to_int}")

# ============================================================================
# Key Takeaways:
# ============================================================================
# 1. type() reveals what kind of data a variable holds
# 2. + means addition for numbers, but concatenation for strings
# 3. Strings can be multiplied by integers (e.g., "hi" * 3 = "hihihi")
# 4. Cannot directly add different types (e.g., str + int) — convert first
# 5. Type matters — "5" (string) is different from 5 (integer)