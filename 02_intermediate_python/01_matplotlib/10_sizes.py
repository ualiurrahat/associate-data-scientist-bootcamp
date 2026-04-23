# -*- coding: utf-8 -*-

"""
Exercise: Sizes
Course: Intermediate Python (DataCamp)
Section: Matplotlib
Date: 2026-04-22
Student: Md. Ualiur Rahman Rahat

Description:
Adjust bubble sizes in a scatter plot to represent population data using numpy arrays.

Key Concepts:
- NumPy arrays for element-wise operations
- Using 's' parameter to control marker sizes
- Doubling array values with NumPy

Original Exercise Instructions:
- Import numpy as np
- Create numpy array np_pop from pop list
- Double np_pop values
- Pass np_pop to s parameter in plt.scatter()
"""



# Import matplotlib.pyplot as plt and numpy as np
import matplotlib.pyplot as plt
import numpy as np

# Gapminder 2007 data (sample of 10 countries for demonstration)
gdp_cap = [974.58, 5937.03, 6223.37, 13171.40, 33693.18, 42951.65, 127.79, 3413.48, 2042.95, 4720.00]
life_exp = [43.8, 72.4, 76.4, 80.2, 81.6, 82.2, 41.2, 70.0, 64.1, 74.8]
pop = [33.7, 127.5, 88.8, 128.2, 301.1, 62.3, 23.2, 192.2, 109.6, 54.5]  # in millions
col = ['blue', 'green', 'green', 'green', 'green', 'green', 'blue', 'red', 'red', 'green']  # continents mapped to colors

# Store pop as a numpy array: np_pop
np_pop = np.array(pop)

# Double np_pop
np_pop = np_pop * 2

# Update: set s argument to np_pop
plt.scatter(gdp_cap, life_exp, s=np_pop)

# Previous customizations
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000], ['1k', '10k', '100k'])

# Display the plot
plt.show()

# Key Takeaways:
# 1. NumPy arrays enable vectorized operations (multiplying entire array at once)
# 2. Bubble size adds a third dimension to scatter plots
# 3. Population as size reveals that large populations exist at various GDP levels
# 4. Doubling sizes makes differences more visually apparent
# 5. s parameter expects size values in points^2