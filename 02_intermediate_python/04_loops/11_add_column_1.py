# -*- coding: utf-8 -*-

"""
Exercise: Add column (1)
Course: Intermediate Python (DataCamp)
Section: Loops
Date: 2026-04-25
Student: Md. Ualiur Rahman Rahat

Description:
Add a new column to DataFrame by iterating through rows with iterrows().

Key Concepts:
- Add column using df.loc[label, new_column] = value
- Apply transformations row by row
- string.upper() method converts to uppercase

Original Exercise Instructions:
- Add new column COUNTRY with uppercase country names
- Use row['country'].upper() to get uppercase version
- Print resulting DataFrame
"""

import pandas as pd
import os

# Create cars data
data = {
    'country': ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt'],
    'drives_right': [True, False, False, False, True, True, True],
    'cars_per_cap': [809, 731, 588, 18, 200, 70, 45]
}
df = pd.DataFrame(data, index=['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG'])
df.to_csv('cars.csv')

# Import cars data
cars = pd.read_csv('cars.csv', index_col=0)

# Code for loop that adds COUNTRY column
for label, row in cars.iterrows():
    cars.loc[label, "COUNTRY"] = row["country"].upper()

# Print cars (with new column)
print(cars)

# Clean up
os.remove('cars.csv')

# Key Takeaways:
# 1. loc[label, new_column] = value adds new column one row at a time
# 2. .upper() method converts string to uppercase
# 3. This works but is SLOW for large datasets
# 4. Data type of new column is inferred automatically
# 5. New column added to DataFrame permanently