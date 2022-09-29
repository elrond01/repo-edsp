# Databricks notebook source
# MAGIC %md
# MAGIC # EDSP Python Challenge

# COMMAND ----------

# MAGIC %md
# MAGIC ### 1. Complete the code below to print the value 3 from the given array

# COMMAND ----------

import numpy as np
np_2d=np.array([[2,3],[4,5],[6,7]])
np_2d[0,1]





# COMMAND ----------

# MAGIC %md
# MAGIC ### 2. Complete the code below to print the value [12,3] using slicing

# COMMAND ----------

x=[10,12,3,7,8]
print(x[1:3])



# COMMAND ----------

# MAGIC %md
# MAGIC ### 3. What is the following code printing? Please add a new cell to write your answer

# COMMAND ----------

p=1

q="EDSP"

print(q*p)

# COMMAND ----------

EDSP

# COMMAND ----------

# MAGIC %md
# MAGIC ### 4. Complete the code to return the output

# COMMAND ----------

import math

print(math.pi)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 5. Complete the code to return the output 3

# COMMAND ----------

distance=15

velocity=5

print(distance / velocity)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 6. Modify the code below to print [8,4,6]

# COMMAND ----------

import numpy as np
m = np.array([6, 2, 4])
n = np.array([2,2,2])
print(m + n)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 7. Complete the code to return the output

# COMMAND ----------

i = 1
while i < 5 :
  print(i)
  i += 1

# COMMAND ----------

# MAGIC %md
# MAGIC ### 8. Fill in the blanks so that the program below produces the following output:
# MAGIC 
# MAGIC first time: [1, 3, 5] 
# MAGIC 
# MAGIC second time: [3, 5]

# COMMAND ----------

values = []
values.append(1)
values.append(3)
values.append(5)
print('first time:', values)
values = values[1:]
print('second time:', values)


# COMMAND ----------

# MAGIC %md
# MAGIC ### 9. Please re-write the code so that the if-block is folded into a function.

# COMMAND ----------

import random
for i in range(10):

    # simulating the mass of a chicken egg
    # the (random) mass will be 70 +/- 20 grams
    mass = 70 + 20.0 * (2.0 * random.random() - 1.0)

    print(mass)
    if mass >= 85:
       print("jumbo")
    elif mass >= 70:
       print("large")
    elif mass < 70 and mass >= 55:
       print("medium")
    else:
       print("small")


# COMMAND ----------

def categorice (mass):
# egg sizing machinery prints a label
    if mass >= 85:
       print("jumbo")
    elif mass >= 70:
       print("large")
    elif mass < 70 and mass >= 55:
       print("medium")
    else:
       print("small")

import random
for i in range(10):

    # simulating the mass of a chicken egg
    # the (random) mass will be 70 +/- 20 grams
    mass = 70 + 20.0 * (2.0 * random.random() - 1.0)

    print(mass)
    categorice(mass)



# COMMAND ----------

# MAGIC %md
# MAGIC ### 10a. From the cars dataset (called data), select records with Maruti brand and mileage > 25

# COMMAND ----------

# importing the module
import pandas as pd
   
# creating a sample dataframe
data = pd.DataFrame({'Brand' : ['Maruti', 'Hyundai', 'Tata',
                                'Mahindra', 'Maruti', 'Hyundai',
                                'Renault', 'Tata', 'Maruti'],
                     'Year' : [2012, 2014, 2011, 2015, 2012, 
                               2016, 2014, 2018, 2019],
                     'Kms Driven' : [50000, 30000, 60000, 
                                     25000, 10000, 46000, 
                                     31000, 15000, 12000],
                     'City' : ['Gurgaon', 'Delhi', 'Mumbai', 
                               'Delhi', 'Mumbai', 'Delhi', 
                               'Mumbai','Chennai',  'Ghaziabad'],
                     'Mileage' :  [28, 27, 25, 26, 28, 
                                   29, 24, 21, 24]})
print(data)

# COMMAND ----------

data.loc[(data['Brand']=='Maruti') & (data['Mileage']>25)]

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC ### 10b. Select range of rows from 2 to 5 from the cars dataset (data).

# COMMAND ----------

data.iloc[2:6]

# COMMAND ----------

# MAGIC %md
# MAGIC ### 10c. Update the values of Mileage to be 22 if the Year < 2015 in the cars dataset (data).

# COMMAND ----------

updated = data['Year'] < 2015
data.loc[updated,'Mileage']= 22
data

# COMMAND ----------

# MAGIC %md
# MAGIC ### 10d. Select the 0th, 2nd, 4th, and 7th index rows from the cars dataset (data).

# COMMAND ----------

data.iloc[[0,2,4,7]]

# COMMAND ----------

# MAGIC %md
# MAGIC ### 11. Draw a line in a diagram from position (1, 3) to position (8, 10). 
# MAGIC 
# MAGIC It should look like this: 
# MAGIC 
# MAGIC <img src=plot.png>

# COMMAND ----------

import matplotlib.pyplot as plt

x = [ 1, 8]
y = [3, 10]

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('x')
