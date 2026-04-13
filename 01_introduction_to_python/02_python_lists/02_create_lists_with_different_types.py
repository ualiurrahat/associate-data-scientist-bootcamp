# -*- coding: utf-8 -*-

"""
Exercise: Create Lists with Different Types
Course: Introduction to Python (DataCamp)
Section: Python Lists
Date: 2026-04-11
Student: Md. Ualiur Rahman Rahat

Description:
-----------
Lists in Python can contain mixed data types in the same list.
This is different from arrays in many other languages (like C++).
A single list can hold strings, integers, floats, booleans, and even other lists.

Key Concepts:
------------
1. Lists can mix data types: str, int, float, bool, etc.
2. Strings in lists must be in quotes (single or double)
3. Variables in lists are evaluated to their values
4. Alternating strings (room names) and floats (areas) creates labeled data

Original Exercise Instructions:
-------------------------------
1. Create a list that alternates: room name (string) then its area (float)
2. Add: "hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath
3. Print the list

Learning Note from Student:
--------------------------
This is powerful for data science:
- Each data point can have a label and a value in the same structure
- C++ arrays cannot mix types like this
- Python lists are heterogeneous (mixed types) vs homogeneous (same type)
"""

# Predefined area measurements
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list with alternating room names (strings) and areas (floats)
# Format: ["room_name", area, "room_name", area, ...]
areas = ["hallway", hall, 
         "kitchen", kit, 
         "living room", liv, 
         "bedroom", bed, 
         "bathroom", bath]

# Print the mixed-type list
# Output: ['hallway', 11.25, 'kitchen', 18.0, 'living room', 20.0, 'bedroom', 10.75, 'bathroom', 9.5]
print(areas)


# ============================================================================
# Additional Practice (self-added):
# ============================================================================

# Example of mixing multiple types in one list
mixed_list = ["Python", 3.9, True, 42, "Data Science", False]
print(f"\nMixed type list: {mixed_list}")

# Verifying each item's type
print("\nType of each item in mixed_list:")
for item in mixed_list:
    print(f"  {item}: {type(item).__name__}")

# Real-world example: storing student records
student = ["Rahat", 23, 3.73, True]  # [name, age, CGPA, is_enrolled]
print(f"\nStudent record: {student}")

# Lists can even store other lists (preview of next exercise)
nested_example = ["strings", [1, 2, 3], 3.14]
print(f"Nested list example: {nested_example}")


# ============================================================================
# Key Takeaways:
# ============================================================================
# 1. Python lists can hold mixed data types (heterogeneous)
# 2. This is different from C++ arrays which are homogeneous
# 3. Strings must be quoted, variables are evaluated
# 4. Mixed-type lists are useful for labeled data (e.g., name + value pairs)
# 5. Use type() to check what type each item in a list is