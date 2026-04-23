# -*- coding: utf-8 -*-

"""
Exercise: Scatter plot (1)
Course: Intermediate Python (DataCamp)
Section: Matplotlib
Date: 2026-04-22
Student: Md. Ualiur Rahman Rahat

Description:
Convert a line plot to a scatter plot and apply logarithmic scaling to better visualize GDP data.

Key Concepts:
- Scatter plots for correlation analysis
- Logarithmic scaling for data with wide value ranges
- plt.scatter() vs plt.plot() usage

Original Exercise Instructions:
- Change the line plot to a scatter plot
- Add plt.xscale('log') to put GDP per capita on logarithmic scale
- Display the plot with plt.show()
"""
# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Gapminder 2007 data (sample of 10 countries for demonstration)
gdp_cap = [974.58, 5937.03, 6223.37, 13171.40, 33693.18, 42951.65, 127.79, 3413.48, 2042.95, 4720.00]
life_exp = [43.8, 72.4, 76.4, 80.2, 81.6, 82.2, 41.2, 70.0, 64.1, 74.8]
pop = [33.7, 127.5, 88.8, 128.2, 301.1, 62.3, 23.2, 192.2, 109.6, 54.5]  # in millions
col = ['blue', 'green', 'green', 'green', 'green', 'green', 'blue', 'red', 'red', 'green']  # continents mapped to colors


# Change the line plot below to a scatter plot
plt.scatter(gdp_cap, life_exp)

# Put the x-axis on a logarithmic scale
plt.xscale('log')

# Show plot
plt.show()

# Key Takeaways:
# 1. Scatter plots are ideal for showing correlation between two variables
# 2. Logarithmic scales help visualize data spanning multiple orders of magnitude
# 3. GDP per capita varies greatly between countries (hundreds to tens of thousands)
# 4. Log scaling reveals patterns that linear scaling would obscure