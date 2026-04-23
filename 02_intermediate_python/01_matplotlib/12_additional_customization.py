# -*- coding: utf-8 -*-

"""
Exercise: Additional Customizations
Course: Intermediate Python (DataCamp)
Section: Matplotlib
Date: 2026-04-22
Student: Md. Ualiur Rahman Rahat

Description:
Add text annotations for India and China, and enable gridlines for better readability.

Key Concepts:
- Text annotations with plt.text()
- Gridline customization with plt.grid()
- Comprehensive plot customization workflow

Original Exercise Instructions:
- Add plt.grid(True) after plt.text() calls
- Keep all existing customizations
"""


# Import matplotlib.pyplot as plt and numpy as np
import matplotlib.pyplot as plt
import numpy as np

# Gapminder 2007 data (sample of 10 countries for demonstration)
gdp_cap = [974.58, 5937.03, 6223.37, 13171.40, 33693.18, 42951.65, 127.79, 3413.48, 2042.95, 4720.00]
life_exp = [43.8, 72.4, 76.4, 80.2, 81.6, 82.2, 41.2, 70.0, 64.1, 74.8]
pop = [33.7, 127.5, 88.8, 128.2, 301.1, 62.3, 23.2, 192.2, 109.6, 54.5]  # in millions
col = ['blue', 'green', 'green', 'green', 'green', 'green', 'blue', 'red', 'red', 'green']  # continents mapped to colors
# Scatter plot
plt.scatter(x=gdp_cap, y=life_exp, s=np.array(pop) * 2, c=col, alpha=0.8)

# Previous customizations
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000], ['1k', '10k', '100k'])

# Additional customizations
plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')

# Add grid() call
plt.grid(True)

# Show the plot
plt.show()

# Key Takeaways:
# 1. Text annotations highlight specific countries of interest
# 2. Coordinates in plt.text() are data coordinates (x, y) positions
# 3. Gridlines provide reference points for reading values
# 4. Complete customization makes plots publication-ready
# 5. Multiple small improvements create professional visualizations