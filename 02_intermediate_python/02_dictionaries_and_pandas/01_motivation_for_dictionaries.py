# -*- coding: utf-8 -*-

"""
Exercise: Motivation for dictionaries
Course: Intermediate Python (DataCamp)
Section: Dictionaries & Pandas
Date: 2026-04-25
Student: Md. Ualiur Rahman Rahat

Description:
Learn why dictionaries are useful by comparing the list-based approach vs dictionary approach.
Lists require maintaining two separate lists and finding indexes to relate data.

Key Concepts:
- list.index() method finds position of an element
- Parallel lists store related data at same indices
- Dictionaries provide direct key->value mapping without index lookup

Original Exercise Instructions:
- Use index() method on countries to find index of 'germany'
- Store this index as ind_ger
- Use ind_ger to access capital of Germany from capitals list
"""

# Definition of countries and capital (parallel lists)
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# Get index of 'germany': ind_ger
ind_ger = countries.index('germany')

# Use ind_ger to print out capital of Germany
print(capitals[ind_ger])

# Key Takeaways:
# 1. Lists store data sequentially but require index tracking
# 2. .index() method searches entire list (O(n) operation)
# 3. If lists get out of sync, data becomes corrupted
# 4. Dictionaries solve this by pairing keys with values directly