# -*- coding: utf-8 -*-

"""
Exercise: loc and iloc (3)
Course: Intermediate Python (DataCamp)
Section: Dictionaries & Pandas
Date: 2026-04-25
Student: Md. Ualiur Rahman Rahat

Description:
Select only columns (all rows) using .loc and .iloc with slice notation (:) for rows.

Key Concepts:
- df.loc[:, 'column'] selects all rows, one column -> Series
- df.loc[:, ['col1','col2']] selects all rows, multiple columns -> DataFrame
- Colon (:) means "select all" in that dimension
- Works for both .loc (labels) and .iloc (positions)

Original Exercise Instructions:
- Print drives_right column as Series using loc or iloc
- Print drives_right column as DataFrame using loc or iloc
- Print cars_per_cap and drives_right columns as DataFrame using loc or iloc
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

# Print out drives_right column as Series
print("Drives_right column as Series (.loc):")
print(cars.loc[:, 'drives_right'])
print(f"\nType: {type(cars.loc[:, 'drives_right'])}\n")

# Alternative using .iloc (drives_right is column position 1)
print("Same column using .iloc:")
print(cars.iloc[:, 1])
print("\n")

# Print out drives_right column as DataFrame (double brackets)
print("Drives_right column as DataFrame:")
print(cars.loc[:, ['drives_right']])
print(f"\nType: {type(cars.loc[:, ['drives_right']])}\n")

# Print out cars_per_cap and drives_right as DataFrame
print("Multiple columns as DataFrame:")
print(cars.loc[:, ['cars_per_cap', 'drives_right']])

# Clean up
os.remove('cars.csv')

# Key Takeaways:
# 1. Colon (:) selects ALL rows (like list slicing with no boundaries)
# 2. Single column with single brackets -> Series
# 3. Single column with double brackets -> DataFrame
# 4. Multiple columns always return DataFrame
# 5. .loc[:, 'col'] vs .loc[:, ['col']] - small syntax, big type difference
# 6. This pattern is extremely common: "give me all rows of specific columns"