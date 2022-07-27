import pandas as pd

# setup - read in csv
path = "/Users/katarinamakivic/Downloads/Refactored_Py_DS_ML_Bootcamp-master/"
sal = pd.read_csv(path + "04-Pandas-Exercises/Salaries.csv")

# 1
print(sal.head())
# 2
print(sal.info())
# 3
print(sal['BasePay'].mean())
# 4
print(sal['OvertimePay'].max())
# 4
print(sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle'])  # job title of Joseph
# 5
print(sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPay'])
# 6
print(sal[sal['TotalPay'] == sal['TotalPay'].max()])
# 7
print(sal.iloc[sal['TotalPay'].argmin()])
# 8
print(sal.groupby('Year').mean()['BasePay'])
# 9
print(sal['JobTitle'].nunique())
# 10
print(sal['JobTitle'].value_counts().head())
# 11
print(sum(sal[sal['Year'] == 2013].value_counts() == 1))


# 12
def find_chief(title):
    if 'chief' in title.lower().split():
        return True
    else:
        return False


print(sum(sal['JobTitle'].apply(lambda x: find_chief(x))))

# 13
# add a col to sal that contains the JobTitle length
sal['title_len'] = sal['JobTitle'].apply(len)
print(sal[['title_len', 'TotalPayBenefits']].corr())
