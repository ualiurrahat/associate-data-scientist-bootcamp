# -*- coding: utf-8 -*-

"""
Exercise: Indexes and values (1)
Course: Intermediate Python (DataCamp)
Section: Loops
Date: 2026-04-25
Student: Md. Ualiur Rahman Rahat

Description:
Use enumerate() to access both index and value when iterating through a list.

Key Concepts:
- enumerate() returns tuples of (index, value)
- Can unpack tuple into two loop variables
- Useful when position matters

Original Exercise Instructions:
- Use enumerate() with two iterator variables
- Print "room x: y" where x is index, y is area
"""

# areas list (room areas in sqm)
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for index, area in enumerate(areas):
    print(f"room {index}: {area}")

# Key Takeaways:
# 1. enumerate() adds counter to iteration
# 2. Returns (0, 11.25), (1, 18.0), (2, 20.0), etc.
# 3. Unpack into index, value variables
# 4. Much cleaner than range(len(areas)) pattern
# 5. f-string formatting makes code readable