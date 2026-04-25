# -*- coding: utf-8 -*-

"""
Exercise: Add conditionals
Course: Intermediate Python (DataCamp)
Section: Loops
Date: 2026-04-25
Student: Md. Ualiur Rahman Rahat

Description:
Add if-else logic inside while loop to handle negative offsets by increasing toward zero.

Key Concepts:
- while loop with conditional logic inside
- Handle positive and negative cases differently
- Move toward zero from either direction

Original Exercise Instructions:
- Initialize offset to -6
- Inside while loop: if offset > 0, decrease by 1; else increase by 1
- Print "correcting..." and offset each iteration
"""

# Initialize offset (negative value)
offset = -6

# Code the while loop
while offset != 0:
    print("correcting...")
    if offset > 0:
        offset -= 1  # Move down toward zero
    else:
        offset += 1  # Move up toward zero
    print(offset)

# Key Takeaways:
# 1. Without if-else, negative offset would go to -7, -8, etc. (infinite!)
# 2. if-else ensures we always move TOWARD zero
# 3. Prints: correcting... -5, -4, -3, -2, -1, 0 then stops
# 4. Same logic works for positive or negative starting values
# 5. Always ensure loop variable changes AND eventually reaches stop condition