# -*- coding: utf-8 -*-

"""
Exercise: Build a histogram (3): compare
Course: Intermediate Python (DataCamp)
Section: Matplotlib
Date: 2026-04-22
Student: Md. Ualiur Rahman Rahat

Description:
Compare life expectancy distributions between 1950 and 2007 using histograms.

Key Concepts:
- Comparing distributions across different time periods
- Consistent bin counts for valid comparisons
- Identifying shifts in data distributions over time

Original Exercise Instructions:
- Build histogram of life_exp with 15 bins
- Build histogram of life_exp1950 with 15 bins
- Compare the two distributions
"""

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Life expectancy 2007 data
life_exp = [43.8, 72.4, 76.4, 80.2, 81.6, 82.2, 41.2, 70.0, 64.1, 74.8, 62.1, 79.5, 81.5, 78.5, 80.8, 46.2, 68.9, 75.3, 73.1, 71.9]

# Life expectancy 1950 data (showing lower values for comparison)
life_exp1950 = [36.5, 68.9, 65.3, 68.4, 71.2, 68.8, 37.2, 62.1, 51.2, 69.1, 52.3, 70.2, 68.5, 68.8, 69.6, 40.1, 61.4, 66.2, 60.1, 58.9]

# Histogram of life_exp, 15 bins
plt.hist(life_exp, bins=15)

# Show and clear plot
plt.show()
plt.clf()

# Histogram of life_exp1950, 15 bins
plt.hist(life_exp1950, bins=15)

# Show and clear plot again
plt.show()
plt.clf()

# Key Takeaways:
# 1. Same bin count (15) ensures fair comparison between datasets
# 2. Life expectancy distribution shifted right (higher) from 1950 to 2007
# 3. Variance/spread may differ between time periods
# 4. Histograms effectively show how distributions evolve over time