# -*- coding: utf-8 -*-

"""
Exercise: Line plot (1)
Course: Intermediate Python (DataCamp)
Section: Matplotlib
Date: 2026-04-22
Student: Md. Ualiur Rahman Rahat

Description:
Create a basic line plot showing world population growth from 1950 to 2100 using matplotlib.

Key Concepts:
- Importing matplotlib.pyplot module
- Basic line plot creation with plt.plot()
- Displaying plots with plt.show()
- Accessing list elements with negative indexing

Original Exercise Instructions:
- Print the last item from both the year and pop list to see the predicted population for 2100
- Import matplotlib.pyplot as plt
- Use plt.plot() to build a line plot with year on x-axis, pop on y-axis
- Display the plot with plt.show()
"""
# Sample data: World population (billions) from World Bank estimates
year = [1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020, 2030, 2040, 2050, 2060, 2070, 2080, 2090, 2100]
pop = [2.5, 3.0, 3.7, 4.4, 5.3, 6.1, 6.9, 7.8, 8.5, 9.2, 9.8, 10.3, 10.7, 11.0, 11.2, 11.3]
# Print the last item from year and pop
print(year[-1])
print(pop[-1])

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Make a line plot: year on the x-axis, pop on the y-axis
plt.plot(year, pop)

# Display the plot with plt.show()
plt.show()

# Key Takeaways:
# 1. Negative indexing (-1) accesses the last element of a list
# 2. plt.plot() takes two main arguments: x-axis data, then y-axis data
# 3. plt.show() is required to render and display the plot
# 4. matplotlib.pyplot is conventionally imported as plt for brevity