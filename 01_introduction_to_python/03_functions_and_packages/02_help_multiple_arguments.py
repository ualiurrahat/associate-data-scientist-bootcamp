# -*- coding: utf-8 -*-

"""
Exercise: Help & Multiple Arguments
Course: Introduction to Python (DataCamp)
Section: Functions and Packages
Date: 2026-04-14
Student: Md. Ualiur Rahman Rahat

Description:
-----------
This exercise combines two concepts:
1. Using help() to understand function arguments
2. Understanding that sorted() takes multiple arguments including 'reverse'

The correct answer to the multiple-choice question is:
"pow() requires base and exp arguments; mod is optional"

Key Concepts:
------------
1. help() displays documentation for any function
2. pow(base, exp, mod) - mod is optional (defaults to None)
3. sorted(iterable, reverse=False) - reverse is optional
4. Optional arguments have default values shown in documentation

Original Exercise Instructions (Question):
-------------------------------------------
Which statement about pow() is true?
- pow() requires base and exp arguments; mod is optional ✓

Exercise 3 (Multiple arguments with sorted):
-------------------------------------------
1. Merge first and second lists using + operator
2. Sort the merged list in descending order (reverse=True)
3. Print the sorted list

Learning Note from Student:
--------------------------
The help() function is invaluable for exploring new functions.
sorted() with reverse=True is like sorting in descending order.
"""

# Exercise 3 code starts here

# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second using concatenation: full
full = first + second
print(f"Merged list (unsorted): {full}")

# Sort full in descending order: full_sorted
# reverse=True means largest to smallest
full_sorted = sorted(full, reverse=True)

# Print out full_sorted
print(f"Sorted descending: {full_sorted}")

# Bonus: sort ascending (default)
full_sorted_asc = sorted(full)
print(f"Sorted ascending: {full_sorted_asc}")


# ============================================================================
# Additional Practice (self-added):
# ============================================================================

print("\n--- Exploring sorted() Function ---")

# Different ways to use sorted()
numbers = [3, 1, 4, 1, 5, 9, 2]

# Default: ascending order
ascending = sorted(numbers)
print(f"Default (ascending): {ascending}")

# Descending order
descending = sorted(numbers, reverse=True)
print(f"Descending: {descending}")

# Sorted() works on strings too
words = ["banana", "apple", "cherry", "date"]
sorted_words = sorted(words)
print(f"Sorted words: {sorted_words}")

# Case-sensitive vs case-insensitive sorting
mixed_case = ["Apple", "banana", "Cherry", "date"]
print(f"Case-sensitive sort: {sorted(mixed_case)}")
print(f"Case-insensitive sort: {sorted(mixed_case, key=str.lower)}")

# pow() demonstration
print("\n--- pow() Function ---")
print(f"pow(2, 3) = {pow(2, 3)}")        # 2^3 = 8
print(f"pow(2, 3, 5) = {pow(2, 3, 5)}")  # (2^3) % 5 = 8 % 5 = 3


# ============================================================================
# Key Takeaways:
# ============================================================================
# 1. help() shows function documentation including required/optional arguments
# 2. sorted(iterable, reverse=True) sorts in descending order
# 3. The + operator concatenates (merges) two lists
# 4. sorted() returns a NEW list (original unchanged)
# 5. pow(base, exp, mod) - mod is optional, for modular exponentiation
# 6. Understanding optional arguments makes you a more flexible programmer