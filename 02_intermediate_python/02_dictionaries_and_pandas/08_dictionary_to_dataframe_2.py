# -*- coding: utf-8 -*-

"""
Exercise: Dictionary to DataFrame (2)
Course: Intermediate Python (DataCamp)
Section: Dictionaries & Pandas
Date: 2026-04-25
Student: Md. Ualiur Rahman Rahat

Description:
Customize DataFrame row labels using the index attribute instead of default numeric indices.

Key Concepts:
- Default row labels are 0, 1, 2, ... (zero-indexed integers)
- DataFrame.index property sets/gets row labels
- Custom labels make data more readable and accessible

Original Exercise Instructions:
- Observe default row labels (0-6)
- Set cars.index equal to row_labels list
- Print cars again to see custom labels
"""

import pandas as pd

# Build cars DataFrame from dictionary (recreating from previous exercise)
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr = [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
cars_dict = {'country': names, 'drives_right': dr, 'cars_per_cap': cpc}
cars = pd.DataFrame(cars_dict)
print("Default numeric row labels:")
print(cars)

# Definition of row_labels (ISO country codes)
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

print("\nAfter setting custom row labels:")
print(cars)

# Key Takeaways:
# 1. Default numeric indices work but aren't descriptive
# 2. Custom labels make data easier to reference (e.g., cars.loc['US'])
# 3. Index can be any hashable type (strings, numbers, tuples)
# 4. Good practice: use meaningful identifiers as row labels
# 5. Similar to setting row names in Excel or R