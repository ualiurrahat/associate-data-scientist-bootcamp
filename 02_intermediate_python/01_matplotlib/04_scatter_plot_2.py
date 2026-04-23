# -*- coding: utf-8 -*-

"""
Exercise: Scatter plot (2)
Course: Intermediate Python (DataCamp)
Section: Matplotlib
Date: 2026-04-22
Student: Md. Ualiur Rahman Rahat

Description:
Create a scatter plot to explore the relationship between population and life expectancy.

Key Concepts:
- Building scatter plots from scratch
- Exploring correlations between different variable pairs
- Understanding population data in millions

Original Exercise Instructions:
- Import matplotlib.pyplot as plt
- Build a scatter plot with pop on x-axis, life_exp on y-axis
- Display the plot with plt.show()
"""

# Import package
import matplotlib.pyplot as plt

# Gapminder 2007 data (sample of 10 countries for demonstration)
gdp_cap = [974.58, 5937.03, 6223.37, 13171.40, 33693.18, 42951.65, 127.79, 3413.48, 2042.95, 4720.00]
life_exp = [43.8, 72.4, 76.4, 80.2, 81.6, 82.2, 41.2, 70.0, 64.1, 74.8]
pop = [33.7, 127.5, 88.8, 128.2, 301.1, 62.3, 23.2, 192.2, 109.6, 54.5]  # in millions
col = ['blue', 'green', 'green', 'green', 'green', 'green', 'blue', 'red', 'red', 'green']  # continents mapped to colors

# Build Scatter plot
plt.scatter(pop, life_exp)

# Show plot
plt.show()

# Key Takeaways:
# 1. Population and life expectancy show less correlation than GDP and life expectancy
# 2. Some densely populated countries still have high life expectancy
# 3. Scatter plots immediately reveal if relationship exists between variables
# 4. Starting from scratch reinforces understanding of each component