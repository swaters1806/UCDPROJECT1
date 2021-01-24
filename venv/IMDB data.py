
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv ('IMDb movies.csv1', low_memory=False)
print (df)

##Subset to Noughties decade
df_2010_2020 = df.loc[(df['date_published'] > '2009') & (df['date_published'] <= '2020')]
df_2010_2020 = df_2010_2020[df_2010_2020['worlwide_gross_income'].notna()]
df_2010_2020[df_2010_2020.worlwide_gross_income.str.startswith('$ ')]
print (df_2010_2020)

df_genres_income = df_2010_2020[["genre", "worlwide_gross_income"]]
print(df_genres_income.shape()

check_for_nan = df_genres_income['worlwide_gross_income'].isnull().values.any()
print(check_for_nan)

##Review records with Worldwide gross income only & drop
##print(df_2010_2020['worlwide_gross_income'].isnull())
##df_2010_2020 = df_2010_2020[df_2010_2020['worlwide_gross_income'].notna()]
##print(df_2010_2020)

##Sum the values of each genre
##print(df_2010_2020['worlwide_gross_income'].dtypes)

##df_2010_2020_USDREV =df_2010_2020[df_2010_2020.worlwide_gross_income.str.startswith('$ ')]
##print(df_2010_2020_USDREV)
##print(df_2010_2020_USDREV['worlwide_gross_income'].dtypes)

##df_top5genres = df_2010_2020.groupby('genre').agg(['sum'])
##df_top5genres.sort_values(by='genre', ascending=False)
##print(df_top5genres.head(5))


df_top5producers = df_ucd_anal.groupby(['production_company','worlwide_gross_income']).sum()
print(df_top5producers)
df_top5producers.sort_values(by='worlwide_gross_income', ascending=True)
print(df_top5producers.head(5))








