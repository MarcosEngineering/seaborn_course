# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 07:02:49 2026

@author: mcamp

"""

# ----------------------------Solution 3.1-------------------------------------

import matplotlib.pyplot as plt
import seaborn as sns

# 1. Built-in car dataset (horsepower, mpg, cylinders, origin, model_year, etc.)
mpg = sns.load_dataset("mpg").dropna()
mpg["high_efficiency"] = mpg["mpg"] >= 25  # Boolean (True=1, False=0)

sns.catplot(
    x="origin",
    y="high_efficiency",
    data=mpg,
    kind="bar",
    order=["usa", "europe", "japan"],
    errorbar=None
)
plt.show()



# -------------------------------Solution 3.2-----------------------------------

import matplotlib.pyplot as plt
import seaborn as sns

# 1. Built-in car dataset (horsepower, mpg, cylinders, origin, model_year, etc.)
mpg = sns.load_dataset("mpg").dropna()

sns.catplot(
    x="origin",
    y="horsepower",
    data=mpg,
    kind="box",
    showfliers=False,
    whis=[5, 95]
)
plt.show()


# -------------------------------Solution 3.3----------------------------------
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Built-in car dataset (horsepower, mpg, cylinders, origin, model_year, etc.)
mpg = sns.load_dataset("mpg").dropna()
# Helper columns for categorical analysis
mpg["era"] = np.where(mpg["model_year"] >= 80, "1980s", "1970s")

sns.catplot(
    x="origin",
    y="mpg",
    data=mpg,
    kind="point",
    hue="era",
    estimator="median",
    capsize=0.2,
    linestyle="none"
)
plt.show()

