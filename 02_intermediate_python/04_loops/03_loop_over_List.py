# -*- coding: utf-8 -*-

"""
Exercise: Loop over a list
Course: Intermediate Python (DataCamp)
Section: Loops
Date: 2026-04-25
Student: Md. Ualiur Rahman Rahat

Description:
Use a for loop to iterate through all elements of a list and print each one.

Key Concepts:
- for loop automatically iterates through sequence
- Loop variable takes each value in sequence
- No index needed for basic iteration

Original Exercise Instructions:
- Write for loop that iterates over all elements of areas list
- Print each element separately
"""

# areas list (room areas in sqm)
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for area in areas:
    print(area)

# Key Takeaways:
# 1. for loop syntax: for variable in iterable:
# 2. Loop variable gets each value one by one
# 3. No need to manage indices (unlike while loops)
# 4. Cleaner and more Pythonic than while for lists
# 5. Iterates through all elements automatically