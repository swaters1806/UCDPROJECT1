
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns


##Low memory used based on Pycharm prompt
df = pd.read_csv ('IMDb movies1.csv', low_memory=False, sep=',', dtype={"worlwide_gross_income": int})
dtype={"genre": str, "director": str, "production_company": str, "year": str, "imdb_title_id": str}
print (df)

##Subset to Noughties decade
df_2010_2020 = df.loc[(df["year"] > 2009) & (df["year"] <= 2020)]
print (df_2010_2020)

##Subset to areas for analysis - genres, producers, year,worldwide gross income

df_ucd_anal = df_2010_2020[['genre', 'director', 'production_company', 'year', 'imdb_title_id', 'worlwide_gross_income', 'title']]
print(df_ucd_anal.head)

##Check for missing data in df
print(df_ucd_anal.T.apply(lambda x: x.isnull().sum(), axis = 1))

##Handling missing value
df_ucd_anal.production_company.fillna("No production company provided", inplace=True)
df_ucd_anal.director.fillna("No director provided", inplace=True)

##Check for missing data after update
print(df_ucd_anal.T.apply(lambda x: x.isnull().sum(), axis = 1))

##Check that Worldwide income is a value that can be summed
print(df_ucd_anal["worlwide_gross_income"].dtypes)

##Sort data based on highest value
prd_valuecheck = df_ucd_anal[["production_company", "worlwide_gross_income"]]
print(prd_valuecheck.head())
prd_valuechecksrt = prd_valuecheck.sort_values("worlwide_gross_income", ascending=False)
print(prd_valuechecksrt.head())
prd_valuechecksrt['WWGross_income_millions'] = df['worlwide_gross_income']/1000000
print(prd_valuechecksrt.dtypes)


Top_5_prod_com = prd_valuechecksrt.iloc[0:5, 0:4]
print(Top_5_prod_com.head())

#1. Production Company by the Amount of the films release
filtered_prod = df_ucd_anal.set_index('title').production_company.str.split(', ', expand=True).stack().reset_index(level=1, drop=True);
filtered_prod = filtered_prod[filtered_prod != 'No production company provided']
plt.figure(figsize=(18,7))
g = sns.countplot(y = filtered_prod, order=filtered_prod.value_counts().index[:10])
plt.title('Top 10 Production Companies between 2010-2020')
plt.xlabel('Titles')
plt.ylabel('Production Company')
plt.show()

#2. Top Directors by film in decade
filtered_directors = df_ucd_anal[df_ucd_anal.director != 'No director provided'].set_index('title').director.str.split(', ', expand=True).stack().reset_index(level=1, drop=True)
plt.figure(figsize=(13,7))
plt.title('Top 10 Director Based on The Number of Titles')
sns.countplot(y = filtered_directors, order=filtered_directors.value_counts().index[:10], palette='Blues')
plt.xlabel('Releases')
plt.show()


#3. Number of releases per Calender year

trop_prod_by_yeardf = df_ucd_anal.groupby(["year"])["worlwide_gross_income"].count().reset_index()
print(trop_prod_by_yeardf.head())

prodcomp_byrevenue = df_ucd_anal.groupby(["year"])["worlwide_gross_income"].sum().reset_index()
print(prodcomp_byrevenue.head())

#3updated. Number of releases per Calender year & Revenue. Two lines on one graph
# create figure and axis objects with subplots()
fig,ax = plt.subplots()
ax.plot(prodcomp_byrevenue.year, prodcomp_byrevenue.worlwide_gross_income, color="red", marker="o")
# set x-axis label
ax.set_xlabel("year")
# set y-axis label
ax.set_ylabel("worlwide_gross_income(m)",color="red")
# twin object for two different y-axis on the sample plot
ax2=ax.twinx()
# make a plot with different y-axis using second axis object
ax2.plot(trop_prod_by_yeardf.year, trop_prod_by_yeardf.worlwide_gross_income,color="blue",marker="o")
ax2.set_ylabel("No. of release",color="blue")
ax2.set_title("Annual Revuenue & Output by Year")
plt.show()








