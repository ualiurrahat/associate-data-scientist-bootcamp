# -*- coding: utf-8 -*-

"""
Exercise: Square Brackets (2)
Course: Intermediate Python (DataCamp)
Section: Dictionaries & Pandas
Date: 2026-04-25
Student: Md. Ualiur Rahman Rahat

Description:
Select DataFrame rows using square brackets with slicing syntax, similar to list slicing.

Key Concepts:
- df[start:stop] selects rows by position (like list slicing)
- Stop index is exclusive (doesn't include that row)
- Returns DataFrame with selected rows only
- Cannot select single row with bracket alone (need loc/iloc)

Original Exercise Instructions:
- Select first 3 observations using df[0:3]
- Select rows 3, 4, 5 (index positions 3,4,5) using df[3:6]
"""

import pandas as pd
import os

# Create cars.csv file
data = {
    'country': ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt'],
    'drives_right': [True, False, False, False, True, True, True],
    'cars_per_cap': [809, 731, 588, 18, 200, 70, 45]
}
df = pd.DataFrame(data, index=['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG'])
df.to_csv('cars.csv')

# Import cars data
cars = pd.read_csv('cars.csv', index_col=0)

# Print out first 3 observations (rows 0,1,2)
print("First 3 observations:")
print(cars[0:3])
print("\n")

# Print out fourth, fifth and sixth observation (rows 3,4,5)
print("Fourth, fifth, and sixth observations:")
print(cars[3:6])

# Clean up
os.remove('cars.csv')

# Key Takeaways:
# 1. Bracket slicing works on rows, not columns (unlike lists)
# 2. Syntax: df[start:stop] where stop is exclusive
# 3. Returns DataFrame with sliced rows, all columns
# 4. Cannot select single row with df[3] (unlike lists)
# 5. Row slicing by position, not by label
# 6. Useful for getting first N rows or a range of rows