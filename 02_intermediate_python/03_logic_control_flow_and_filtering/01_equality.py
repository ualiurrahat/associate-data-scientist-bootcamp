# -*- coding: utf-8 -*-

"""
Exercise: Equality
Course: Intermediate Python (DataCamp)
Section: Logic, Control Flow and Filtering
Date: 2026-04-25
Student: Md. Ualiur Rahman Rahat

Description:
Learn to use equality (==) and inequality (!=) operators to compare values in Python.

Key Concepts:
- == checks if two values are equal (returns True/False)
- != checks if two values are NOT equal
- Different types can be compared (e.g., boolean vs integer)
- String comparison is case-sensitive

Original Exercise Instructions:
- Check if True equals False
- Check if -5 * 15 is not equal to 75
- Check if "pyscript" and "PyScript" are equal
- Compare boolean True with integer 1
"""

# Comparison of booleans
print(True == False)  # False - obviously not equal

# Comparison of integers
print(-5 * 15 != 75)  # True because -75 != 75

# Comparison of strings (case-sensitive!)
print("pyscript" == "PyScript")  # False - 'p' vs 'P' differs

# Compare a boolean with an integer
print(True == 1)  # True - In Python, True is 1, False is 0

# Key Takeaways:
# 1. == compares values, not memory locations (unlike JS)
# 2. In Python, True == 1 and False == 0 (unique to Python)
# 3. String comparison is case-sensitive by default
# 4. != is the opposite of ==
# 5. Comparison results are boolean (True/False)