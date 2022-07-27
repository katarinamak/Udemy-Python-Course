import numpy as np
import pandas as pd

import matplotlib.pyplot as mp

path = "/Users/katarinamakivic/Downloads/Refactored_Py_DS_ML_Bootcamp-master/"
df = pd.read_csv(path + "10-Data-Capstone-Projects/911.csv")

print(df.info())

print(df.head(3))

# What are the top 5 zipcodes for 911 calls?
print(df['zip'].value_counts().head(5))

# Take a look at the 'title' column, how many unique title codes are there
print(df['title'].nunique())

# In the titles column there are "Reasons/Departments" specified before the title code. These are EMS, Fire,
# and Traffic. Use .apply() with a custom lambda expression to create a new column called "Reason" that contains this
# string value.


