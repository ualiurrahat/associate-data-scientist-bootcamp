# -*- coding: utf-8 -*-

"""
Exercise: Cars per capita (1)
Course: Intermediate Python (DataCamp)
Section: Logic, Control Flow and Filtering
Date: 2026-04-25
Student: Md. Ualiur Rahman Rahat

Description:
Filter numeric data using comparison operators on DataFrame columns.

Key Concepts:
- Filter numeric columns with >, <, >=, <=, ==, !=
- Combine comparison with boolean indexing
- Identify rows meeting numeric thresholds

Original Exercise Instructions:
- Select cars_per_cap column as cpc
- Create boolean Series many_cars where cpc > 500
- Use many_cars to subset cars as car_maniac
- Print car_maniac (countries with >500 cars per 1000 people)
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

# One-liner approach (commented steps show breakdown)
# cpc = cars['cars_per_cap']
# many_cars = cpc > 500
# car_maniac = cars[many_cars]
car_maniac = cars[cars['cars_per_cap'] > 500]

# Print car_maniac
print("Countries with >500 cars per 1000 people:")
print(car_maniac)

# Clean up
os.remove('cars.csv')

# Key Takeaways:
# 1. Numeric filtering uses same boolean indexing pattern
# 2. Comparison applies to entire column (vectorized)
# 3. Returns boolean Series of same length
# 4. Can filter on any numeric column
# 5. US, Australia, Japan have very high car ownership
# 6. India (18) has very low car ownership