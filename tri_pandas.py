#%%
import pandas as pd
dataArr = [
    ['ajay', 12, 'male'],
    ['vijay', 95, 'male'],
    ['rashmi', 84, 'female']
]

df = pd.DataFrame(dataArr,
                  columns=['name', 'age', 'sexuality'],
                  index=[114,546,987])

# %%
# read dataframe from csv file using 'read_csv' function
df = pd.read_csv('data/personsDb.csv')

# %%
# read dataframe from xlsx file using 'read_excel' function
df = pd.read_excel('data/personsDb.xlsx')

# %%
# get all the column names of the dataframe using the 'columns' attribute
colNames = df.columns.tolist()
#print('The dataframe columns are {0}'.format(colNames))

# %%
# get all the items of a specific column name
# get all the names from the name column
names = df['name'].values.tolist()

print('All the names are {0}'.format(names))

# %%
# filtering the rows of a dataframe based upon its column values
# get the names of the people who are atleast 50 years
df2 = df[df['age']>=50]

# %%
# filter people who are male and atleast 50 years
df3 = df[(df['age']>=50) & (df['sexuality']=='Male')]

# %%
# get the names of only male people
df4 = df[df['sexuality'] == 'Male']
maleNames = df4['name'].values.tolist()
print('The male people are {0}'.format(', '.join(maleNames)))