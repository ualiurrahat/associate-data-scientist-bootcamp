# -*- coding: utf-8 -*-

"""
Exercise: Loop over dictionary
Course: Intermediate Python (DataCamp)
Section: Loops
Date: 2026-04-25
Student: Md. Ualiur Rahman Rahat

Description:
Iterate through dictionary key-value pairs using .items() method.

Key Concepts:
- .items() returns (key, value) tuples
- Unpack into two variables in loop header
- f-strings for clean formatting

Original Exercise Instructions:
- Loop through each key:value pair in europe
- Print "the capital of x is y" for each
"""

# Definition of dictionary (countries and their capitals)
europe = {
    'spain': 'madrid',
    'france': 'paris',
    'germany': 'berlin',
    'norway': 'oslo',
    'italy': 'rome',
    'poland': 'warsaw',
    'austria': 'vienna'
}

# Iterate over europe (key = country, value = capital)
for country, capital in europe.items():
    print(f"the capital of {country} is {capital}")

# Key Takeaways:
# 1. .items() is required to loop through dictionary pairs
# 2. Without .items(), loop only iterates over keys
# 3. Unpack key, value in loop header (like enumerate)
# 4. Dictionary order preserved in Python 3.7+
# 5. Much more intuitive than iterating over keys and looking up values