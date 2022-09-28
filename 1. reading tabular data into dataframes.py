# Databricks notebook source
# MAGIC %fs

# COMMAND ----------

dbutils.fs.pwd()

# COMMAND ----------

import pandas as pd

data = pd.read_csv("/dbfs/mnt/data/gapminder_gdp_oceania.csv")

print(data)

# COMMAND ----------

mount_name = "data"
display(dbutils.fs.ls(f"/mnt/data"))

# COMMAND ----------

print(data.columns)

# COMMAND ----------

print(data.T)

# COMMAND ----------

data.describe()
      

# COMMAND ----------

americas = pd.read_csv('/dbfs/mnt/data/gapminder_gdp_americas.csv', index_col='country')
americas.describe()

# COMMAND ----------

americas_flipped.tail(n=3)
