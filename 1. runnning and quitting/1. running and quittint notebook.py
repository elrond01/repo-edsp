# Databricks notebook source
# MAGIC %md
# MAGIC 1. uno
# MAGIC 2. dos
# MAGIC 3. tres

# COMMAND ----------

age = 42
first_name = 'Ahmed'

# COMMAND ----------

print(first_name, 'is', age, 'years old')

# COMMAND ----------

age = age + 3
print(age)
      

# COMMAND ----------

print(first_name[0]+first_name[1:4])

# COMMAND ----------

species_name = "Acacia buxifolia"

# COMMAND ----------

species_name[2:8]

# COMMAND ----------

print(type(52))

# COMMAND ----------

separator = '=' * 10
print(separator)

# COMMAND ----------

print(1 + int('2'))
result = 3.25 + 4
print(result, 'is', type(result))

# COMMAND ----------

print('5 // 3:', 5 // 3)
print('5 / 3:', 5 / 3)
print('5 % 3:', 5 % 3)
