# -*- coding: utf-8 -*-

"""
Exercise: Line plot (3)
Course: Intermediate Python (DataCamp)
Section: Matplotlib
Date: 2026-04-22
Student: Md. Ualiur Rahman Rahat

Description:
Create a line plot comparing GDP per capita and life expectancy across countries in 2007.

Key Concepts:
- Line plots for exploring relationships between variables
- The importance of choosing appropriate plot types
- Accessing list elements with negative indexing

Original Exercise Instructions:
- Print the last item from both gdp_cap and life_exp lists (Zimbabwe data)
- Build a line chart with gdp_cap on x-axis, life_exp on y-axis
- Display the plot with plt.show()
"""

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Gapminder 2007 data (sample of 10 countries for demonstration)
gdp_cap = [974.58, 5937.03, 6223.37, 13171.40, 33693.18, 42951.65, 127.79, 3413.48, 2042.95, 4720.00]

life_exp = [43.8, 72.4, 76.4, 80.2, 81.6, 82.2, 41.2, 70.0, 64.1, 74.8]

pop = [33.7, 127.5, 88.8, 128.2, 301.1, 62.3, 23.2, 192.2, 109.6, 54.5]  # in millions

col = ['blue', 'green', 'green', 'green', 'green', 'green', 'blue', 'red', 'red', 'green']  # continents mapped to colors
# Print the last item of gdp_cap and life_exp
print(gdp_cap[-1])
print(life_exp[-1])

# Make a line plot, gdp_cap on the x-axis, life_exp on the y-axis
plt.plot(gdp_cap, life_exp)

# Display the plot
plt.show()

# Key Takeaways:
# 1. Line plots connect points sequentially - best for time series data
# 2. For non-sequential data like GDP vs life expectancy, scatter plots are more appropriate
# 3. Always consider whether your plot type matches your data structure
# 4. Negative indexing works on any list regardless of content type