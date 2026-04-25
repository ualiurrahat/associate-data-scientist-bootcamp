# -*- coding: utf-8 -*-

"""
Exercise: loc and iloc (2)
Course: Intermediate Python (DataCamp)
Section: Dictionaries & Pandas
Date: 2026-04-25
Student: Md. Ualiur Rahman Rahat

Description:
Select specific rows AND columns simultaneously using .loc and .iloc with comma separation.

Key Concepts:
- Syntax: df.loc[rows, columns] or df.iloc[rows, columns]
- rows and columns can be single label, list, or slice
- First selector specifies rows, second specifies columns

Original Exercise Instructions:
- Print drives_right value for Morocco (label 'MOR')
- Print sub-DataFrame for Russia and Morocco with columns 'country' and 'drives_right'
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

# Print out drives_right value of Morocco (single value)
print("Drives_right value for Morocco:")
print(cars.loc['MOR', 'drives_right'])
print(f"\nType: {type(cars.loc['MOR', 'drives_right'])}\n")

# Alternative using .iloc (Morocco is row 5, drives_right is column 1)
print("Same value using .iloc:")
print(cars.iloc[5, 1])
print("\n")

# Print sub-DataFrame for Russia and Morocco with specific columns
print("Sub-DataFrame for Russia and Morocco:")
print(cars.loc[['RU', 'MOR'], ['country', 'drives_right']])

# Clean up
os.remove('cars.csv')

# Key Takeaways:
# 1. .loc['row', 'col'] returns single scalar value
# 2. .loc[['row1','row2'], ['col1','col2']] returns DataFrame
# 3. Row and column selectors separated by comma
# 4. Order matters: rows FIRST, columns SECOND
# 5. This is the most powerful way to select data in pandas