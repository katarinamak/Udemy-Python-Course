import numpy as np
import pandas as pd
import matplotlib as mp

path = "/Users/katarinamakivic/Downloads/Refactored_Py_DS_ML_Bootcamp-master/"
df1 = pd.read_csv(path + "07-Pandas-Built-in-Data-Viz/df1")

df1['A'].plot.hist()
