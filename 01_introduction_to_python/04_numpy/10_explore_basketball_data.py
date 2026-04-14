# -*- coding: utf-8 -*-

"""
Exercise: Explore the Baseball Data
Course: Introduction to Python (DataCamp)
Section: NumPy
Date: 2026-04-14
Student: Md. Ualiur Rahman Rahat

Description:
-----------
Summary statistics help understand data distribution:
- Mean: central tendency
- Median: robust central tendency
- Standard deviation: spread/variability
- Correlation: relationship between variables

Key Concepts:
------------
1. np.mean() - average value
2. np.median() - middle value
3. np.std() - standard deviation (measure of spread)
4. np.corrcoef() - correlation coefficient (-1 to 1)

Original Exercise Instructions:
-------------------------------
1. Print median height (already have mean)
2. Calculate standard deviation of heights
3. Calculate correlation between height and weight

Learning Note from Student:
--------------------------
Correlation coefficient interpretation:
- 1.0 = perfect positive correlation (taller = heavier)
- 0 = no correlation
- -1.0 = perfect negative correlation (taller = lighter)
Baseball players likely have positive correlation (taller players weigh more)
"""

import numpy as np

# Create sample baseball data (1000 players)
np.random.seed(42)
n_players = 1000

# Height: normal distribution around 72 inches
height = np.random.normal(72, 3, n_players)
# Weight: correlated with height (taller = heavier) + some randomness
weight = 4.5 * (height - 70) + 180 + np.random.normal(0, 10, n_players)
# Age: uniform between 20-40
age = np.random.uniform(20, 40, n_players)

np_baseball = np.column_stack([height, weight, age])

print("Baseball Data Summary Statistics")
print("=" * 50)

# Mean height (already in code)
avg = np.mean(np_baseball[:, 0])
print(f"Average height: {avg:.2f} inches")

# Print median height (complete this)
med = np.median(np_baseball[:, 0])
print(f"Median height: {med:.2f} inches")

# Print out the standard deviation on height
stddev = np.std(np_baseball[:, 0])
print(f"Standard Deviation (height): {stddev:.2f} inches")
print(f"  → 68% of players between {avg - stddev:.1f} and {avg + stddev:.1f} inches")

# Print out correlation between first and second column (height and weight)
corr = np.corrcoef(np_baseball[:, 0], np_baseball[:, 1])
print(f"\nCorrelation (height vs weight): {corr[0, 1]:.3f}")

# Interpret correlation
if corr[0, 1] > 0.7:
    interpretation = "Strong positive correlation"
elif corr[0, 1] > 0.3:
    interpretation = "Moderate positive correlation"
elif corr[0, 1] > 0:
    interpretation = "Weak positive correlation"
elif corr[0, 1] < -0.7:
    interpretation = "Strong negative correlation"
elif corr[0, 1] < -0.3:
    interpretation = "Moderate negative correlation"
else:
    interpretation = "Weak or no correlation"

print(f"  → {interpretation}")


# ============================================================================
# Additional Practice (self-added):
# ============================================================================

print("\n--- More Summary Statistics ---")

# Additional statistical measures
print(f"Min height: {np.min(np_baseball[:, 0]):.2f} inches")
print(f"Max height: {np.max(np_baseball[:, 0]):.2f} inches")
print(f"Range: {np.ptp(np_baseball[:, 0]):.2f} inches")  # ptp = peak-to-peak
print(f"25th percentile (Q1): {np.percentile(np_baseball[:, 0], 25):.2f}")
print(f"75th percentile (Q3): {np.percentile(np_baseball[:, 0], 75):.2f}")
print(f"IQR (interquartile range): {np.percentile(np_baseball[:, 0], 75) - np.percentile(np_baseball[:, 0], 25):.2f}")

# Correlation matrix (all variables)
print(f"\nFull Correlation Matrix:")
corr_matrix = np.corrcoef(np_baseball.T)  # Transpose for variables as rows
print("          Height  Weight    Age")
print(f"Height:   {corr_matrix[0,0]:.3f}   {corr_matrix[0,1]:.3f}   {corr_matrix[0,2]:.3f}")
print(f"Weight:   {corr_matrix[1,0]:.3f}   {corr_matrix[1,1]:.3f}   {corr_matrix[1,2]:.3f}")
print(f"Age:      {corr_matrix[2,0]:.3f}   {corr_matrix[2,1]:.3f}   {corr_matrix[2,2]:.3f}")

# Visualization of distribution (conceptual)
print("\n--- Height Distribution ---")
hist, bins = np.histogram(np_baseball[:, 0], bins=10)
print("Histogram (counts per bin):")
for i in range(len(hist)):
    bar = "█" * int(hist[i] / 10)
    print(f"{bins[i]:5.1f}-{bins[i+1]:5.1f}: {bar} ({hist[i]})")


# ============================================================================
# Key Takeaways:
# ============================================================================
# 1. np.std() measures spread (how data varies around mean)
# 2. 68-95-99.7 rule: 68% within 1 std, 95% within 2 std, 99.7% within 3 std
# 3. np.corrcoef() returns correlation matrix (diagonal = 1.0)
# 4. Correlation ranges from -1 (perfect negative) to +1 (perfect positive)
# 5. Correlation ≠ causation (but shows relationships)
# 6. Summary statistics are essential for Exploratory Data Analysis (EDA)
# 7. Always check multiple statistics (mean, median, std, min, max, percentiles)