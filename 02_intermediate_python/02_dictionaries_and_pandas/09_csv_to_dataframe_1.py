# -*- coding: utf-8 -*-

"""
Exercise: CSV to DataFrame (1)
Course: Intermediate Python (DataCamp)
Section: Dictionaries & Pandas
Date: 2026-04-25
Student: Md. Ualiur Rahman Rahat

Description:
Import data directly from a CSV file into a pandas DataFrame without manual list creation.

Key Concepts:
- pd.read_csv() reads comma-separated values files
- CSV is standard format for tabular data export
- Much more efficient than typing data manually

Original Exercise Instructions:
- Import pandas as pd
- Use pd.read_csv() to import 'cars.csv'
- Store as cars DataFrame and print

Note:
Since we don't have the actual 'cars.csv' file, we'll create a small CSV from data
and then read it back to demonstrate the functionality.
"""

import pandas as pd
import os

# Create sample cars.csv file from our data (for demonstration)
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr = [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Create DataFrame first
temp_cars = pd.DataFrame({
    'country': names,
    'drives_right': dr,
    'cars_per_cap': cpc
})

# Save to CSV (this simulates having the file)
temp_cars.to_csv('cars.csv')
print("Created cars.csv file from data\n")

# Now the actual exercise: Import from CSV
# Import pandas as pd (already imported above)
# Import the cars.csv data: cars
cars = pd.read_csv('cars.csv')

# Print out cars
print("Imported from CSV:")
print(cars)

# Clean up: remove the temporary file
os.remove('cars.csv')
print("\n(Note: cars.csv was created temporarily for this demo and then deleted)")

# Key Takeaways:
# 1. read_csv() is the most common pandas import function
# 2. CSV files are universal - work with Excel, databases, etc.
# 3. No need to manually type data - read from files instead
# 4. Real-world data almost always comes from files, not typed in code