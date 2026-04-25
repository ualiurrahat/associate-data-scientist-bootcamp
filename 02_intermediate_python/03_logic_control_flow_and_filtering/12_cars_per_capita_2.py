# -*- coding: utf-8 -*-

"""
Exercise: Cars per capita (2)
Course: Intermediate Python (DataCamp)
Section: Logic, Control Flow and Filtering
Date: 2026-04-25
Student: Md. Ualiur Rahman Rahat

Description:
Use np.logical_and() for range filtering with multiple conditions.

Key Concepts:
- np.logical_and() for element-wise AND on arrays/Series
- Range filtering: lower_bound < column < upper_bound
- Combine multiple numeric conditions

Original Exercise Instructions:
- Create DataFrame medium with cars_per_cap between 100 and 500
- Use np.logical_and() to combine conditions
- Print medium
"""

import pandas as pd
import numpy as np
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

# One-liner with np.logical_and
medium = cars[np.logical_and(cars['cars_per_cap'] > 100, 
                              cars['cars_per_cap'] < 500)]

# Alternative breakdown:
# cpc = cars['cars_per_cap']
# between = np.logical_and(cpc > 100, cpc < 500)
# medium = cars[between]

print("Countries with cars_per_cap between 100 and 500:")
print(medium)

# Clean up
os.remove('cars.csv')

# Key Takeaways:
# 1. np.logical_and() combines two boolean Series element-wise
# 2. For range filtering, use: lower < col < upper
# 3. Cannot use Python 'and' with Series (would error)
# 4. Can chain multiple conditions with nested logical_and
# 5. Russia (200) fits the 100-500 range
# 6. India (18), Morocco(70), Egypt(45) are below 100
# 7. US(809), Australia(731), Japan(588) are above 500