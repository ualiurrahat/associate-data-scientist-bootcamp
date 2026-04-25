# -*- coding: utf-8 -*-

"""
Exercise: if
Course: Intermediate Python (DataCamp)
Section: Logic, Control Flow and Filtering
Date: 2026-04-25
Student: Md. Ualiur Rahman Rahat

Description:
Use if statements to execute code conditionally based on boolean expressions.

Key Concepts:
- if statement syntax: if condition:
- Indentation matters (4 spaces standard)
- Block executes only if condition is True

Original Exercise Instructions:
- Write if statement that prints for kitchen (room == "kit")
- Write if statement that prints "big place!" if area > 15
"""

# Define variables
room = "kit"
area = 14.0

# if statement for room
if room == "kit":
    print("looking around in the kitchen.")

# if statement for area
if area > 15:
    print("big place!")

# This second if condition is False (14.0 > 15), so nothing prints

# Key Takeaways:
# 1. Colon (:) ends condition line, required syntax
# 2. Indentation defines code block (unlike C++ which uses braces)
# 3. 4 spaces is PEP 8 standard
# 4. Multiple if statements run independently
# 5. No parentheses needed around condition (unlike C++/JS)