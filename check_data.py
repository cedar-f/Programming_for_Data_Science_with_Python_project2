import pandas as pd
from IPython.display import display
from tabulate import tabulate

df=pd.read_csv('./new_york_city.csv')

# print(df.describe())
#
# print(df.head())

print(tabulate(df.head(100),headers='keys',tablefmt='psql'))