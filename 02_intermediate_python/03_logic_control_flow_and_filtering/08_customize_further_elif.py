# -*- coding: utf-8 -*-

"""
Exercise: Customize further: elif
Course: Intermediate Python (DataCamp)
Section: Logic, Control Flow and Filtering
Date: 2026-04-25
Student: Md. Ualiur Rahman Rahat

Description:
Use elif (else-if) to handle multiple conditions in a chain.

Key Concepts:
- elif = else if (combines else and if)
- Chain multiple conditions with elif
- First True condition's block executes, then exits
- Optional else at the end for "none of the above"

Original Exercise Instructions:
- Add elif to check if area > 10
- Print "medium size, nice!" for this case
"""

# Define variables
room = "bed"
area = 14.0

# if-elif-else construct for room
if room == "kit":
    print("looking around in the kitchen.")
elif room == "bed":
    print("looking around in the bedroom.")
else:
    print("looking around elsewhere.")

# if-elif-else construct for area
if area > 15:
    print("big place!")
elif area > 10:
    print("medium size, nice!")  # This runs (14 > 10)
else:
    print("pretty small.")

# Key Takeaways:
# 1. elif means "else if" - checks only if previous conditions False
# 2. Order matters: elif area > 10 then elif area > 15 would NEVER run
# 3. Check most specific conditions FIRST, general LAST
# 4. Can have multiple elif statements
# 5. elif is Python-specific (C++/JS use else if with space)