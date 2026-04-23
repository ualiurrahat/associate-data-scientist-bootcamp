# -*- coding: utf-8 -*-

"""
Exercise: Build a histogram (1)
Course: Intermediate Python (DataCamp)
Section: Matplotlib
Date: 2026-04-22
Student: Md. Ualiur Rahman Rahat

Description:
Create a histogram to visualize the distribution of life expectancy across countries in 2007.

Key Concepts:
- Histograms for distribution analysis
- Default bin behavior (10 bins)
- Frequency distribution visualization

Original Exercise Instructions:
- Use plt.hist() to create a histogram of life_exp values
- Do not specify bins (Python defaults to 10)
- Add plt.show() to display the histogram
"""

# Create histogram of life_exp data
plt.hist(life_exp)

# Display histogram
plt.show()

# Key Takeaways:
# 1. Histograms show how data is distributed across different ranges
# 2. Default bin size (10) provides a reasonable starting point
# 3. Tallest bar shows the range containing most countries' life expectancy
# 4. Life expectancy appears clustered around certain values