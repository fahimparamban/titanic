import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set(style="whitegrid")  # nice style for plots
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")  # only for later comparison if needed

train.head()
# Shape of dataset
print("Train shape:", train.shape)

# Info about datatypes and missing values
train.info()

# Summary statistics for numeric columns
train.describe()

# Value counts for categorical columns
print(train['Survived'].value_counts())
train.isnull().sum()
# Fill Age with median
train['Age'] = train['Age'].fillna(train['Age'].median())

# Fill Embarked with mode
train['Embarked'] = train['Embarked'].fillna(train['Embarked'].mode()[0])

# Drop Cabin (too many missing)
train.drop(columns=['Cabin'], inplace=True)
plt.figure(figsize=(8,5))
sns.histplot(train['Age'], bins=30, kde=True)
plt.title('Age Distribution')
plt.show()
sns.countplot(data=train, x='Survived')
plt.title('Survival Count')
plt.show()
sns.countplot(data=train, x='Sex', hue='Survived')
plt.title('Survival by Sex')
plt.show()
import matplotlib.pyplot as plt

# Select only numeric columns
numeric_train = train.select_dtypes(include=['int64', 'float64'])

# Create heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(numeric_train.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap - Titanic Dataset")
plt.show()
