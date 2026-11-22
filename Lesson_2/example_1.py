# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 12:42:32 2026

@author: mcamp
"""

# Save a data set in local file and create a new data set

import numpy as np
import pandas as pd
import seaborn as sns

# 1. Built-in car dataset (horsepower, mpg, cylinders, origin, model_year, etc.)
mpg = sns.load_dataset("mpg").dropna()

# Save the mpg dataset to a CSV file
mpg.to_csv("mpg_dataset.csv", index=False)

# 2. Simulated hourly air pollution dataset acros Creats two city locations (3 days of readings)
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

# Save the simulated air pollution dataset to a CSV file
air_df.to_csv("air_pollution_dataset.csv", index=False)

print("Files saved successfully!")