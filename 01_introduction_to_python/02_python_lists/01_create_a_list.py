# -*- coding: utf-8 -*-

"""
Exercise: Create a List
Course: Introduction to Python (DataCamp)
Section: Python Lists
Date: 2026-04-11
Student: Md. Ualiur Rahman Rahat

Description:
-----------
A list is a compound data type that can group multiple values together.
Lists are created using square brackets [] with items separated by commas.
Lists can contain variables, literal values, or a mix of both.

Key Concepts:
------------
1. Lists are created with square brackets: [item1, item2, item3]
2. Lists can store variables (the variable's value gets stored, not the variable name)
3. Lists maintain the order of items as written
4. print() displays the entire list with brackets and commas

Original Exercise Instructions:
-------------------------------
1. Create a list 'areas' containing hallway, kitchen, living room, bedroom, bathroom areas (in order)
2. Use predefined variables: hall, kit, liv, bed, bath
3. Print the areas list

Learning Note from Student:
--------------------------
This is similar to arrays in C++ but more flexible:
- No fixed size needed
- Can mix different data types (as we'll see in next exercise)
- Square brackets [] instead of C++'s curly braces {} for array initialization
"""

# Predefined area measurements (all in square meters/feet - unit not specified)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create a list containing all five area values
# The order matches: hallway, kitchen, living room, bedroom, bathroom
areas = [hall, kit, liv, bed, bath]

# Print the entire list
# Output: [11.25, 18.0, 20.0, 10.75, 9.5]
print(areas)


# ============================================================================
# Additional Practice (self-added):
# ============================================================================

# Creating lists from literal values (no variables)
simple_list = [1, 2, 3, 4, 5]
print(f"\nSimple list: {simple_list}")

# Empty list (useful for building lists gradually)
empty_list = []
print(f"Empty list: {empty_list}")

# List with a single item (note the comma is optional for one item)
single_item = [42]
print(f"Single item list: {single_item}")

# Lists can hold any data type (demonstration)
mixed_list = [10, "text", 3.14, True]
print(f"Mixed types list: {mixed_list}")

# Check the type of a list
print(f"Type of 'areas': {type(areas)}")  # Output: <class 'list'>


# ============================================================================
# Key Takeaways:
# ============================================================================
# 1. Lists use square brackets [] and commas between items
# 2. Variables inside lists are evaluated to their values
# 3. Lists preserve the order you define
# 4. print(list) shows the entire list with brackets
# 5. Lists can be empty, have one item, or many items