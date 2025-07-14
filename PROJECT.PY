import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

df = pd.read_csv('customer churn.csv')
# df.head()
# print(df.head())
# df.info()
# print(df.info())
# replacing blanks with 0 and no total charges are recorded
# df["TotalCharges"] = df["TotalCharges"].replace(" ","0")
# df["TotalCharges"] = df["TotalCharges"].astype("float")
# print(df)
# print(df.info())
# print(df.columns)
# df.isnull().sum().sum()
# print(df.isnull)
df.describe()
print(df.describe)