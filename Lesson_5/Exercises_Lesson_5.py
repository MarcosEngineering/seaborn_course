# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 07:19:54 2026

@author: mcamp

"""


# ---------------------------Solution 5.1----------------------------------

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

# Built-in datasets
tips = sns.load_dataset("tips")


sns.displot(
    x="total_bill",
    data=tips,
    kind="kde",
    hue="time",
    fill=True
)
plt.show()



# --------------------------Solution 5.2-----------------------------------
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

# Built-in datasets
tips = sns.load_dataset("tips")

sns.lmplot(
    x="total_bill",
    y="tip",
    data=tips,
    hue="smoker",
    col="time"
)
plt.show()


# -------------------------Solution 5.3---------------------------------
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
# Built-in datasets
tips = sns.load_dataset("tips")

tips_corr = tips.select_dtypes(include="number").corr()
sns.heatmap(tips_corr, annot=True, fmt=".2f", cmap="YlGnBu")
plt.title("Tips Dataset Correlations")
plt.show()

