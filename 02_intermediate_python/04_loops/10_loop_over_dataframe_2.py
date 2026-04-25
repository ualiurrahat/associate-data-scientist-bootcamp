# -*- coding: utf-8 -*-

"""
Exercise: Loop over DataFrame (2)
Course: Intermediate Python (DataCamp)
Section: Loops
Date: 2026-04-25
Student: Md. Ualiur Rahman Rahat

Description:
Access specific columns from each row while iterating with iterrows().

Key Concepts:
- row['column_name'] accesses row data by column
- Format output with specific column values
- Convert numbers to strings if needed

Original Exercise Instructions:
- Print "country: cars_per_cap" for each row
- Format: "US: 809", "AUS: 731", etc.
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

# Adapt for loop to print specific columns
print("Cars per capita by country:")
for label, row in cars.iterrows():
    print(f"{label}: {row['cars_per_cap']}")

# Clean up
os.remove('cars.csv')

# Key Takeaways:
# 1. Use row['column_name'] to access specific values
# 2. Row label (index) comes from first loop variable
# 3. f-strings automatically convert numbers to strings
# 4. Each iteration gives one country's data
# 5. Good for row-specific operations or conditional logic