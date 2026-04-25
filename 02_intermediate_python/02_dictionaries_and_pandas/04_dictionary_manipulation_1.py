# -*- coding: utf-8 -*-

"""
Exercise: Dictionary Manipulation (1)
Course: Intermediate Python (DataCamp)
Section: Dictionaries & Pandas
Date: 2026-04-25
Student: Md. Ualiur Rahman Rahat

Description:
Add new key-value pairs to an existing dictionary and check for key existence.

Key Concepts:
- dictionary[new_key] = value adds new entry
- 'key' in dictionary checks if key exists (returns boolean)
- Dictionaries are mutable (can be changed after creation)

Original Exercise Instructions:
- Add key 'italy' with value 'rome' to europe
- Print 'italy' in europe to verify it exists
- Add key 'poland' with value 'warsaw'
- Print entire europe dictionary
"""

# Definition of dictionary
europe = {
    'spain': 'madrid', 
    'france': 'paris', 
    'germany': 'berlin', 
    'norway': 'oslo'
}

# Add italy to europe
europe['italy'] = 'rome'

# Print out italy in europe (checks if key exists)
print('italy' in europe)

# Add poland to europe
europe['poland'] = 'warsaw'

# Print europe
print(europe)

# Key Takeaways:
# 1. Adding new key-value pairs uses same syntax as accessing
# 2. 'in' keyword checks key existence without throwing errors
# 3. No need to pre-allocate dictionary size - grows dynamically
# 4. Unlike lists, dictionaries don't have .append() - just assign to new key