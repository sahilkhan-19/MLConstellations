import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('DataVerse/Churn_Modelling.csv')
df.info()
print(df.isnull().sum())

updated_df = df
updated_df['Age'] = updated_df['Age'].fillna(df['Age'].mean())
updated_df['CreditScore'] = updated_df['CreditScore'].fillna(df['CreditScore'].mean())
df.info()
print(df.isnull().sum())