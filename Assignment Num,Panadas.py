# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 12:14:53 2023

@author: User
"""

import pandas as pd

# Read the Iris dataset
iris_df = pd.read_csv('iris.csv')


#Display the columns in the dataset:
print("Columns in the dataset:")
print(iris_df.columns)


#Calculate the mean of each column:

column_means = iris_df.mean()
print("Mean of each column:")
print(column_means)

#Check for null values:

null_counts = iris_df.isnull().sum()
print("Null values in each column:")
print(null_counts)

#erform meaningful visualizations:


import seaborn as sns
import matplotlib.pyplot as plt

sns.pairplot(iris_df, hue='species')
plt.show()
#b. Boxplot:

sns.boxplot(x='species', y='sepal_length', data=iris_df)
plt.show()
#. Histogram:

plt.hist(iris_df['petal_length'], bins=20)
plt.xlabel('Petal Length')
plt.ylabel('Frequency')
plt.show()






