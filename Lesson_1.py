# -*- coding: utf-8 -*-

"""
Created on Wed Nov 18 07:12:23 2026

@author: mcamp

"""

#-------------Example 1-----------------------

import seaborn as sns
import matplotlib.pyplot as plt

# Preparate our data (Standard python List)

heights=[160,170,175,178,180,172,176,177,179,181]
weights=[67,75,77,81,85,77,87,78,87,75]

# Create the scatter plot

sns.scatterplot(x=heights,y=weights)

# costomize and dysplay

plt.title("Height vs Weights")
plt.xlabel ("Height (cm)")
plt.ylabel("Weight (kg)")
plt.show()


#-------------Example 2-----------------------

import seaborn as sns
import matplotlib.pyplot as plt

# categorial data list
grades = ["A","B","C","B","B","C","C","B","C"]

# Create count plot
sns.countplot(x=grades)

# styling

plt.title("Frequency of Student Grades")
plt.xlabel("Grades received")
plt.ylabel("Count")
plt.show()

#-------------Example 3-----------------------

import seaborn as sns
import matplotlib.pyplot as plt

# Load a built-in pandas DataFrame from seaborn

tips= sns.load_dataset("tips")

sns.countplot(data=tips, x="day")

plt.title("Number of Transactions by Day")

plt.show()

# print(tips.head())

#-------------Example 4-----------------------

import seaborn as sns
import matplotlib.pyplot as plt

# Load a built-in pandas DataFrame from seaborn

tips= sns.load_dataset("tips")

# Use "hue" to color points by the "time column

sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time")

plt.title("Tips vs Total Bill (Lunch vs Dinner)")

plt.show()

#-------------Example 5-----------------------

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.countplot(data=tips, x="day",hue="sex")

plt.title("Bill Payers by Day and Gender")

plt.show()



















