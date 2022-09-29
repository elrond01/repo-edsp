# Databricks notebook source
for number in [2, 3, 5]:
    print(number)

# COMMAND ----------

primes = [2, 3, 5]cumulative = []

for p in primes:
    squared = p ** 2
    cubed = p ** 3
    print(p, squared, cubed)

# COMMAND ----------

total = 0
for number in range(10):
   total = total + (number + 1)
print(total)

# COMMAND ----------

cumulative = []
total = 0
data = [1,2,2,5]
for number in data:
    cumulative.append(total)
    total = total + number
print(cumulative)


# COMMAND ----------

masses = [3.54, 2.07, 9.22, 1.86, 1.71]
for m in masses:
    if m > 3.0:
        print(m, 'is large')

# COMMAND ----------

masses = [3.54, 2.07, 9.22, 1.86, 1.71]
for m in masses:
    if m > 9.0:
        print(m, 'is HUGE')
    elif m > 3.0:
        print(m, 'is large')
    else:
        print(m, 'is small')

# COMMAND ----------

import glob
import pandas as pd
for filename in glob.glob('data/*.csv'):
    contents = pd.read_csv(filename)
    if len(contents) < 50:
        print(filename, len(contents))
