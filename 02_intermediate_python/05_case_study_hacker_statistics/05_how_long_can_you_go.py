# -*- coding: utf-8 -*-

"""
Exercise: How low can you go?
Course: Intermediate Python (DataCamp)
Section: Case Study: Hacker Statistics
Date: 2026-04-25
Student: Md. Ualiur Rahman Rahat

Description:
Add boundary condition to prevent negative positions using max() function.

Key Concepts:
- max() returns largest value (prevents going below 0)
- Boundary constraints in simulations
- Real-world limits (can't go below ground floor)

Original Exercise Instructions:
- Use max() to ensure step never goes below 0
- Replace step = step - 1 with max(0, step - 1)
- Check resulting random_walk
"""

import numpy as np

# Set seed for reproducibility
np.random.seed(123)

# Initialize random_walk
random_walk = [0]

for x in range(100):
    step = random_walk[-1]
    dice = np.random.randint(1, 7)

    if dice <= 2:
        # Replace: use max to make sure step can't go below 0
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1, 7)

    random_walk.append(step)

print(random_walk)

# Key Takeaways:
# 1. max(0, step-1) prevents negative values
# 2. Without this, position could go negative (basement?)
# 3. Boundary reflects real-world constraint (ground floor minimum)
# 4. max() selects larger of two values
# 5. Essential for realistic simulations