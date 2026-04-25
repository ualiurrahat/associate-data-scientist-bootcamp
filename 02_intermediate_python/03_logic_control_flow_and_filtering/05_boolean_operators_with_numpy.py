# -*- coding: utf-8 -*-

"""
Exercise: Boolean operators with NumPy
Course: Intermediate Python (DataCamp)
Section: Logic, Control Flow and Filtering
Date: 2026-04-25
Student: Md. Ualiur Rahman Rahat

Description:
Use NumPy's logical functions to combine boolean arrays since 'and/or/not' don't work with arrays.

Key Concepts:
- np.logical_and() for element-wise AND
- np.logical_or() for element-wise OR
- np.logical_not() for element-wise NOT
- Regular 'and'/'or' fails with arrays (throws ValueError)

Original Exercise Instructions:
- Which areas in my_house are > 18.5 OR < 10?
- Which areas are < 11 in BOTH my_house AND your_house?
"""

import numpy as np

# Create arrays
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than 18.5 or smaller than 10
print(np.logical_or(my_house > 18.5, my_house < 10))
# Returns: [False  True False  True]
# 20.0 qualifies (>18.5), 9.5 qualifies (<10)

# Both my_house and your_house smaller than 11
print(np.logical_and(my_house < 11, your_house < 11))
# Returns: [False False False  True]
# Only bathroom (9.5 and 9.0) satisfies both

# Key Takeaways:
# 1. Use np.logical_ functions, not Python 'and/or' with arrays
# 2. Regular 'and' would error: "ValueError: ambiguous truth value"
# 3. These functions are vectorized - work element-wise
# 4. Can chain multiple conditions with nested logical_ calls
# 5. Very useful for complex filtering conditions