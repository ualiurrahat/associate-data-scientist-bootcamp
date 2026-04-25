# -*- coding: utf-8 -*-

"""
Exercise: Driving right (2)
Course: Intermediate Python (DataCamp)
Section: Logic, Control Flow and Filtering
Date: 2026-04-25
Student: Md. Ualiur Rahman Rahat

Description:
Use inline boolean filtering without storing intermediate variables.

Key Concepts:
- One-liner filtering: df[df['column'] == value]
- No intermediate variables needed
- Cleaner, more concise code

Original Exercise Instructions:
- Convert previous code to one-liner
- Filter cars directly without separate dr variable
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

# Convert code to a one-liner
sel = cars[cars['drives_right']]

# Print sel
print(sel)

# Clean up
os.remove('cars.csv')

# Key Takeaways:
# 1. Inline filtering eliminates temporary variable dr
# 2. More readable once you understand the pattern
# 3. Same performance as two-step approach
# 4. Pattern: df[df['column'] == condition]
# 5. Can also use >, <, !=, etc. for numeric columns