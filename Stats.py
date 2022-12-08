# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 22:00:22 2022

@author: Huawei
"""

import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns
import numpy as np

def electric(filename):
    df=pd.read_csv(filename,skiprows=(4))
    a=df['Country Name']
    df=df.iloc[15:20,50:55]
    #print(df['Country Name']=="Belgium")
    print(df)
    df = df.fillna(0)
    print(df)
    df.insert(loc=0,column='Country Name',value=a)
    #df.apply(lambda col: pd.Series(col.unique()))
    #df.insert(loc=0,column='Year',value=b)
    df=df.dropna(axis=1)
    df=df.set_index('Country Name').T
    print(df)
    # a1=df['Country Name']
    # b1=df[['2006','2007','2008','2009','2010']]
    # print(a1)  
    return df 
a=electric("electricityconsumption.csv")
plt.figure(dpi=144)                   #resolution and clarity purpose of graph
a.plot(kind='line')
# a.plot(kind='line',a["2006"],a["Azerbaijan"],label="2006",dashes=[1,1])    #calling function to plot line
# a.plot(kind='line',a["2007"],a["Burundi"],label="2007",dashes=[1,1])  
# a.plot(kind='line',a["2008"],a["Belgium"],label="2008",dashes=[1,1])  
# a.plot(kind='line',a["2009"],a["Benin"],label="2009",dashes=[1,1])  
# a.plot(kind='line',a["2010"],a["Burkina Faso "],label="2010",dashes=[1,1])  
    #plt.plot(df, df["Female"],"Female","blue")
plt.xlabel("Countries")
plt.ylabel("Energy per Capita")
plt.title("Electric Consumption per Capita")
plt.legend(loc="best") 



def electric(filename):
    df=pd.read_csv(filename,skiprows=(4))
    a=df['Country Name']
    df=df.iloc[15:20,50:55]
    #print(df['Country Name']=="Belgium")
    print(df)
    df = df.fillna(0)
    print(df)
    df.insert(loc=0,column='Country Name',value=a)
    #df.apply(lambda col: pd.Series(col.unique()))
    #df.insert(loc=0,column='Year',value=b)
    df=df.dropna(axis=1)
    df=df.set_index('Country Name').T
    print(df)
    # a1=df['Country Name']
    # b1=df[['2006','2007','2008','2009','2010']]
    # print(a1)  
    return df 
a=electric("gdp.csv")
plt.figure(dpi=144)                   #resolution and clarity purpose of graph
a.plot(kind='line')
# a.plot(kind='line',a["2006"],a["Azerbaijan"],label="2006",dashes=[1,1])    #calling function to plot line
# a.plot(kind='line',a["2007"],a["Burundi"],label="2007",dashes=[1,1])  
# a.plot(kind='line',a["2008"],a["Belgium"],label="2008",dashes=[1,1])  
# a.plot(kind='line',a["2009"],a["Benin"],label="2009",dashes=[1,1])  
# a.plot(kind='line',a["2010"],a["Burkina Faso "],label="2010",dashes=[1,1])  
    #plt.plot(df, df["Female"],"Female","blue")
plt.xlabel("Countries")
plt.ylabel("GDP")
plt.title("GDP growth")
plt.legend(loc="best") 

# def co2(filename):
#      df=pd.read_csv(filename,skiprows=(4))
#      a=df['Country Name']
#      df=df.iloc[50:55,50:55]
#      #print(df['Country Name']=="Belgium")
#      print(df)
#      df = df.fillna(0)
#      print(df)
#      df.insert(loc=0,column='Country Name',value=a)
#      #df.apply(lambda col: pd.Series(col.unique()))
#      #df.insert(loc=0,column='Year',value=b)
#      df=df.dropna(axis=1)
#      df1=df.set_index('Country Name').T
#      print(df)
#      a1=df['Country Name']
#      b1=df[['2006','2007','2008','2009','2010']]
#      print(a1)
#      #x_axis = np.arange(len(a1))
#      plt.figure(dpi=144)                   #resolution and clarity purpose of graph
#      plt.bar(a1,b1["2006"],label="2006")    #calling function to plot line
#      plt.bar(a1,b1["2007"],bottom=b1["2007"],label="2007")  
#      plt.bar(a1,b1["2008"],bottom=b1["2008"],label="2008")  
#      plt.bar(a1,b1["2009"],bottom=b1["2009"],label="2009")  
#      plt.bar(a1,b1["2010"],bottom=b1["2010"],label="2010")
#      plt.xlabel("Countries")
#      plt.ylabel("Energy per Capita")
#      plt.title("CO2 Emissions")
#      plt.legend(loc="best")   
#      return df,df1 
# a,b=co2("co2.csv")
def co2(filename):
     df=pd.read_csv(filename,skiprows=(4))
     a=df['Country Name']
     df=df.iloc[15:20,55:60]
     #print(df['Country Name']=="Belgium")
     print(df)
     df = df.fillna(0)
     print(df)
     df.insert(loc=0,column='Country Name',value=a)
     #df.apply(lambda col: pd.Series(col.unique()))
     #df.insert(loc=0,column='Year',value=b)
     df=df.dropna(axis=1)
     df1=df.set_index('Country Name').T
     print(df)
     # a1=df['Country Name']
     # b1=df[['2011','2012','2013','2014','2015']]
     #print(a1)
     return df
a=co2("co2.csv")
plt.figure(figsize=(10,7),dpi=150) 
a.plot(kind='bar',x='Country Name')
plt.xlabel("Countries")
plt.ylabel("Energy per Capita")
plt.ylim()
plt.title("CO2 Emissions")
plt.legend(loc="best") 
plt.xticks()
plt.show()
