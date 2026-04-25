# -*- coding: utf-8 -*-

"""
Exercise: Greater and less than
Course: Intermediate Python (DataCamp)
Section: Logic, Control Flow and Filtering
Date: 2026-04-25
Student: Md. Ualiur Rahman Rahat

Description:
Use comparison operators (<, >, <=, >=) to compare numbers and strings.

Key Concepts:
- < less than, > greater than
- <= less than or equal, >= greater than or equal
- Strings compared alphabetically (lexicographical order)
- Booleans: True=1, False=0 for comparisons

Original Exercise Instructions:
- Check if x (pre-defined) is greater than or equal to -10
- Check if "test" is less than or equal to y (pre-defined)
- Check if True is greater than False
"""

# Comparison of integers
x = -3 * 6  # x = -18
print(x >= -10)  # -18 >= -10? False (more negative is smaller)

# Comparison of strings
y = "test"
print("test" <= y)  # "test" <= "test"? True (equal)

# Comparison of booleans
print(True > False)  # 1 > 0? True

# Key Takeaways:
# 1. Negative numbers: -18 is LESS than -10 (more negative = smaller)
# 2. String comparison uses alphabetical order (ASCII/Unicode values)
# 3. Booleans act like numbers (True=1, False=0) in comparisons
# 4. <= and >= include equality, < and > don't
# 5. Cannot compare strings with numbers (TypeError)