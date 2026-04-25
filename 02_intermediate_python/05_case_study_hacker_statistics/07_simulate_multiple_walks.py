# -*- coding: utf-8 -*-

"""
Exercise: Simulate multiple walks
Course: Intermediate Python (DataCamp)
Section: Case Study: Hacker Statistics
Date: 2026-04-25
Student: Md. Ualiur Rahman Rahat

Description:
Run multiple random walk simulations to collect statistics across different runs.

Key Concepts:
- Nested loops: outer loop for simulations, inner for steps
- Collecting results in list of lists
- Multiple simulations for statistical analysis

Original Exercise Instructions:
- Simulate random walk 5 times
- Append each random_walk to all_walks list
- Print all_walks after simulations
"""

import numpy as np

# Set seed for reproducibility
np.random.seed(123)

# Initialize all_walks (list to store all simulations)
all_walks = []

# Simulate random walk five times
for i in range(5):
    # Code from before
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

    # Append random_walk to all_walks
    all_walks.append(random_walk)

# Print all_walks (5 walks, each with 101 positions)
print(f"Number of simulations: {len(all_walks)}")
print(f"Length of each walk: {len(all_walks[0])}")
print(f"First simulation: {all_walks[0][:10]}...")  # Show first 10 steps

# Key Takeaways:
# 1. Nested loops: outer controls simulations, inner controls steps
# 2. all_walks stores results for all simulations
# 3. Multiple runs reveal variability between simulations
# 4. List of lists structure: all_walks[simulation][step]
# 5. Essential for probability calculations