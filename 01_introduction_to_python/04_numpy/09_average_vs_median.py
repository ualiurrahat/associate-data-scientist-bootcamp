# -*- coding: utf-8 -*-

"""
Exercise: Average vs Median
Course: Introduction to Python (DataCamp)
Section: NumPy
Date: 2026-04-14
Student: Md. Ualiur Rahman Rahat

Description:
-----------
Mean and median are both measures of central tendency, but they respond differently to outliers.
- Mean: sum of all values / number of values (sensitive to outliers)
- Median: middle value when sorted (robust to outliers)
When mean and median are far apart, outliers are likely present.

Key Concepts:
------------
1. np.mean() - arithmetic average
2. np.median() - middle value
3. Outliers affect mean more than median
4. Large difference between mean and median indicates outliers

Original Exercise Instructions:
-------------------------------
1. Extract first column (height) from np_baseball
2. Print the mean of heights
3. Print the median of heights

Learning Note from Student:
--------------------------
In the MLB data, some height values were abnormally high (errors).
The mean was pulled higher by these outliers, but median stayed normal.
This is why median is often used for income data, house prices, etc.
"""

import numpy as np

# Create sample data with outliers
np.random.seed(42)
# Normal heights (66-78 inches) with a few outliers (90+ inches)
np_height_in = np.random.normal(72, 3, 1000)  # Normal distribution
# Add outliers (errors in data)
np_height_in = np.append(np_height_in, [95, 98, 102, 110])  # 4 outliers
np_height_in = np_height_in.astype(int)

print("Height Data Analysis (inches)")
print("=" * 50)
print(f"Total data points: {len(np_height_in)}")
print(f"Contains outliers: Yes (4 extremely high values)")

# Print out the mean of np_height_in
mean_height = np.mean(np_height_in)
print(f"\nMean height: {mean_height:.2f} inches")

# Print out the median of np_height_in
median_height = np.median(np_height_in)
print(f"Median height: {median_height:.2f} inches")

# Compare mean and median
difference = mean_height - median_height
print(f"\nDifference (mean - median): {difference:.2f} inches")

if abs(difference) > 2:
    print("⚠️ Large difference suggests outliers are present!")
    print("   Median is more reliable for this dataset.")
else:
    print("✓ Mean and median are close - data is likely clean.")


# ============================================================================
# Additional Practice (self-added):
# ============================================================================

print("\n--- Mean vs Median Comparison ---")

# Dataset without outliers
clean_data = np.random.normal(100, 10, 1000)
print(f"\nClean data (no outliers):")
print(f"  Mean: {np.mean(clean_data):.2f}")
print(f"  Median: {np.median(clean_data):.2f}")
print(f"  Difference: {np.mean(clean_data) - np.median(clean_data):.2f}")

# Dataset with outliers
data_with_outliers = np.append(clean_data, [1000, 2000, 3000])
print(f"\nData with outliers (added 1000,2000,3000):")
print(f"  Mean: {np.mean(data_with_outliers):.2f} (pulled up!)")
print(f"  Median: {np.median(data_with_outliers):.2f} (resistant)")
print(f"  Difference: {np.mean(data_with_outliers) - np.median(data_with_outliers):.2f}")

# Real-world example: salaries
salaries = np.array([35, 40, 42, 45, 48, 50, 52, 55, 60, 1000])  # 1000 = CEO salary
print(f"\nCompany salaries (in $1000s):")
print(f"  Mean salary: ${np.mean(salaries):.1f}K (inflated by CEO)")
print(f"  Median salary: ${np.median(salaries):.1f}K (typical employee)")
print(f"  → Median better represents 'typical' salary")

# When to use which
print("\n--- When to Use Mean vs Median ---")
print("Use MEAN when:")
print("  • Data is normally distributed (bell curve)")
print("  • No significant outliers")
print("  • You need all data points to contribute")
print("\nUse MEDIAN when:")
print("  • Data has outliers")
print("  • Data is skewed (e.g., income, house prices)")
print("  • You want a 'typical' value unaffected by extremes")


# ============================================================================
# Key Takeaways:
# ============================================================================
# 1. np.mean() = sum / n (sensitive to outliers)
# 2. np.median() = middle value (robust to outliers)
# 3. Large mean-median difference = outliers present
# 4. Mean is good for normal distributions
# 5. Median is better for skewed data or data with outliers
# 6. In data cleaning, always compare mean and median as a sanity check