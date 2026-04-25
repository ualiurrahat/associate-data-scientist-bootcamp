# -*- coding: utf-8 -*-

"""
Exercise: Add else
Course: Intermediate Python (DataCamp)
Section: Logic, Control Flow and Filtering
Date: 2026-04-25
Student: Md. Ualiur Rahman Rahat

Description:
Add else clauses to handle both True and False cases of conditions.

Key Concepts:
- if-else: executes one block or the other (not both)
- else covers all remaining cases
- Only one block executes in if-else

Original Exercise Instructions:
- Add else to area control structure
- Print "pretty small" if area not > 15
"""

# Define variables
room = "kit"
area = 14.0

# if-else construct for room
if room == "kit":
    print("looking around in the kitchen.")
else:
    print("looking around elsewhere.")

# if-else construct for area
if area > 15:
    print("big place!")
else:
    print("pretty small.")  # This runs because area=14.0

# Key Takeaways:
# 1. if-else = exactly two mutually exclusive paths
# 2. else has no condition (executes when if condition is False)
# 3. Only ONE of if or else blocks executes
# 4. else is optional (can have if without else)
# 5. else aligns with its if (same indentation level)