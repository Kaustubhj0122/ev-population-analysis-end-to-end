import numpy as np
import pandas as pd
import random

# 1. load data from excel and its key columns:-
ev=pd.read_csv(r"G:\Data Science\project\Data Analysis end to end prj\EV_Population_Analysis\Electric_Vehicle_Population_Data.csv")
ev.columns

# 2. head 
ev.head(5)

# 3. Abount max, min, mean, count of each one using describe method.
ev.describe()

# 4. About each Field Data type, count and null/not null
ev.info()
ev.shape # to get total number of rows and columns.


# 5. Total count of the missing values from whole dataframe 
ev.isnull().sum()


# 6. Models unique values to fill prize accordig to that one:-
ev['Model'].unique()


# 7. Filling Missing Numerical Values:--
m_list=ev['Model'].unique()

i=25600
j=28400
for m in m_list:
    ev.loc[(ev['Model']== str(m).strip()) & (ev['Base MSRP'].isna() | ev['Base MSRP']==0),'Base MSRP']=np.random.randint(i,j)
    i=i+4030
    j=j+5100



# 8. finding  Vehicle IDC
ev['Electric Range'].fillna(ev['Electric Range'].median(), inplace=True)
ev.loc[ev['Electric Range'] == 0, 'Electric Range'] = np.random.randint(10, 50, size=(ev['Electric Range'] == 0).sum())


# 9. Fill missing categorical data (found on ev.isnull().sum() info from data cleaning part)
ev['County'].fillna('Indus', inplace=True)
ev['City'].fillna('Texas', inplace=True)
ev['Electric Utility'].fillna('Not Specified', inplace=True)


# 10. Fill Number in between 0-49 for Legislative District:-
l=ev['Legislative District'].isna()
ev.loc[l,'Legislative District']=np.random.randint(0,50,size=l.sum())

# 11. Strip whitespaces from the column names
ev.columns = ev.columns.str.strip()

# 12. Standardize/rename column names
ev.rename(columns={'Clean Alternative Fuel Vehicle (CAFV) Eligibility': 'CAFV_Eligibility'}, inplace=True)

# 13.  Create derived features
ev['Vehicle_Age (years)'] = (2025 - ev['Model Year']) # (2025 - ev['Model Year']).astype(str) + ' years'

# 14. create new column regarding battery cpty
battery_cpty={1:"Less than 60 kWh", 2:'In Between 60-80 kWh', 3:'In Between 80-100 kWh', 4:'More than 100 kwh'}
ev['Battery Capacity']=[np.random.randint(1,4) for _ in range(150482) ]

# 15.  use the map method to assign values for the respective  battery types via code.
ev['Battery Capacity']=ev['Battery Capacity'].map(battery_cpty)


# 16. check the column names
ev.columns
ev.head(10)


## EDA Part:- 

import matplotlib.pyplot as plt
import seaborn as sns

# 1. Top 10 Manufacturers
top_makes = ev['Make'].value_counts().head(10)
sns.barplot(x=top_makes.index, y=top_makes.values)
plt.title("Top 10 Electric Vehicle Manufacturers")
plt.xticks(rotation=45)
plt.show()

# 2. GroupBy to find mean price of each make
base_mrp = ev.groupby('Make')['Base MSRP'].mean().sort_values(ascending=False)
print(base_mrp)

# Plot
plt.figure(figsize=(20, 6))
sns.barplot(x=base_mrp.index, y=base_mrp.values, palette='viridis')

plt.title("Average Base MSRP of Each EV Make", fontsize=14, weight='bold')
plt.xlabel("Make", fontsize=12)
plt.ylabel("Average Base MSRP ($)", fontsize=12)
plt.xticks(rotation=45)

plt.show()


# 3. EV Adoption by Model Year
plt.figure(figsize=(10,5))
sns.countplot(x='Model Year', data=ev, order=sorted(ev['Model Year'].unique()),palette='plasma')
plt.title("EV Registrations by Model Year")
plt.show()


# 4 Distribution of Electric Range
sns.histplot(ev['Electric Range'], bins=20,kde=True)
plt.title("Distribution of Electric Range")
plt.xlabel("Range (miles)")
plt.show()


# 5 CAFV Eligibility Breakdown
sns.countplot(x='CAFV_Eligibility', data=ev)
plt.title("CAFV Eligibility Distribution")
plt.xticks(rotation=30)
plt.show()

# 6 Geographic Insights: Top Counties
top_counties = ev['County'].value_counts().head(10)
sns.barplot(y=top_counties.index, x=top_counties.values, color="#00C4C4")
plt.xlabel("Number of Electric Vehicles")
plt.ylabel("County")
plt.tight_layout()
plt.title("Top 10 Counties with Most EVs")
plt.show()


# 7 heatmap:--
# Select relevant numeric columns
num_cols = ['Model Year', 'Electric Range', 'Base MSRP', 
            'Legislative District', '2020 Census Tract','Vehicle_Age (years)']

# Compute correlation
corr = ev[num_cols].corr()

plt.figure(figsize=(8,6))
sns.heatmap(
    corr,
    annot=True,          # display correlation values
    fmt=".2f",           # limit to 2 decimal places
    cmap="viridis",       # color palette  Recommended :- [crest,viridis,coolwarm ]
    linewidths=0.5,      # space between cells
    cbar_kws={'label': 'Correlation Coefficient'}  # color bar label
)
plt.title("Correlation Heatmap of EV Numeric Features", fontsize=14, fontweight='bold', pad=15)
plt.tight_layout()
plt.show()


# SQL Connection part:-
# mysql_integration.py
import mysql.connector
from sqlalchemy import create_engine
import pymysql



engine = create_engine("mysql+pymysql://root:Kaustubh%409860@localhost:3306/ev_population_db")


ev.to_sql(name='ev_population', con=engine, if_exists='replace', index=False)
print("Data successfully uploaded to MySQL!")
