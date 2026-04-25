# -*- coding: utf-8 -*-

"""
Exercise: Determine your next move
Course: Intermediate Python (DataCamp)
Section: Case Study: Hacker Statistics
Date: 2026-04-25
Student: Md. Ualiur Rahman Rahat

Description:
Use if-elif-else logic to determine next move in Empire State Building game based on dice roll.

Key Concepts:
- Conditional logic with multiple branches
- Dice probabilities: 1-2 (down), 3-5 (up), 6 (random up)
- Step tracking in random walk

Original Exercise Instructions:
- Roll dice with randint()
- If dice 1 or 2: step down
- If dice 3,4,5: step up
- If dice 6: step up by random amount (1-6)
- Print dice and new step
"""

import numpy as np

# Set seed for reproducibility
np.random.seed(123)

# Starting step (current position)
step = 50

# Roll the dice
dice = np.random.randint(1, 7)

# Finish the control construct
if dice <= 2:
    step = step - 1          # Move down 1 step
elif 3 <= dice <= 5:
    step = step + 1          # Move up 1 step
else:  # dice == 6
    step = step + np.random.randint(1, 7)  # Move up by random amount

# Print out dice and step
print(f"Dice: {dice}")
print(f"New step: {step}")

# Key Takeaways:
# 1. Different dice outcomes trigger different behaviors
# 2. 1-2: 33.3% chance, 3-5: 50% chance, 6: 16.7% chance
# 3. Can chain comparisons: 3 <= dice <= 5 (Python-specific)
# 4. Random walk depends on cumulative dice rolls
# 5. Game has positive bias (more ways to go up)