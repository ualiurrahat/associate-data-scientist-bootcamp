# -*- coding: utf-8 -*-

"""
Exercise: Visualize the walk
Course: Intermediate Python (DataCamp)
Section: Case Study: Hacker Statistics
Date: 2026-04-25
Student: Md. Ualiur Rahman Rahat

Description:
Plot the random walk using matplotlib to visualize the path over time.

Key Concepts:
- Line plots for time series data
- plt.plot() with single argument (uses index as x-axis)
- Visual pattern recognition

Original Exercise Instructions:
- Import matplotlib.pyplot as plt
- Use plt.plot() to plot random_walk
- Display with plt.show()
"""

import numpy as np
import matplotlib.pyplot as plt

# Set seed for reproducibility
np.random.seed(123)

# Initialization
random_walk = [0]

for x in range(100):
    step = random_walk[-1]
    dice = np.random.randint(1, 7)

    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1, 7)

    random_walk.append(step)

# Import matplotlib.pyplot as plt (already imported)
# Plot random_walk (x-axis = step number, y-axis = position)
plt.plot(random_walk)

# Add labels for clarity
plt.xlabel('Step Number')
plt.ylabel('Position')
plt.title('Random Walk Simulation (100 Steps)')

# Show the plot
plt.show()

# Key Takeaways:
# 1. plt.plot() with one argument uses list index as x-axis
# 2. Visual reveals patterns: upward bias, occasional drops
# 3. Can see when boundary (0) is hit
# 4. Random walks look "jagged" and unpredictable
# 5. Visualization helps understand simulation results