import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

path = "/Users/katarinamakivic/Downloads/Refactored_Py_DS_ML_Bootcamp-master/"
df = pd.read_csv(path + "10-Data-Capstone-Projects/911.csv")

print(df.info())

print(df.head(3))

# What are the top 5 zipcodes for 911 calls?
print(df['zip'].value_counts().head(5))

# Take a look at the 'title' column, how many unique title codes are there
print(df['title'].nunique())

# In the 'titles' column there are "Reasons/Departments" specified before the title code. These are EMS, Fire,
# and Traffic. Use .apply() with a custom lambda expression to create a new column called "Reason" that contains this
# string value.
reasons = df['title'].apply(lambda title: title.split(':')[0])

df['Reason'] = reasons
print(df['Reason'].head())

# What is the most common Reason for a 911 call based off of this new column?
print(df['Reason'].value_counts().head())

plt.figure(1)
sns.countplot(x='Reason', data=df)

# plt.show()

# What is the data type of the objects in the timeStamp column?
print(type(df['timeStamp'].iloc[0]))

# convert the column from strings to DateTime objects
df['timeStamp'] = pd.to_datetime(df['timeStamp'])
print(type(df['timeStamp'].iloc[0]))

# Notice how the Day of Week is an integer 0-6. Use the .map() with this dictionary to map the actual string names to
# the day of the week:

# Now that the timestamp column are actually DateTime objects, use .apply() to create 3 new columns called Hour,
# Month, and Day of Week. You will create these columns based off of the timeStamp column

df['Hour'] = df['timeStamp'].apply(lambda time: time.hour)
df['Month'] = df['timeStamp'].apply(lambda time: time.month)
df['Day of Week'] = df['timeStamp'].apply(lambda time: time.dayofweek)

dmap = {0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun'}
df['Day of Week'] = df['Day of Week'].map(dmap)

print(df.head(5))

# se seaborn to create a countplot of the Day of Week column with the hue based off of the Reason column.
plt.figure(2)
plot = sns.countplot(x='Day of Week', data=df, hue='Reason', palette='viridis')
plot.set_ylim(0, 8000)
plot.legend(loc='center left', bbox_to_anchor=(1, 0.5))

# do the same for Month:
plt.figure(3)
plot = sns.countplot(x='Month', data=df, hue='Reason', palette='viridis')
plot.set_ylim(0, 8000)
plot.legend(loc='center left', bbox_to_anchor=(1, 0.5))

# plt.show()

# Now create a gropuby object called byMonth, where you group the DataFrame by the month column and use the count()
# method for aggregation. Use the head() method on this returned DataFrame.

groupMonth = df.groupby(['Month']).count()
print(groupMonth.head())

# simple plot off of the dataframe indicating the count of calls per month.
plt.figure(4)
groupMonth['title'].plot()

# Now see if you can use seaborn's lmplot() to create a linear fit on the number of calls per month. Keep in mind you
# may need to reset the index to a column.
sns.lmplot(x='Month', y='twp', data=groupMonth.reset_index())
plt.show()


