# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 07:05:14 2026

@author: mcamp
"""

# -----------------Solution 1.1-------------------------

import seaborn as sns
import matplotlib.pyplot as plt

bills = [10.5, 15.0, 22.4, 30.0, 45.2, 18.7, 27.5]
tip_amounts = [1.5, 2.5, 3.5, 5.0, 8.0, 3.0, 4.2]


sns.scatterplot(x=bills, y=tip_amounts)
plt.show()

#----------------- Solution 1.2-------------------------

import seaborn as sns
import matplotlib.pyplot as plt

# Load a built-in pandas DataFrame from seaborn
tips = sns.load_dataset("tips")

sns.countplot(x="day", data=tips)
plt.show()

# ---------------Solution 1.3---------------------------
import seaborn as sns
import matplotlib.pyplot as plt

# Load a built-in pandas DataFrame from seaborn
tips = sns.load_dataset("tips")

sns.scatterplot(
    x="total_bill",
    y="tip",
    data=tips,
    hue="smoker",
    palette={"Yes": "red", "No": "blue"}
)
plt.show()

