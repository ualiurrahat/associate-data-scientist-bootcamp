# -*- coding: utf-8 -*-

"""
Exercise: Colors
Course: Intermediate Python (DataCamp)
Section: Matplotlib
Date: 2026-04-22
Student: Md. Ualiur Rahman Rahat

Description:
Add color coding by continent and adjust transparency (alpha) to enhance plot readability.

Key Concepts:
- Color mapping categorical variables using 'c' parameter
- Transparency control with 'alpha' parameter (0 to 1)
- Visual encoding of multiple dimensions

Original Exercise Instructions:
- Add c=col argument to plt.scatter()
- Add alpha=0.8 for 80% opacity
- Keep previous customizations
"""

# Import matplotlib.pyplot as plt and numpy as np
import matplotlib.pyplot as plt
import numpy as np


# Gapminder 2007 data (sample of 10 countries for demonstration)
gdp_cap = [974.58, 5937.03, 6223.37, 13171.40, 33693.18, 42951.65, 127.79, 3413.48, 2042.95, 4720.00]
life_exp = [43.8, 72.4, 76.4, 80.2, 81.6, 82.2, 41.2, 70.0, 64.1, 74.8]
pop = [33.7, 127.5, 88.8, 128.2, 301.1, 62.3, 23.2, 192.2, 109.6, 54.5]  # in millions
col = ['blue', 'green', 'green', 'green', 'green', 'green', 'blue', 'red', 'red', 'green']  # continents mapped to colors

# Specify c and alpha inside plt.scatter()
plt.scatter(x=gdp_cap, y=life_exp, s=np.array(pop) * 2, c=col, alpha=0.8)

# Previous customizations
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000], ['1k', '10k', '100k'])

# Show the plot
plt.show()

# Key Takeaways:
# 1. Color adds a fourth dimension (continent) to the visualization
# 2. Alpha transparency reveals overlapping/overplotted points
# 3. Lower alpha (more transparent) helps see density where points cluster
# 4. Different continents show distinct GDP-life expectancy patterns
# 5. Named parameters (x=, y=, s=, c=) improve code readability