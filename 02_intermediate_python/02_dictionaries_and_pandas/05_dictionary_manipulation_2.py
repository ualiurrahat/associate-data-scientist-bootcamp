# -*- coding: utf-8 -*-

"""
Exercise: Dictionary Manipulation (2)
Course: Intermediate Python (DataCamp)
Section: Dictionaries & Pandas
Date: 2026-04-25
Student: Md. Ualiur Rahman Rahat

Description:
Update existing dictionary values and remove incorrect key-value pairs.

Key Concepts:
- dictionary[key] = new_value updates existing key
- del dictionary[key] removes key-value pair
- Keys must exist when using del or KeyError occurs

Original Exercise Instructions:
- Update Germany's capital from 'bonn' to 'berlin'
- Remove key 'australia' from europe (it doesn't belong in Europe!)
- Print updated europe
"""

# Definition of dictionary (with errors to fix)
europe = {
    'spain': 'madrid', 
    'france': 'paris', 
    'germany': 'bonn',  # Wrong capital!
    'norway': 'oslo', 
    'italy': 'rome', 
    'poland': 'warsaw',
    'australia': 'vienna'  # Australia isn't in Europe!
}

# Update capital of germany
europe['germany'] = 'berlin'

# Remove australia
del europe['australia']

# Print europe
print(europe)

# Key Takeaways:
# 1. Updating uses same syntax as adding - Python figures out if key exists
# 2. del keyword permanently removes key-value pairs
# 3. Be careful: del doesn't return the value (unlike list .pop())
# 4. Always verify dictionary contents after modifications