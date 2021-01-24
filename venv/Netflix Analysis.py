
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv ('Netflix_data.csv')
print (df)

##Subset to user only applicable data
uk_i_df = df[(df["country"] == "United Kingdom")]

print(uk_i_df.shape)


##Data with missing value
print(uk_i_df.T.apply(lambda x: x.isnull().sum(), axis = 1))

##Handling missing value
df.director.fillna("No Director Listed", inplace=True)
df.cast.fillna("No none Cast", inplace=True)
df.country.fillna("Country not provided", inplace=True)
df.dropna(subset=["date_added", "rating"], inplace=True)

##Check Missing values are resolved
print(df.T.apply(lambda x: x.isnull().sum(), axis = 1))





