# -*- coding: utf-8 -*-

"""
Exercise: String Methods
Course: Introduction to Python (DataCamp)
Section: Functions and Packages
Date: 2026-04-14
Student: Md. Ualiur Rahman Rahat

Description:
-----------
Methods are functions that belong to a specific object type.
String methods are called using dot notation: string.method_name()
Unlike functions, methods are attached to the object they operate on.

Key Concepts:
------------
1. .upper() - returns string in all uppercase (does NOT modify original)
2. .count() - counts occurrences of a substring
3. Strings are IMMUTABLE - methods return new strings, don't change original
4. Dot notation: object.method(argument)

Original Exercise Instructions:
-------------------------------
1. Use .upper() on 'place' and store in place_up
2. Print both place and place_up to see original unchanged
3. Use .count('o') to count letter 'o' occurrences

Learning Note from Student:
--------------------------
Important: .upper() doesn't change 'place' - it creates a new string!
This is different from some list methods that modify in-place.
"""

# string to experiment with: place
place = "poolhouse"

# Use upper() on place (returns new string, original unchanged)
place_up = place.upper()

# Print out place and place_up
print(f"Original (unchanged): {place}")
print(f"Uppercase version: {place_up}")

# Print out the number of o's in place
# .count() searches for substring 'o' in the string
o_count = place.count('o')
print(f"Number of 'o' characters: {o_count}")


# ============================================================================
# Additional Practice (self-added):
# ============================================================================

print("\n--- More String Methods ---")

text = "  Hello, Python World!  "

# .lower() - convert to lowercase
print(f".lower(): '{text.lower()}'")

# .strip() - remove whitespace from both ends
print(f".strip(): '{text.strip()}'")

# .replace() - replace substring
print(f".replace('Python', 'Data Science'): '{text.replace('Python', 'Data Science')}'")

# .split() - split into list
words = text.strip().split()
print(f".split(): {words}")

# .join() - join list into string
joined = "-".join(words)
print(f".join(): '{joined}'")

# .startswith() and .endswith() - check beginning/ending
print(f"Starts with '  Hello': {text.startswith('  Hello')}")
print(f"Ends with 'World!  ': {text.endswith('World!  ')}")

# .find() - find index of substring
print(f"Find 'Python' at index: {text.find('Python')}")

# Chaining string methods
clean_text = text.strip().lower().replace("world", "universe")
print(f"Chained methods: '{clean_text}'")


# ============================================================================
# Key Takeaways:
# ============================================================================
# 1. Strings are immutable - methods return NEW strings
# 2. Dot notation: string.method() not method(string)
# 3. .upper() and .lower() change case
# 4. .count() counts occurrences of a substring
# 5. .strip() removes leading/trailing whitespace (very common in data cleaning)
# 6. .split() and .join() are essential for text processing
# 7. Method chaining: text.strip().lower() executes left to right