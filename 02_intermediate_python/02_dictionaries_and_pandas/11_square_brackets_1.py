# -*- coding: utf-8 -*-

"""
Exercise: Square Brackets (1)
Course: Intermediate Python (DataCamp)
Section: Dictionaries & Pandas
Date: 2026-04-25
Student: Md. Ualiur Rahman Rahat

Description:
Select DataFrame columns using square brackets, understanding the difference between Series and DataFrame returns.

Key Concepts:
- Single bracket df['col'] returns Series (1D labeled array)
- Double bracket df[['col']] returns DataFrame (2D with one column)
- Multiple columns: df[['col1', 'col2']] returns DataFrame

Original Exercise Instructions:
- Use single brackets to print country column as Series
- Use double brackets to print country column as DataFrame
- Use double brackets to print country and drives_right columns as DataFrame
"""

import pandas as pd
import os

# Create cars.csv file with correct indexing
data = {
    'country': ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt'],
    'drives_right': [True, False, False, False, True, True, True],
    'cars_per_cap': [809, 731, 588, 18, 200, 70, 45]
}
df = pd.DataFrame(data, index=['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG'])
df.to_csv('cars.csv')

# Import cars data
cars = pd.read_csv('cars.csv', index_col=0)

# Print out country column as Pandas Series (1D)
print("Series (single brackets):")
print(cars['country'])
print(f"\nType: {type(cars['country'])}\n")

# Print out country column as Pandas DataFrame (2D)
print("DataFrame (double brackets):")
print(cars[['country']])
print(f"\nType: {type(cars[['country']])}\n")

# Print out DataFrame with country and drives_right columns
print("Multiple columns as DataFrame:")
print(cars[['country', 'drives_right']])

# Clean up
os.remove('cars.csv')

# Key Takeaways:
# 1. Single bracket = Series (good for calculations/plotting)
# 2. Double bracket = DataFrame (good for consistency)
# 3. Multiple columns MUST use double brackets
# 4. Type matters: Series has no .columns attribute, DataFrame does
# 5. Many pandas methods return different results based on input type