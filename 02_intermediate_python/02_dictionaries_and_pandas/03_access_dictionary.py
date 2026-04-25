# -*- coding: utf-8 -*-

"""
Exercise: Access dictionary
Course: Intermediate Python (DataCamp)
Section: Dictionaries & Pandas
Date: 2026-04-25
Student: Md. Ualiur Rahman Rahat

Description:
Access dictionary values using keys and examine all keys in the dictionary.

Key Concepts:
- dictionary.keys() returns all keys as a view object
- dictionary[key] accesses value for specific key
- Keys must exist or KeyError occurs

Original Exercise Instructions:
- Call keys() method on europe and print result
- Print value belonging to key 'norway'
"""

# Definition of dictionary
europe = {
    'spain': 'madrid', 
    'france': 'paris', 
    'germany': 'berlin', 
    'norway': 'oslo'
}

# Print out the keys in europe
print(europe.keys())

# Print out value that belongs to key 'norway'
print(europe['norway'])

# Key Takeaways:
# 1. .keys() returns dict_keys object (iterable like a list)
# 2. Dictionary access is O(1) - instant regardless of size
# 3. Much faster than list.index() which searches sequentially
# 4. Keys act like labels, values are the actual data