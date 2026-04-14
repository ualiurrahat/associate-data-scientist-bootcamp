# -*- coding: utf-8 -*-

"""
Exercise: List Methods
Course: Introduction to Python (DataCamp)
Section: Functions and Packages
Date: 2026-04-14
Student: Md. Ualiur Rahman Rahat

Description:
-----------
Lists have methods that help find and count elements.
Unlike strings, many list methods modify the list in-place.

Key Concepts:
------------
1. .index(value) - returns first index where value appears
2. .count(value) - returns number of times value appears
3. Both methods work on any list type (numbers, strings, etc.)
4. .index() raises ValueError if value not found

Original Exercise Instructions:
-------------------------------
1. Use .index() to find where 20.0 appears in areas list
2. Use .count() to count how many times 9.50 appears

Learning Note from Student:
--------------------------
.index() returns the position (0-based index), not the value.
Useful for finding where specific data points are located.
"""

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
# 20.0 is at position/index 2 (0-based indexing)
index_of_20 = areas.index(20.0)
print(f"Index of 20.0: {index_of_20}")

# Print out how often 9.50 appears in areas
# 9.50 appears once in the list
count_of_9_50 = areas.count(9.50)
print(f"Count of 9.50: {count_of_9_50}")


# ============================================================================
# Additional Practice (self-added):
# ============================================================================

print("\n--- More List Methods ---")

# .index() with duplicate values
duplicate_list = [1, 2, 3, 2, 4, 2, 5]
print(f"List with duplicates: {duplicate_list}")
print(f"First occurrence of 2: index {duplicate_list.index(2)}")

# .count() on various lists
print(f"Count of 2: {duplicate_list.count(2)}")
print(f"Count of 1: {duplicate_list.count(1)}")
print(f"Count of 99 (not present): {duplicate_list.count(99)}")

# .index() with strings
fruits = ["apple", "banana", "cherry", "banana"]
print(f"\nFruits list: {fruits}")
print(f"Index of 'banana': {fruits.index('banana')}")  # Returns first occurrence only

# Handling .index() when value doesn't exist (uncomment to see error)
# print(fruits.index('grape'))  # ValueError: 'grape' is not in list

# Safe way to use .index()
def safe_index(lst, value):
    """Return index if value exists, otherwise -1"""
    try:
        return lst.index(value)
    except ValueError:
        return -1

print(f"Safe index of 'grape': {safe_index(fruits, 'grape')}")

# Practical data science use: finding outliers
data = [10, 12, 11, 99, 13, 12, 10]
outlier = 99
outlier_index = data.index(outlier)
print(f"\nOutlier {outlier} found at index {outlier_index}")


# ============================================================================
# Key Takeaways:
# ============================================================================
# 1. .index() returns the FIRST occurrence's position (0-based)
# 2. .count() returns frequency count (0 if not present)
# 3. Both work on any data type in the list
# 4. .index() raises ValueError if value not found (handle with try/except)
# 5. Useful for data exploration: finding where certain values are located
# 6. For last occurrence, you'd need to reverse the list or loop through