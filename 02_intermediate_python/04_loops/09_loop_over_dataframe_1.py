# -*- coding: utf-8 -*-

"""
Exercise: Loop over DataFrame (1)
Course: Intermediate Python (DataCamp)
Section: Loops
Date: 2026-04-25
Student: Md. Ualiur Rahman Rahat

Description:
Iterate over DataFrame rows using iterrows() method.

Key Concepts:
- iterrows() returns (index, row) tuples
- row is a Series containing column values
- Useful for row-by-row operations

Original Exercise Instructions:
- Write for loop over cars using iterrows()
- Print row label (index) and row contents
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

# Iterate over rows of cars
print("Iterating over DataFrame rows:")
for label, row in cars.iterrows():
    print(f"\nLabel: {label}")
    print(f"Row data:\n{row}")

# Clean up
os.remove('cars.csv')

# Key Takeaways:
# 1. iterrows() returns (index, Series) for each row
# 2. row is a Series with column names as index
# 3. Each iteration creates a new Series (memory intensive)
# 4. Good for understanding, but vectorized operations are faster
# 5. Avoid iterrows() for large datasets (use apply instead)