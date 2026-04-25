# -*- coding: utf-8 -*-

"""
Exercise: Create dictionary
Course: Intermediate Python (DataCamp)
Section: Dictionaries & Pandas
Date: 2026-04-25
Student: Md. Ualiur Rahman Rahat

Description:
Convert parallel lists into a dictionary where country names are keys and capitals are values.

Key Concepts:
- Dictionary syntax: {key1: value1, key2: value2}
- Keys must be unique and immutable (strings, numbers, tuples)
- Values can be any data type

Original Exercise Instructions:
- Create dictionary europe with 4 key:value pairs from countries and capitals
- Use lowercase characters everywhere
- Print europe
"""

# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# From string in countries and capitals, create dictionary europe
europe = {
    'spain': 'madrid', 
    'france': 'paris', 
    'germany': 'berlin', 
    'norway': 'oslo'
}

# Print europe
print(europe)

# Key Takeaways:
# 1. Dictionaries map keys to values directly - no index searching needed
# 2. Order doesn't matter in dictionaries (Python 3.7+ preserves insertion order)
# 3. Dictionary syntax uses curly braces {} not square brackets []
# 4. Much more intuitive than parallel lists for paired data