# -*- coding: utf-8 -*-

"""
Exercise: CSV to DataFrame (2)
Course: Intermediate Python (DataCamp)
Section: Dictionaries & Pandas
Date: 2026-04-25
Student: Md. Ualiur Rahman Rahat

Description:
Fix CSV import by specifying which column should be used as row labels using index_col parameter.

Key Concepts:
- index_col parameter tells pandas which column becomes row labels
- Default behavior (index_col=None) adds extra unnamed column
- Setting index_col=0 uses first column as row labels

Original Exercise Instructions:
- Notice first column becomes extra data column
- Add index_col=0 to read_csv() to fix
- First column now becomes row labels instead of data
"""

import pandas as pd
import os

# Create sample cars.csv file with an index column (first column will be country codes)
data = {
    'Unnamed: 0': ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG'],
    'country': ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt'],
    'drives_right': [True, False, False, False, True, True, True],
    'cars_per_cap': [809, 731, 588, 18, 200, 70, 45]
}
df = pd.DataFrame(data)
df.to_csv('cars.csv', index=False)
print("Created cars.csv with first column as row labels\n")

# Wrong import (without index_col) - creates extra column
cars_wrong = pd.read_csv('cars.csv')
print("WRONG: Without index_col parameter")
print(cars_wrong)
print("\nNotice the extra 'Unnamed: 0' column? That's our row labels becoming data!\n")

# Fix import by including index_col
cars_correct = pd.read_csv('cars.csv', index_col=0)
print("CORRECT: With index_col=0")
print(cars_correct)

# Clean up
os.remove('cars.csv')
print("\n(Note: cars.csv was created temporarily and then deleted)")

# Key Takeaways:
# 1. index_col=0 tells pandas "use first column as row names"
# 2. Without it, CSV's first column becomes regular data column
# 3. CSV files often have row identifiers in first column
# 4. Always check if your DataFrame has unexpected index column
# 5. Saves you from manually setting .index later