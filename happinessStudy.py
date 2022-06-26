import pandas as pd

data = pd.read_csv('/Users/katarinamakivic/Downloads/World Happiness data/2019.csv')

header = next(csvreader)
print(header)

rows = []
for row in csvreader:
    rows.append(row)

print(rows)

file.close()
