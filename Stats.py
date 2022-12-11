# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 22:00:22 2022

@author: Huawei
"""
import pandas as pd
import matplotlib.pyplot as plt

"""
Created a function electric to manipulate the data using pandas dataframes which takes a csv file as argument, 
reads a dataframe in Worldbank format which is electric consumption and returns two dataframes: 
one with years as columns and one with countries as columns.
iloc:for selective columns in dataframe
fillna(0):will replace Nan values with 0
Transposed(T): is used to return transposed columns
kind='line': line plot function in pandas
bbox_to_anchor: to place leegend outside the box
label:display labels
savefig:saves image in the directory
linestyle: we can display different types of line
"""

def electric(filename):
    df_electric=pd.read_csv(filename,skiprows=(4))
    df_country=df_electric['Country Name']
    df_electric=df_electric.iloc[[10,20,40,50,60],[54,55,56,57,58]]
    df_electric = df_electric.fillna(0)
    print(df_electric)
    df_electric.insert(loc=0,column='Country Name',value=df_country)
    df_electric=df_electric.dropna(axis=1)
    df_electrict=df_electric.set_index('Country Name').T
    #print(df)
    return df_electric,df_electrict 
a,b=electric("electricityconsumption.csv")
print(a.describe())
plt.figure(figsize=(8,10),dpi=150)                   
b.plot(kind='line',linestyle='-.')
plt.xlabel("Years")
plt.ylabel("Energy per Capita")
plt.title("Electric power consumption (kWh per capita)")
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5)) 
plt.savefig("Electric.png",bbox_inches="tight")
plt.show()

"""
Created a function gdp to manipulate the data using pandas dataframes which takes a csv file as argument, 
reads a dataframe in Worldbank format which is GDP growth (annual %) and returns two dataframes: 
one with years as columns and one with countries as columns.
iloc:for selective columns in dataframe
fillna(0):will replace Nan values with 0
Transposed(T): is used to return transposed columns
kind='line': line plot function in pandas
bbox_to_anchor: to place leegend outside the box
label:display labels
savefig:saves image in the directory
linestyle: we can display different types of line
"""

def gdp(filename):
    df_gdp=pd.read_csv(filename,skiprows=(4))
    a=df_gdp['Country Name']
    df_gdp=df_gdp.iloc[[10,20,40,50,60],[54,55,56,57,58]]
    print(df_gdp)
    df_gdp = df_gdp.fillna(0)
    df_gdp.insert(loc=0,column='Country Name',value=a)
    df_gdp=df_gdp.dropna(axis=1)
    df_gdpt=df_gdp.set_index('Country Name').T
    return df_gdp,df_gdpt 
a,b=gdp("gdp.csv")
print(a.describe())
plt.figure(figsize=(8,10),dpi=150)                  
b.plot(kind='line',linestyle='-.')
plt.xlabel("Years")
plt.ylabel("GDP Growth")
plt.title("GDP growth (annual %)")
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5)) 
plt.savefig("GDP.png",bbox_inches="tight")
plt.show()

"""
Created a function greenhouse to manipulate the data using pandas dataframes which takes a csv file as argument, 
reads a dataframe in Worldbank format which is Green house Gas Emissions and returns two dataframes: 
one with years as columns and one with countries as columns.
iloc:for selective columns in dataframe
fillna(0):will replace Nan values with 0
Transposed(T): is used to return transposed columns
kind='bar': bar plot function in pandas
bbox_to_anchor: to place leegend outside the box
label:display labels
savefig:saves image in the directory
linestyle: we can display different types of line
"""

def greenhouse(filename):
     df_greenhouse=pd.read_csv(filename,skiprows=(4))
     a=df_greenhouse['Country Name']
     df_greenhouse=df_greenhouse.iloc[[55,40,45,70,188],[35,45,55,59,60]]
     print(df_greenhouse)
     df_greenhouse = df_greenhouse.fillna(0)
     print(df_greenhouse)
     df_greenhouse.insert(loc=0,column='Country Name',value=a)
     df_greenhouse=df_greenhouse.dropna(axis=1)
     df_greenhouset=df_greenhouse.set_index('Country Name').T
     return df_greenhouse,df_greenhouset
a,b=greenhouse("greenhouse.csv")
print(a.describe())
plt.figure(figsize=(10,7),dpi=150) 
a.plot(kind='bar',x='Country Name')
font = {'family':'serif','color':'darkred','size':10}
plt.xlabel("Countries",fontdict=(font))
plt.ylabel("Green house Gas Emissions",fontdict=(font))
plt.ylim()
plt.xticks(rotation=45)
plt.title("Total greenhouse gas emissions")
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5)) 
plt.savefig("greenhouse.png",bbox_inches="tight")
plt.show()

"""
Created a function forest to manipulate the data using pandas dataframes which takes a csv file as argument, 
reads a dataframe in Worldbank format which is Forest area (% of land area) and returns two dataframes: 
one with years as columns and one with countries as columns.
iloc:for selective columns in dataframe
fillna(0):will replace Nan values with 0
Transposed(T): is used to return transposed columns
kind='bar': bar plot function in pandas
bbox_to_anchor: to place leegend outside the box
label:display labels
savefig:saves image in the directory
linestyle: we can display different types of line
"""
def forest(filename):
     df_forest=pd.read_csv(filename,skiprows=(4))
     a=df_forest['Country Name']
     df_forest=df_forest.iloc[[55,40,45,70,188],[35,45,55,59,60]]
     print(df_forest)
     df_forest = df_forest.fillna(0)
     print(df_forest)
     df_forest.insert(loc=0,column='Country Name',value=a)
     df_forest=df_forest.dropna(axis=1)
     df_forestt=df_forest.set_index('Country Name').T
     print(df_forest)
     return df_forest,df_forestt
a,b=forest("forest.csv")
print(a.describe())
plt.figure(figsize=(10,7),dpi=150) 
a.plot(kind='bar',x='Country Name')
font = {'family':'serif','color':'darkred','size':10}
plt.xlabel("Countries",fontdict=(font))
plt.ylabel("Forest area (% of land area)",fontdict=(font))
plt.ylim()
plt.xticks(rotation=45)
plt.title("Forest Area")
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5)) 
plt.savefig("forest.png",bbox_inches="tight")
plt.show()