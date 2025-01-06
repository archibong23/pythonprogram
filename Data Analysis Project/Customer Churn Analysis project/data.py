import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Load Data
data = pd.read_csv("raw_data.csv")
# print(data.head())
# print(data.info())

#Convert Totalcharges to numeric, coerce errors to NaN
data['TotalCharges'] = pd.to_numeric(data['TotalCharges'], errors='coerce')

#Check for missing values in Totalcharges
print(data['TotalCharges'].isnull().sum())

#Fill missing values or drop rows with missing TotalCharges
data['TotalCharges'].fillna(data['TotalCharges'].median(), inplace=True)

#Drop Irrelevant columns
data.drop(columns=['customerID'], inplace=True)

#Encode Target variable
data['churn'] = data['churn'].map({'Yes': 1, 'No': 0})

#explore missing values
print(data.isnull().sum())