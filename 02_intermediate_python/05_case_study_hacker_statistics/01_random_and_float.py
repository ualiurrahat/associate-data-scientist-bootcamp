# -*- coding: utf-8 -*-

"""
Exercise: Random float
Course: Intermediate Python (DataCamp)
Section: Case Study: Hacker Statistics
Date: 2026-04-25
Student: Md. Ualiur Rahman Rahat

Description:
Generate random floats using numpy's random module and set seeds for reproducibility.

Key Concepts:
- np.random.seed() ensures reproducible random numbers
- np.random.rand() generates random float between 0 and 1
- Same seed = same sequence of random numbers

Original Exercise Instructions:
- Import numpy as np
- Set seed to 123 using seed()
- Generate random float with rand() and print it
"""

# Import numpy as np
import numpy as np

# Set the seed (for reproducibility)
np.random.seed(123)

# Generate and print random float
print(np.random.rand())

# Key Takeaways:
# 1. Random seeds make experiments reproducible
# 2. rand() always returns number between 0.0 and 1.0
# 3. Without seed, different random numbers each run
# 4. Same seed = same "random" numbers (pseudo-random)
# 5. Essential for debugging and sharing results