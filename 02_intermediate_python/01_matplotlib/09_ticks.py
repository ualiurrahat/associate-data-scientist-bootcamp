# -*- coding: utf-8 -*-

"""
Exercise: Ticks
Course: Intermediate Python (DataCamp)
Section: Matplotlib
Date: 2026-04-22
Student: Md. Ualiur Rahman Rahat

Description:
Customize x-axis tick labels to show abbreviated values (1k, 10k, 100k) instead of full numbers.

Key Concepts:
- Customizing tick locations and labels with xticks()
- Improving readability with abbreviated labels
- Matching tick values to custom label text

Original Exercise Instructions:
- Use tick_val and tick_lab lists as inputs to xticks()
- Display plot after customization
"""

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Gapminder 2007 data (sample of 10 countries for demonstration)
gdp_cap = [974.58, 5937.03, 6223.37, 13171.40, 33693.18, 42951.65, 127.79, 3413.48, 2042.95, 4720.00]
life_exp = [43.8, 72.4, 76.4, 80.2, 81.6, 82.2, 41.2, 70.0, 64.1, 74.8]
pop = [33.7, 127.5, 88.8, 128.2, 301.1, 62.3, 23.2, 192.2, 109.6, 54.5]  # in millions
col = ['blue', 'green', 'green', 'green', 'green', 'green', 'blue', 'red', 'red', 'green']  # continents mapped to colors

# Scatter plot
plt.scatter(gdp_cap, life_exp)

# Previous customizations
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')

# Definition of tick_val and tick_lab
tick_val = [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']

# Adapt the ticks on the x-axis
plt.xticks(tick_val, tick_lab)

# After customizing, display the plot
plt.show()

# Key Takeaways:
# 1. Custom ticks replace default numeric labels with formatted text
# 2. First argument: positions where ticks appear
# 3. Second argument: labels to show at those positions
# 4. Abbreviations reduce clutter while maintaining information
# 5. Useful for currency, population, or other large numbers