# -*- coding: utf-8 -*-

"""
Exercise: Add column (2)
Course: Intermediate Python (DataCamp)
Section: Loops
Date: 2026-04-25
Student: Md. Ualiur Rahman Rahat

Description:
Add column efficiently using apply() method instead of iterrows().

Key Concepts:
- apply() applies function to entire column at once
- Vectorized operations are much faster than loops
- str.upper is a method, pass as argument to apply

Original Exercise Instructions:
- Replace for loop with one-liner using .apply(str.upper)
- Add COUNTRY column with uppercase country names
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

# Use .apply(str.upper) - vectorized approach
cars["COUNTRY"] = cars["country"].apply(str.upper)

print(cars)

# Clean up
os.remove('cars.csv')

# Key Takeaways:
# 1. apply() is 10-100x faster than iterrows() for large datasets
# 2. Pass function name without parentheses: str.upper, not str.upper()
# 3. apply() automatically applies to each element in column
# 4. One line of code instead of loop with multiple lines
# 5. Always prefer vectorized operations when possible
# 6. This is the pandas way: "NO manual loops with iterrows!"