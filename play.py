#%% 
import pandas as pd

pd.__version__


# %%
mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)
myvar


# %%
a = [1,2,3, "what"]
myvarr = pd.Series(a)
myvarr
# %%

data = [
    ['google', 10],
    ['amazon', 7],
    ['facebook', 5]
]

df = pd.DataFrame(data, columns=['site', 'Age'])

print(df)


# %%

a = ['google', 'amazon', 'facebook']

myvar = pd.Series(a, index=['x', 'y', 'z'])
myvar

# %%
sites = {
    1: 'google',
    2: 'amazon',
    3: 'facebook'
}
print(pd.Series(sites))
# %%
myvar = pd.Series(sites, index=[1, 2])
myvar

# %%
myvar = pd.Series(sites, index=[1, 2], name="my-Series-TEST")
myvar
# %%
data = [
    ['google', 10],
    ['amazon', 7],
    ['facebook', 5]
]

df = pd.DataFrame(data, columns=['site', 'Age'])
print(df)
df['site'] = df['site'].astype(str)
print(df)

df['Age'] = df['Age'].astype(float)
print(df)
# %%
data = [
    {'a': 1, 'b': 2},
    {'a': 5, 'b': 10, 'c': 20}
]

df = pd.DataFrame(data)
print(df)
# %%
data = {
    'calories': [420, 380, 390],
    'duration': [50, 40, 45]
}

df = pd.DataFrame(data)
print(df)
print(df.loc[0]) # first row
print(df.loc[1]) # second row

print(df.loc[2]) # third row
# print(df.loc[3]) # fourth row

print(df.loc[[0, 1]]) # first and second row
# %%
df = pd.DataFrame(data, index=['day1', 'day2', 'day3'])

print(df.loc['day2'])
# %%
