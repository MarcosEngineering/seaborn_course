# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 06:51:49 2026

@author: mcamp

"""

# -----------------------------Solution 2.1--------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Built-in car dataset (horsepower, mpg, cylinders, origin, model_year, etc.)
mpg = sns.load_dataset("mpg").dropna()

# Helper columns for categorical analysis
mpg["era"] = np.where(mpg["model_year"] >= 80, "1980s", "1970s")

sns.relplot(
    x="weight",
    y="mpg",
    data=mpg,
    kind="scatter",
    col="origin",
    col_order=["usa", "europe", "japan"],
    row="era",
    row_order=["1970s", "1980s"]
)
plt.show()



# -------------------------------Solution 2.2-----------------------------------
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Built-in car dataset (horsepower, mpg, cylinders, origin, model_year, etc.)
mpg = sns.load_dataset("mpg").dropna()


sns.relplot(
    x="horsepower",
    y="mpg",
    data=mpg,
    kind="scatter",
    size="cylinders",
    sizes=(30, 220),
    hue="origin",
    style="origin",
    alpha=0.65
)
plt.show()


# ----------------------------Solution 2.3-------------------------------------
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Built-in car dataset (horsepower, mpg, cylinders, origin, model_year, etc.)
mpg = sns.load_dataset("mpg").dropna()


sns.relplot(
    x="model_year",
    y="mpg",
    data=mpg,
    kind="line",
    hue="origin",
    style="origin",
    markers=True,
    dashes=False,
    errorbar="sd"
)
plt.show()

