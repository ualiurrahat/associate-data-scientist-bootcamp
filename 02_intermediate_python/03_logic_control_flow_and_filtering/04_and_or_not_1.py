# -*- coding: utf-8 -*-

"""
Exercise: and, or, not (1)
Course: Intermediate Python (DataCamp)
Section: Logic, Control Flow and Filtering
Date: 2026-04-25
Student: Md. Ualiur Rahman Rahat

Description:
Combine multiple conditions using logical operators and, or, not.

Key Concepts:
- and: True only if BOTH conditions are True
- or: True if AT LEAST ONE condition is True
- not: reverses boolean (True becomes False, False becomes True)
- Operator precedence: not > and > or

Original Exercise Instructions:
- Check if my_kitchen > 10 AND < 18
- Check if my_kitchen < 14 OR > 17
- Check if 2*my_kitchen < 3*your_kitchen
"""

# Define variables
my_kitchen = 18.0
your_kitchen = 14.0

# my_kitchen bigger than 10 and smaller than 18?
print(my_kitchen > 10 and my_kitchen < 18)
# 18 > 10 True, 18 < 18 False -> True and False = False

# my_kitchen smaller than 14 or bigger than 17?
print(my_kitchen < 14 or my_kitchen > 17)
# 18 < 14 False, 18 > 17 True -> False or True = True

# Double my_kitchen smaller than triple your_kitchen?
print(my_kitchen * 2 < your_kitchen * 3)
# 36 < 42? True

# Key Takeaways:
# 1. Logical operators combine boolean expressions
# 2. Python uses short-circuit evaluation (stops early if possible)
# 3. In Python: 'and' and 'or' are keywords (not && or || like C++/JS)
# 4. Group conditions with parentheses when mixing operators
# 5. Can combine as many conditions as needed