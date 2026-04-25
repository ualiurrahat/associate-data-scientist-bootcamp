# -*- coding: utf-8 -*-

"""
Exercise: Driving right (1)
Course: Intermediate Python (DataCamp)
Section: Logic, Control Flow and Filtering
Date: 2026-04-25
Student: Md. Ualiur Rahman Rahat

Description:
Filter DataFrame rows using a boolean Series created from a column.

Key Concepts:
- Boolean indexing: df[boolean_series] returns rows where True
- Extract column as Series for filtering
- Essential pattern for data filtering

Original Exercise Instructions:
- Extract drives_right column as Series dr
- Use dr to subset cars DataFrame as sel
- Print sel (should show only right-driving countries)
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

# Extract drives_right column as Series: dr
dr = cars['drives_right']

# Alternative ways using loc and iloc
# dr = cars.loc[:, 'drives_right']
# dr = cars.iloc[:, 1]

# Use dr to subset cars: sel
sel = cars[dr]

# Print sel
print(sel)

# Clean up
os.remove('cars.csv')

# Key Takeaways:
# 1. Boolean Series with same index as DataFrame filters rows
# 2. Rows where Series is True are kept, False are dropped
# 3. This is called boolean indexing or boolean masking
# 4. The Series index must align with DataFrame index
# 5. Very powerful for data subsetting