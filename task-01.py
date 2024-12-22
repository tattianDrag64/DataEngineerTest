# Task 1: Python Task

# Objective: Assess the candidate's Python programming skills, including problem-solving, code readability, and use of libraries.

# Problem: Analyze a dataset and generate insights

#   Download the Iris dataset.

#   url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# Write a Python script that:

import pandas as pd 
import numpy as np

#   + Loads the Iris dataset into a Pandas DataFrame.

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data" 
table_col = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"] 
iris_dataset = pd.read_csv(url, header=None, names=table_col)


#   + Performs basic exploratory data analysis (EDA), including:
#   + Summary statistics for each feature (mean, median, standard deviation).


# print("First 5 rows of the dataset:")
# print(iris_dataset.head())

# print("\nStatistics for num colums:")
# print(iris_dataset.describe())

# mean_values = iris_dataset.iloc[:, :-1].mean()
# std_values = iris_dataset.iloc[:, :-1].std()

# print("\nMean values for numeric columns:")
# print(mean_values)

# print("\nStandard deviation for numeric columns:")
# print(std_values)

# median_values = iris_dataset.iloc[:, :-1].median()

# print("\nMedian values for numeric columns:")
# print(median_values)

# # The count of unique values in the "species" column.

# print("\nNumber of unique values in the 'species' column:")
# print(iris_dataset['species'].value_counts())

#   Generates a histogram for one numeric feature and a scatter plot comparing two features.

import matplotlib.pyplot as plt
import seaborn as sns 

# sns.histplot(iris_dataset['sepal_length'], kde = True)
# plt.title('Histogram of Sepal Length')
# plt.show()

# sns.scatterplot(x='sepal_length', y='petal_length', hue='species', data=iris_dataset)
# plt.title('Scatter Plot: Sepal Length vs Petal Length')
# plt.show()

# Identifies and handles any missing values in the dataset (even if simulated by altering the dataset).

iris_dataset.loc[0, 'sepal_length'] = np.nan
print("\nDataset with a simulated missing value:")
print(iris_dataset.head())

iris_dataset['sepal_length'].fillna(iris_dataset['sepal_length'].mean(), inplace=True)
print("\nDataset after handling missing values:")
print(iris_dataset.head())


# Implements a simple classification model using logistic regression from Scikit-learn:

#   + Splits the dataset into training and testing sets.
#   Trains the model and evaluates it using accuracy.


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

X = iris_dataset.iloc[:, :-1]
y = iris_dataset['species']

#training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=100)
model.fit(X_train, y_train)

y_pred = model.predict(X_test) 
print("\nAccuracy:", accuracy_score(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))