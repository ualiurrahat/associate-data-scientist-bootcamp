# -*- coding: utf-8 -*-

"""
Exercise: The next step
Course: Intermediate Python (DataCamp)
Section: Case Study: Hacker Statistics
Date: 2026-04-25
Student: Md. Ualiur Rahman Rahat

Description:
Simulate 100 steps of random walk using a for loop, tracking position after each dice roll.

Key Concepts:
- For loops for simulation iterations
- Tracking state in list (random_walk)
- Accessing last element with index -1

Original Exercise Instructions:
- Initialize random_walk list with first step 0
- Run loop 100 times
- Each iteration: get last step, roll dice, update step, append
- Print final random_walk
"""

import numpy as np

# Set seed for reproducibility
np.random.seed(123)

# Initialize random_walk (start at position 0)
random_walk = [0]

# Complete the loop for 100 steps
for x in range(100):
    # Set step: last element in random_walk
    step = random_walk[-1]

    # Roll the dice
    dice = np.random.randint(1, 7)

    # Determine next step
    if dice <= 2:
        step = step - 1
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1, 7)

    # append next_step to random_walk
    random_walk.append(step)

# Print random_walk (101 positions: start + 100 moves)
print(random_walk)

# Key Takeaways:
# 1. random_walk[-1] always gives current position
# 2. List starts with position 0, then update after each roll
# 3. 101 elements total (initial 0 + 100 moves)
# 4. Negative steps possible (below ground)
# 5. Cumulative process shows path dependency