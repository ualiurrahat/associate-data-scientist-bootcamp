# -*- coding: utf-8 -*-

"""
Exercise: Basic while loop
Course: Intermediate Python (DataCamp)
Section: Loops
Date: 2026-04-25
Student: Md. Ualiur Rahman Rahat

Description:
Implement a while loop that runs until a condition becomes False, decrementing a counter each iteration.

Key Concepts:
- while loop repeats while condition is True
- Loop variable must change inside loop to avoid infinite loop
- -= operator for decrement (offset = offset - 1)

Original Exercise Instructions:
- Create offset variable with initial value 8
- While offset != 0, print "correcting..."
- Decrease offset by 1 each iteration
- Print offset value each time
"""

# Initialize offset
offset = 8

# Code the while loop
while offset != 0:
    print("correcting...")
    offset -= 1  # Decrease by 1 each iteration
    print(offset)

# Key Takeaways:
# 1. while loop checks condition BEFORE each iteration
# 2. Must modify loop variable to eventually make condition False
# 3. offset -= 1 is shorthand for offset = offset - 1
# 4. Prints: correcting... 7, correcting... 6, ..., correcting... 0
# 5. Loop stops when offset becomes 0