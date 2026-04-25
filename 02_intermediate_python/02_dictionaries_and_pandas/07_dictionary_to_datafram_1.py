# -*- coding: utf-8 -*-

"""
Exercise: Dictionary to DataFrame (1)
Course: Intermediate Python (DataCamp)
Section: Dictionaries & Pandas
Date: 2026-04-25
Student: Md. Ualiur Rahman Rahat

Description:
Convert a dictionary of lists into a pandas DataFrame - the foundation of data analysis in Python.

Key Concepts:
- pandas DataFrame = 2D tabular data structure (rows and columns)
- Dictionary keys become column names
- Dictionary values (lists) become column data
- pd.DataFrame() constructor converts dict to DataFrame

Original Exercise Instructions:
- Import pandas as pd
- Create my_dict with keys: 'country', 'drives_right', 'cars_per_cap'
- Use pd.DataFrame() to convert dict to cars DataFrame
- Print cars

Note:
Data represents vehicle statistics by country (2000s era data)
"""

# Pre-defined lists (same data, different structure)
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr = [True, False, False, False, True, True, True]  # True = drives on right side
cpc = [809, 731, 588, 18, 200, 70, 45]  # Cars per 1000 people

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs
my_dict = {
    'country': names,
    'drives_right': dr,
    'cars_per_cap': cpc
}

# Build a DataFrame cars from my_dict
cars = pd.DataFrame(my_dict)

# Print cars
print(cars)

# Key Takeaways:
# 1. pandas is THE library for data analysis in Python
# 2. DataFrame = spreadsheet-like structure with labeled rows/columns
# 3. Dictionary keys become column headers automatically
# 4. Lists must be same length (or error occurs)
# 5. This is much cleaner than managing multiple parallel lists