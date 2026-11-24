# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 08:44:18 2026

@author: mcamp
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# 1. Standard mpg dataset
mpg = sns.load_dataset("mpg").dropna().copy()
mpg["era"] = np.where(mpg["model_year"] >= 80, "1980s", "1970s")
mpg["high_efficiency"] = mpg["mpg"] >= 25

# 2. Daily Air Quality Dataset
np.random.seed(42)
days = 7
hours = np.tile(np.arange(0, 24), days * 2)
locations = np.repeat(["Downtown", "Suburb"], 24 * days)
morning_peak = 22 * np.exp(-0.5 * ((hours - 8) / 2.2) ** 2)
evening_peak = 26 * np.exp(-0.5 * ((hours - 18) / 2.5) ** 2)
baseline = np.where(locations == "Downtown", 30, 14)
noise = np.where(
    locations == "Downtown",
    np.random.normal(0, 6.5, size=len(hours)),
    np.random.normal(0, 3.0, size=len(hours))
)
air_df = pd.DataFrame({
    "hour": hours,
    "NO_2_mean": np.clip(baseline + morning_peak + evening_peak + noise, 5, None),
    "location": locations
})

"""

# --------------------------- Example 1 ------------------------------

# Apply a clean ticks style globally
sns.set_style("ticks")

# Apply the "colorblind" palette to ensure accessibility
sns.relplot(
    x="horsepower",
    y="mpg",
    data=mpg,
    kind="scatter",
    hue="origin",
    palette="colorblind"
)
plt.show()


# ---------------------------- Example 2 ------------------------------


# Temporarily scale up the visual elements for a presentation
sns.set_context("talk")

sns.relplot(
    x="horsepower",
    y="mpg",
    data=mpg,
    kind="scatter",
    hue="origin"
)
plt.show()


# Reset to standard notebook size for the rest of the lesson
sns.set_context("notebook")


# ------------------------------ Example 3 ------------------------------

# Custom categorical mapping dictionary
origin_colors = {
    "usa": "#3c5087",      # Blue
    "japan": "#d82d2d",    # Red
    "europe": "#3fa34d"    # Green
}

sns.relplot(
    x="horsepower",
    y="mpg",
    data=mpg,
    kind="scatter",
    hue="origin",
    palette=origin_colors
)
plt.show()


# ------------------------------ Example 4  ------------------------------

# Build a categorical plot (returns a FacetGrid)
g = sns.catplot(
    x="origin",
    y="mpg",
    data=mpg,
    kind="box",
    col="era"
)

# 1. Add a global figure title
g.fig.suptitle("Fuel Efficiency: 1970s vs 1980s by Origin", y=1.05, fontsize=16, fontweight="bold")

# 2. Add custom titles to individual subplot panels
g.set_titles("Era: {col_name}")

# 3. Label the X and Y axes cleanly
g.set_axis_labels("Manufacturing Region", "Miles Per Gallon (mpg)")

plt.show()

# ------------------------------ Example 5  ------------------------------


# Build an axes-level plot (returns an AxesSubplot)
ax = sns.boxplot(
    x="origin",
    y="mpg",
    data=mpg
)

# Add a title & customize axis labels
ax.set_title("Distribution of Fuel Efficiency by Origin", fontsize=14, pad=15)
ax.set_xlabel("Country of Origin")
ax.set_ylabel("Miles Per Gallon (mpg)")

plt.show()

# ------------------------------ Example 6  ------------------------------

g = sns.catplot(
    x="cylinders",
    y="horsepower",
    data=mpg,
    kind="box"
)
g.fig.suptitle("Horsepower by Cylinder Count", y=1.04)

# Rotate labels 45 degrees
plt.xticks(rotation=45)
plt.show()


# ------------------------------ Example 7 ------------------------------

#Choose a sharp dark background with tick marks
sns.set_style("darkgrid")

g = sns.catplot(
    x="origin",
    y="weight",
    data=mpg,
    kind="box",
    hue="era",
    palette="muted"
)

# Design elements and clean labels
g.fig.suptitle("Vehicle Weight Distribution by Era and Origin", y=1.05, fontweight="semibold")
g.set_axis_labels("Country of Origin", "Vehicle Weight (lbs)")

# Customize the legend Title
g._legend.set_title("Manufacture Era")

plt.show()

"""

# ------------------------------ Example 8 ------------------------------

sns.set_style("whitegrid")
sns.set_context("talk") # Emphasize fonts and ticks

# Multi-panel bar plot showing high-efficiency percentages
g = sns.catplot(
    x="origin",
    y="high_efficiency",
    data=mpg,
    kind="bar",
    col="era",
    hue="cylinders",
    palette="viridis",
    errorbar=None
)

# Setup subplots, labels and precise titles
g.fig.suptitle("Proportion of Fuel Efficient Cars (>= 25 MPG)", y=1.08, fontweight="bold")
g.set_axis_labels("Origin Region", "Proportion reaching 25+ MPG")
g.set_titles("{col_name} Production")

# Fix overlapping tick label margins
for ax in g.axes.flat:
    plt.sca(ax)
    plt.xticks(rotation=30)

plt.show()

# Reset the scale context
sns.set_context("notebook")
