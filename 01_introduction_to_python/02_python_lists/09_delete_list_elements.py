# -*- coding: utf-8 -*-

"""
Exercise: Delete List Elements
Course: Introduction to Python (DataCamp)
Section: Python Lists
Date: 2026-04-11
Student: Md. Ualiur Rahman Rahat

Description:
-----------
The 'del' statement removes elements from a list by index.
After deletion, all subsequent elements shift left (indices change).
Can delete single elements, slices, or entire lists.

Key Concepts:
------------
1. Syntax: del list[index]
2. After deletion, indices of later elements decrease by 1
3. Can delete slices: del list[start:end]
4. Can delete entire list: del list (then list is undefined)

Original Exercise Instructions:
-------------------------------
1. Delete poolhouse items (string and float) from areas list
2. Note: After first deletion, indices shift — second deletion uses same index
3. Print updated list

Learning Note from Student:
--------------------------
Important: When you delete, indices change!
The exercise cleverly uses del areas[10] twice because after first deletion,
the next item shifts into index 10.
C++ vectors: erase() method, similar shifting behavior.
"""

# Areas list with poolhouse and garage added
areas = ["hallway", 11.25, "kitchen", 18.0,
         "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

print("Original list:")
print(areas)
print(f"Length: {len(areas)}")

# Delete the poolhouse items from the list
# Poolhouse string is at index 10, area at index 11
# After first deletion, the area shifts to index 10

# First delete: remove "poolhouse" (string) at index 10
del areas[10]
print("\nAfter deleting 'poolhouse' (index 10):")
print(areas)
print(f"Length: {len(areas)}")

# Second delete: remove 24.5 (now at index 10 after shift)
del areas[10]
print("\nAfter deleting poolhouse area (now at index 10):")
print(areas)
print(f"Length: {len(areas)}")

# Alternative approach (more clear): delete slice
# del areas[10:12] would delete both at once


# ============================================================================
# Additional Practice (self-added):
# ============================================================================

print("\n--- Deletion Patterns ---")

# Example list for deletion practice
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']
print(f"Original fruits: {fruits}")

# Delete single element by index
del fruits[2]  # Removes 'cherry'
print(f"After del fruits[2]: {fruits}")

# Delete slice (multiple elements)
del fruits[1:3]  # Removes indices 1 and 2
print(f"After del fruits[1:3]: {fruits}")

# Delete using negative index
del fruits[-1]  # Removes last element
print(f"After del fruits[-1]: {fruits}")

# Safe deletion: check index exists first
index_to_delete = 5
if index_to_delete < len(fruits):
    del fruits[index_to_delete]
else:
    print(f"Index {index_to_delete} out of range (length={len(fruits)})")

# Delete entire list (uncomment to see)
# del fruits
# print(fruits)  # NameError: name 'fruits' is not defined


# ============================================================================
# Key Takeaways:
# ============================================================================
# 1. 'del' removes elements by index (no return value)
# 2. After deletion, later elements shift left (indices change!)
# 3. Always be careful with chained deletions — indices change
# 4. Use slice deletion to remove multiple items at once: del list[start:end]
# 5. Deleting an entire list with 'del list' removes it from memory
# 6. Common in data cleaning to remove outliers or invalid entries