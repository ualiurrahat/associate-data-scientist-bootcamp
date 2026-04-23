# -*- coding: utf-8 -*-

"""
Exercise: Labels
Course: Intermediate Python (DataCamp)
Section: Matplotlib
Date: 2026-04-22
Student: Md. Ualiur Rahman Rahat

Description:
Add axis labels and a title to customize a scatter plot for better interpretability.

Key Concepts:
- Adding descriptive axis labels with xlabel() and ylabel()
- Plot titles with title()
- Professional plot presentation

Original Exercise Instructions:
- Use xlab and ylab strings to set x and y-axis labels
- Use title string to add plot title
- Display plot with plt.show()
"""


# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Gapminder 2007 data (sample of 10 countries for demonstration)
gdp_cap = [974.58, 5937.03, 6223.37, 13171.40, 33693.18, 42951.65, 127.79, 3413.48, 2042.95, 4720.00]
life_exp = [43.8, 72.4, 76.4, 80.2, 81.6, 82.2, 41.2, 70.0, 64.1, 74.8]
pop = [33.7, 127.5, 88.8, 128.2, 301.1, 62.3, 23.2, 192.2, 109.6, 54.5]  # in millions
col = ['blue', 'green', 'green', 'green', 'green', 'green', 'blue', 'red', 'red', 'green']  # continents mapped to colors


# Basic scatter plot, log scale
plt.scatter(gdp_cap, life_exp)
plt.xscale('log')

# Strings
xlab = 'GDP per Capita [in USD]'
ylab = 'Life Expectancy [in years]'
title = 'World Development in 2007'

# Add axis labels
plt.xlabel(xlab)
plt.ylabel(ylab)

# Add title
plt.title(title)

# After customizing, display the plot
plt.show()

# Key Takeaways:
# 1. Labels make plots self-explanatory and publication-ready
# 2. Include units in axis labels (e.g., [in USD], [in years])
# 3. Title should describe what the plot shows
# 4. Labels dramatically improve plot readability for others