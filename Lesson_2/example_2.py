# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 12:42:32 2026

@author: mcamp
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# 1. Built-in car dataset (horsepower, mpg, cylinders, origin, model_year, etc.)
mpg = sns.load_dataset("mpg").dropna()

# 2. Simulated hourly air pollution dataset across two city locations (3 days of readings)
np.random.seed(42)
hours = np.tile(np.arange(0, 24), 6)
locations = np.repeat(["Downtown", "Suburb"], 72)
base_pattern = 25 + 15 * np.sin((hours - 6) * np.pi / 12) ** 2
offset = np.where(locations == "Downtown", 18, 0)
no2_level = base_pattern + offset + np.random.normal(0, 4, size=len(hours))

air_df = pd.DataFrame({
    "hour": hours,
    "NO_2_mean": no2_level,
    "location": locations
})

"""

# ----------------------------1 GRAPH------------------------------------------

# Basic scatter plot using relplot()
sns.relplot(x="horsepower", y="mpg", data=mpg, kind="scatter")
plt.show() 




# ----------------------------2 GRAPH------------------------------------------

# Separate horizontal subplots by car origin
sns.relplot(
    x="horsepower",
    y="mpg",
    data=mpg,
    kind="scatter",
    col="origin",
    col_order=["usa", "europe", "japan"]
)
plt.show()


# ----------------------------3 GRAPH------------------------------------------

# Point size and color both reflect the number of cylinders
sns.relplot(
    x="horsepower",
    y="mpg",
    data=mpg,
    kind="scatter",
    size="cylinders",
    hue="cylinders"
)
plt.show()


# ----------------------------4 GRAPH------------------------------------------

# Distinguish car origins by both color and marker shape, with slight transparency
sns.relplot(
    x="horsepower",
    y="mpg",
    data=mpg,
    kind="scatter",
    hue="origin",
    style="origin",
    alpha=0.6
)
plt.show()


# ----------------------------5 GRAPH------------------------------------------

# Track how average NO2 air pollution changes over a 24-hour day
sns.relplot(
    x="hour",
    y="NO_2_mean",
    data=air_df,
    kind="line"
)
plt.show()



# ----------------------------6 GRAPH------------------------------------------

# Replace the 95% confidence interval with standard deviation
sns.relplot(
    x="hour",
    y="NO_2_mean",
    data=air_df,
    kind="line",
    errorbar="sd"
)
plt.show()


# ----------------------------7 GRAPH------------------------------------------

# Turn off the shaded band completely
sns.relplot(
    x="hour",
    y="NO_2_mean",
    data=air_df,
    kind="line",
    errorbar=None
)
plt.show()

"""

# ----------------------------8 GRAPH------------------------------------------

# Compare Downtown vs. Suburb pollution over 24 hours
sns.relplot(
    x="hour",
    y="NO_2_mean",
    data=air_df,
    kind="line",
    hue="location",
    style="location",
    markers=True,
    dashes=False,
    errorbar="sd"
)
plt.show()
