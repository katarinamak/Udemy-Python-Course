import pandas as pd

path = "/Users/katarinamakivic/Downloads/Refactored_Py_DS_ML_Bootcamp-master/"
ecom = pd.read_csv(path + "04-Pandas-Exercises/Ecommerce Purchases")

# 1
print(ecom.head())

# 2
print(len(ecom))  # number of rows
print(len(ecom.columns))  # number of columns
print(ecom.shape)  # number of rows and columns
print(ecom.info())

# 3
print(ecom['Purchase Price'].mean())

# 4
print(ecom['Purchase Price'].max())

print(ecom['Purchase Price'].min())

# 5
print(sum(ecom['Language'] == 'en'))

# 6
print((ecom['Job'] == 'Lawyer').info())

# 7
print(ecom['AM or PM'].value_counts())

# 8
print(ecom['Job'].value_counts().head(5))

# 9
print(ecom[ecom['Lot'] == '90 WT']['Purchase Price'])

# 10
print(ecom[ecom['Credit Card'] == 4926535242672853]['Email'])

# 11
print(ecom[(ecom['CC Provider'] == 'American Express') & (ecom['Purchase Price'] > 95)].count())

# 12
print(sum(ecom['CC Exp Date'].apply(lambda x: x[3:] == '25')))


# 13


def get_email_provider(email):
    return email.split('@')[1]


print(ecom['Email'].apply(lambda email: email.split('@')[1]).value_counts().head(5))
