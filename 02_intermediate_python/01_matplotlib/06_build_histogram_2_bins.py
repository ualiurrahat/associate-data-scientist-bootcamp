# -*- coding: utf-8 -*-

"""
Exercise: Build a histogram (2): bins
Course: Intermediate Python (DataCamp)
Section: Matplotlib
Date: 2026-04-22
Student: Md. Ualiur Rahman Rahat

Description:
Compare histograms with different numbers of bins to understand bin size impact on data interpretation.

Key Concepts:
- Controlling histogram bin count with 'bins' parameter
- Trade-off between too few and too many bins
- Using plt.clf() to clear plots between visualizations

Original Exercise Instructions:
- Build histogram of life_exp with 5 bins
- Build another histogram with 20 bins
- Use plt.show() and plt.clf() between plots
"""
# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Life expectancy data for 2007 (all countries)
life_exp = [43.8, 72.4, 76.4, 80.2, 81.6, 82.2, 41.2, 70.0, 64.1, 74.8, 62.1, 79.5, 81.5, 78.5, 80.8, 46.2, 68.9, 75.3, 73.1, 71.9]

# Build histogram with 5 bins
plt.hist(life_exp, bins=5)

# Show and clean up plot
plt.show()
plt.clf()

# Build histogram with 20 bins
plt.hist(life_exp, bins=20)

# Show and clean up again
plt.show()
plt.clf()

# Key Takeaways:
# 1. 5 bins oversimplifies - loses detail about distribution shape
# 2. 20 bins shows more detail but may appear "noisy"
# 3. Optimal bin count balances detail and clarity
# 4. plt.clf() is essential for creating multiple separate plots
# 5. Bin count dramatically affects how patterns in data appear