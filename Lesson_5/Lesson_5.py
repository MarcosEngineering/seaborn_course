# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 21:01:32 2026

@author: mcamp
"""

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

# Built-in datasets
mpg = sns.load_dataset("mpg").dropna().copy()
tips = sns.load_dataset("tips")

# -------------------------- Example 1 ---------------------------------------

# Histogram with a smooth KDE curve overlaid
sns.displot(
    x="mpg",
    data=mpg,
    kind="hist",
    bins=20,
    kde=True
)
plt.show()

# -------------------------- Example 2 ---------------------------------------

# Overlapping KDE curves to compare distributions by car origin
sns.displot(
    x="mpg",
    data=mpg,
    kind="kde",
    hue="origin",
    fill=True,
    alpha=0.35
)
plt.show()

# -------------------------- Example 3 ---------------------------------------

# Compute correlations across numerical columns
corr_matrix = mpg.select_dtypes(include="number").corr()

# Plot annotated heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(
    corr_matrix,
    annot=True,       # Display exact correlation values in each cell
    fmt=".2f",        # Round to 2 decimal places
    cmap="coolwarm",  # Diverging palette: blue (negative) to red (positive)
    center=0,
    linewidths=0.5
)
plt.title("Correlation Matrix of Car Features")
plt.show()

# -------------------------- Example 4 ---------------------------------------

# Quick overview of 4 key car variables, colored by origin
sns.pairplot(
    data=mpg[["mpg", "horsepower", "weight", "acceleration", "origin"]],
    hue="origin",
    corner=True  # Hides the redundant upper triangle of the grid
)
plt.show()

# -------------------------- Example 5 ---------------------------------------

# Joint scatter + marginal distributions for restaurant bills and tips
sns.jointplot(
    x="total_bill",
    y="tip",
    data=tips,
    kind="reg"  # Options: "scatter", "kde", "hist", "hex", "reg"
)
plt.show()
