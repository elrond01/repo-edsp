# Databricks notebook source
import pandas as pd
for filename in ['/dbfs/mnt/data/gapminder_gdp_africa.csv', '/dbfs/mnt/data/gapminder_gdp_asia.csv']:
    data = pd.read_csv(filename, index_col='country')
    print(filename, data.min())

# COMMAND ----------

import glob
print('all csv files in data directory:', glob.glob('/dbfs/mnt/data/*.csv'))

# COMMAND ----------

print('all PDB files:', glob.glob('*.pdb'))

# COMMAND ----------

# MAGIC %scala
# MAGIC dbutils.notebook.getContext.notebookPath

# COMMAND ----------

# MAGIC %sh
# MAGIC pwd
# MAGIC ls

# COMMAND ----------

# MAGIC %sh ls /Workspace/Repos/oscar.eduardo.gonzalez@microsoft.com/repo-edsp

# COMMAND ----------

# MAGIC %sh
# MAGIC ls /databricks/
