# Databricks notebook source
from math import cos, pi

print('cos(pi) is', cos(pi))

# COMMAND ----------

import math as m

print('cos(pi) is', m.cos(m.pi))

# COMMAND ----------

print("sin(pi/2) =", m.sin(pi/2))
print("sin(pi/2) =", m.sin(m.pi/2))
print("sin(pi/2) =", math.sin(math.pi/2))

# COMMAND ----------

import pandas as pd

data = pd.read_csv('data/gapminder_gdp_oceania.csv')
print(data)

# COMMAND ----------

# STEP 1: RUN THIS CELL TO INSTALL BAMBOOLIB

# You can also install bamboolib on the cluster. Just talk to your cluster admin for that
%pip install bamboolib  

# Heads up: this will restart your python kernel, so you may need to re-execute some of your other code cells.

# COMMAND ----------

# STEP 2: RUN THIS CELL TO IMPORT AND USE BAMBOOLIB

import bamboolib as bam

# This opens a UI from which you can import your data
bam  

# Already have a pandas data frame? Just display it!
# Here's an example
# import pandas as pd
# df_test = pd.DataFrame(dict(a=[1,2]))
# df_test  # <- You will see a green button above the data set if you display it

# COMMAND ----------

print(df)
