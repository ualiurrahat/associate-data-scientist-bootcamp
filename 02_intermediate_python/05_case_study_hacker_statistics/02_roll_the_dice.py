# -*- coding: utf-8 -*-

"""
Exercise: Roll the dice
Course: Intermediate Python (DataCamp)
Section: Case Study: Hacker Statistics
Date: 2026-04-25
Student: Md. Ualiur Rahman Rahat

Description:
Simulate dice rolls using numpy's randint() function for integer random numbers.

Key Concepts:
- np.random.randint(low, high) generates integers from low to high-1
- Simulates discrete uniform distribution
- Each roll is independent

Original Exercise Instructions:
- Use randint() to generate numbers 1 through 6 (simulate dice)
- Print first roll
- Print second roll (should be different)
"""

# Import numpy and set seed
import numpy as np
np.random.seed(123)

# Use randint() to simulate a dice (1-6 inclusive)
print(np.random.randint(1, 7))

# Use randint() again (different result)
print(np.random.randint(1, 7))

# Key Takeaways:
# 1. randint(1,7) generates 1,2,3,4,5,6 (7 is exclusive)
# 2. Upper bound is exclusive, lower is inclusive
# 3. Perfect for simulating dice, cards, or any discrete events
# 4. Each call generates new random number
# 5. Seed ensures same sequence across runs