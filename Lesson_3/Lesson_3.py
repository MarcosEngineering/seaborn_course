# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 10:39:54 2026

@author: mcamp
"""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set_theme(style="whitegrid")

# Load built-in car dataset
mpg = sns.load_dataset("mpg").dropna().copy()

# Helper columns for categorical analysis
mpg["era"] = np.where(mpg["model_year"] >= 80, "1980s", "1970s")
mpg["high_efficiency"] = mpg["mpg"] >= 25  # Boolean (True=1, False=0)

"""

# ----------------------- example 1 -----------------------------------                          

# Vertical count plot: How many cars come from each region?
sns.catplot(
    x="origin",
    data=mpg,
    kind="count",
    order=["usa", "japan", "europe"]
)
plt.show()

# ----------------------- example 2 -----------------------------------

# Horizontal count plot: Distribution of engine cylinder counts
sns.catplot(
    y="cylinders",
    data=mpg,
    kind="count"
)
plt.show()

# ----------------------- example 3 -----------------------------------

# What percentage of cars from each region achieve 25+ mpg?
sns.catplot(
    x="origin",
    y="high_efficiency",
    data=mpg,
    kind="bar",
    order=["usa", "europe", "japan"],
    errorbar=None
)
plt.show()


# ----------------------- example 4 -----------------------------------

# Horizontal bar plot of average horsepower by origin, without error bars
sns.catplot(
    x="horsepower",
    y="origin",
    data=mpg,
    kind="bar",
    order=["usa", "europe", "japan"],
    errorbar=None
)
plt.show()

# ----------------------- example 5 -----------------------------------

# Compare the distribution of fuel efficiency (mpg) across regions
sns.catplot(
    x="origin",
    y="mpg",
    data=mpg,
    kind="box",
    order=["usa", "europe", "japan"]
)
plt.show()

# ----------------------- example 6 -----------------------------------

# Box plot of horsepower by origin, hiding extreme outlier dots
sns.catplot(
    x="origin",
    y="horsepower",
    data=mpg,
    kind="box",
    order=["usa", "europe", "japan"],
    showfliers=True
)
plt.show()

# ----------------------- example 7 -----------------------------------

# Extend whiskers to the 5th and 95th percentiles for vehicle weight by cylinders
sns.catplot(
    x="cylinders",
    y="weight",
    data=mpg,
    kind="box",
    whis=[7, 93]
)
plt.show()


# ----------------------- example 8 -----------------------------------

# Plot MEDIAN horsepower by origin, with caps and no connecting line
sns.catplot(
    x="origin",
    y="horsepower",
    data=mpg,
    kind="point",
    order=["usa", "europe", "japan"],
    estimator="median",
    capsize=0.3,
    linestyle="none"
)
plt.show()

"""
# ----------------------- example 9 -----------------------------------

# Compare average mpg across origins, split by decade (1970s vs. 1980s)
g = sns.catplot(
    x="origin",
    y="mpg",
    data=mpg,
    kind="point",
    hue="era",
    order=["usa", "europe", "japan"],
    hue_order=["1970s", "1980s"],
    capsize=0.15
)
g.set_axis_labels("Manufacturing Origin", "Average Fuel Efficiency (mpg)")
g.fig.suptitle("Fuel Efficiency by Origin: 1970s vs. 1980s", y=1.03)
plt.show()

