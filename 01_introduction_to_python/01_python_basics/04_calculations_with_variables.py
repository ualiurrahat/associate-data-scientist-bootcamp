#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Exercise: Calculations with Variables
Course: Introduction to Python (DataCamp)
Section: Python Basics
Date: 2026-04-11
Student: Md. Ualiur Rahman Rahat

Description:
-----------
Variables can be used in mathematical expressions just like numbers.
The result of an expression can be stored in a new variable.
This allows dynamic calculations where changing inputs automatically updates outputs.

Key Concepts:
------------
1. Use variables in calculations instead of hardcoded numbers
2. Assign expression results to new variables
3. Variables make code readable and maintainable

Original Exercise Instructions:
-------------------------------
1. Create monthly_savings = 10 and num_months = 4
2. Multiply them and store in new_savings
3. Print new_savings

Learning Note from Student:
--------------------------
This is the foundation of all data science calculations:
- Changing monthly_savings or num_months automatically updates new_savings
- No need to recalculate manually
"""

# Create variables with starting values
monthly_savings = 10   # Amount saved per month (integer)
num_months = 4         # Number of months to save (integer)

# Calculate total savings: monthly amount × number of months
# This evaluates to 10 * 4 = 40
new_savings = monthly_savings * num_months

# Display the result
print(new_savings)     # Output: 40

# ============================================================================
# Additional Practice (self-added):
# ============================================================================

# What if savings change? Variables make this easy to update
monthly_savings = 25   # Changed from 10 to 25
new_savings = monthly_savings * num_months
print(f"If I save ${monthly_savings}/month for {num_months} months: ${new_savings}")

# Calculate different scenarios
print("\n--- Savings Scenarios ---")
for months in [3, 6, 12]:
    total = monthly_savings * months
    print(f"{months} months: ${total}")

# ============================================================================
# Key Takeaways:
# ============================================================================
# 1. Variables make calculations dynamic and reusable
# 2. Changing input variables automatically affects results
# 3. This is the basis for any data analysis that involves formulas
# 4. Variables can be combined with operators (+, -, *, /, etc.)