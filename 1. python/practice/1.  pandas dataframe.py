# Databricks notebook source
import pandas as pd
data = pd.read_csv('/dbfs/mnt/data/gapminder_gdp_europe.csv', index_col='country')
print(data.iloc[0, 0])
print(data.loc["Albania", "gdpPercap_1952"])
print(data.loc["Albania", :])
print(data.loc['Italy':'Poland', 'gdpPercap_1962':'gdpPercap_1972'].min())


# COMMAND ----------

subset = data.loc['Italy':'Poland', 'gdpPercap_1962':'gdpPercap_1972']
print('Subset of data:\n', subset)

# Which values were greater than 10000 ?
print('\nWhere are values large?\n', subset > 10000)

# COMMAND ----------

mask = subset > 10000
print(subset[mask])

# COMMAND ----------

mask_higher = data > data.mean()
wealth_score = mask_higher.aggregate('sum', axis=1) / len(data.columns)
print(wealth_score)

# COMMAND ----------

print(data.groupby(wealth_score).sum())


# COMMAND ----------

first = pd.read_csv('/dbfs/mnt/data/gapminder_all.csv', index_col='country')
second = first[first['continent'] == 'Americas']
third = second.drop('Puerto Rico')
fourth = third.drop('continent', axis = 1)
fourth.to_csv('result.csv')

# COMMAND ----------

data = pd.read_csv('/dbfs/mnt/data/gapminder_gdp_europe.csv', index_col='country')
print(data.idxmin())
print(data.idxmax())

# COMMAND ----------

data['gdpPercap_2007']/data['gdpPercap_1952']

# COMMAND ----------

my_string = 'Hello world!'   # creation of a string object 
dir(my_string)
