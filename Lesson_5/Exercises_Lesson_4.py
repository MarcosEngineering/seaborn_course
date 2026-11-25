# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 07:10:07 2026

@author: mcamp

"""

# ----------------------------Solution 4.1-------------------------------------

import matplotlib.pyplot as plt
import seaborn as sns

# 1. Built-in car dataset (horsepower, mpg, cylinders, origin, model_year, etc.)
mpg = sns.load_dataset("mpg").dropna()


sns.set_style("ticks")
sns.set_context("talk")
custom_palette = {"usa": "#1f77b4", "europe": "#2ca02c", "japan": "#d62728"}

sns.relplot(
    x="horsepower",
    y="mpg",
    data=mpg,
    kind="scatter",
    hue="origin",
    palette=custom_palette
)
plt.show()
sns.set_context("notebook")


# -------------------Solution 4.2 (Part 1 - AxesSubplot)-----------------------

import seaborn as sns
import matplotlib.pyplot as plt

# Load a built-in pandas DataFrame from seaborn
tips = sns.load_dataset("tips")


ax = sns.boxplot(x="day", y="total_bill", data=tips)
ax.set_title("Total Bill by Day")
plt.show()




# -------------------------------Solution 4.3-------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Built-in car dataset (horsepower, mpg, cylinders, origin, model_year, etc.)
mpg = sns.load_dataset("mpg").dropna()
# Helper columns for categorical analysis
mpg["era"] = np.where(mpg["model_year"] >= 80, "1980s", "1970s")

sns.set_style("whitegrid")
g = sns.catplot(
    x="origin",
    y="horsepower",
    data=mpg,
    kind="bar",
    col="era",
    hue="cylinders",
    palette="viridis",
    errorbar=None
)
g.fig.suptitle("Average Horsepower by Origin, Cylinders & Era", y=1.05, fontweight="bold")
g.set_axis_labels("Origin Region", "Average Horsepower")

for ax in g.axes.flat:
    plt.sca(ax)
    plt.xticks(rotation=30)

plt.show()