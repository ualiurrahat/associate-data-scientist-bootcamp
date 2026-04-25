# -*- coding: utf-8 -*-

"""
Exercise: Dictionariception (Nested Dictionaries)
Course: Intermediate Python (DataCamp)
Section: Dictionaries & Pandas
Date: 2026-04-25
Student: Md. Ualiur Rahman Rahat

Description:
Work with nested dictionaries where values are themselves dictionaries containing multiple attributes.

Key Concepts:
- Nested dictionaries: dictionary values can be other dictionaries
- Chained square brackets: dict[key1][key2] accesses nested values
- Building complex data structures

Original Exercise Instructions:
- Print capital of France using chained square brackets
- Create 'data' dictionary with 'capital' and 'population' for Italy
- Add Italy to europe dictionary with data as the value
"""

# Dictionary of dictionaries (nested structure)
europe = {
    'spain': {'capital': 'madrid', 'population': 46.77},
    'france': {'capital': 'paris', 'population': 66.03},
    'germany': {'capital': 'berlin', 'population': 80.62},
    'norway': {'capital': 'oslo', 'population': 5.084}
}

# Print out the capital of France (chained square brackets)
print(europe['france']['capital'])

# Create sub-dictionary data
data = {'capital': 'rome', 'population': 59.83}

# Add data to europe under key 'italy'
europe['italy'] = data

# Print europe
print(europe)

# Key Takeaways:
# 1. Nested dictionaries represent hierarchical/relational data
# 2. Each country has multiple attributes (capital, population)
# 3. Chained indexing: first get country, then get attribute
# 4. This structure is similar to JSON (common in APIs)
# 5. Leads naturally to pandas DataFrames (tabular structure)