# -*- coding: utf-8 -*-

"""
Exercise: Implement clumsiness
Course: Intermediate Python (DataCamp)
Section: Case Study: Hacker Statistics
Date: 2026-04-25
Student: Md. Ualiur Rahman Rahat

Description:
Add random "falling down" events with 0.5% probability to make simulation more realistic.

Key Concepts:
- Random events with small probability
- np.random.rand() generates float for probability check
- Reset position to 0 on rare events

Original Exercise Instructions:
- Simulate 20 random walks instead of 5
- Add clumsiness: if random float <= 0.005, set step to 0
- Visualize all walks
"""

import numpy as np
import matplotlib.pyplot as plt

# Set seed for reproducibility
np.random.seed(123)

# Clear the plot so it doesn't get cluttered
plt.clf()

# Simulate random walk 20 times
all_walks = []
for i in range(20):
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

        # Implement clumsiness (0.5% chance of falling)
        if np.random.rand() <= 0.005:
            step = 0  # Reset to ground floor

        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))
plt.plot(np_aw_t)
plt.title('20 Random Walks with Clumsiness (0.5% fall chance)')
plt.xlabel('Step Number')
plt.ylabel('Position')
plt.show()

# Key Takeaways:
# 1. np.random.rand() gives probability between 0 and 1
# 2. <= 0.005 means 0.5% chance event occurs
# 3. Clumsiness adds realistic risk of falling
# 4. Resets progress to zero (painful setback!)
# 5. Small probabilities can have big effects over many steps