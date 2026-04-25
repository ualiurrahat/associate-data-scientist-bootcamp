# -*- coding: utf-8 -*-

"""
Exercise: loc and iloc (1)
Course: Intermediate Python (DataCamp)
Section: Dictionaries & Pandas
Date: 2026-04-25
Student: Md. Ualiur Rahman Rahat

Description:
Use .loc (label-based) and .iloc (integer position-based) to select specific rows from DataFrame.

Key Concepts:
- .loc[] uses row/column LABELS (e.g., 'JPN', 'country')
- .iloc[] uses integer POSITIONS (e.g., 2, 0)
- Single label returns Series, list of labels returns DataFrame

Original Exercise Instructions:
- Use loc or iloc to select Japan observation as Series
- Use loc or iloc to select Australia and Egypt as DataFrame
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

# Print out observation for Japan as Series
print("Japan observation (using .loc):")
print(cars.loc['JPN'])
print(f"\nType: {type(cars.loc['JPN'])}\n")

# Alternative using .iloc (Japan is at position 2)
print("Japan observation (using .iloc):")
print(cars.iloc[2])
print("\n")

# Print out observations for Australia and Egypt as DataFrame
print("Australia and Egypt (using .loc):")
print(cars.loc[['AUS', 'EG']])
print(f"\nType: {type(cars.loc[['AUS', 'EG']])}\n")

# Alternative using .iloc (Australia=1, Egypt=6)
print("Australia and Egypt (using .iloc):")
print(cars.iloc[[1, 6]])

# Clean up
os.remove('cars.csv')

# Key Takeaways:
# 1. .loc uses labels ('JPN'), .iloc uses positions (2)
# 2. Single label -> Series, list of labels -> DataFrame
# 3. .loc includes the stop index, .iloc excludes it (like slicing)
# 4. .iloc is faster but less readable
# 5. .loc is preferred for clarity unless doing positional operations