# -*- coding: utf-8 -*-

"""
Exercise: Indexes and values (2)
Course: Intermediate Python (DataCamp)
Section: Loops
Date: 2026-04-25
Student: Md. Ualiur Rahman Rahat

Description:
Start index at 1 instead of 0 for human-readable numbering.

Key Concepts:
- Add 1 to index for human-friendly counting
- convert numbers to strings for concatenation
- Alternative: f-strings with expressions

Original Exercise Instructions:
- Modify print so first output shows "room 1: 11.25"
- Room numbers should start at 1, not 0
"""

# areas list (room areas in sqm)
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop with index+1 for human-readable numbering
for index, area in enumerate(areas):
    print("room " + str(index + 1) + ": " + str(area))

# Alternative using f-string (more modern)
# print(f"room {index + 1}: {area}")

# Key Takeaways:
# 1. Computers count from 0, humans count from 1
# 2. index + 1 converts to human-readable format
# 3. Must convert numbers to strings when concatenating with +
# 4. f-strings handle conversion automatically
# 5. Small adjustments make output user-friendly