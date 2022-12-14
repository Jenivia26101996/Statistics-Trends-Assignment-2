# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 22:00:22 2022

@author: Huawei
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
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

"""correlation plot for heatmap"""
def corr_plot(file):
    df_stats = pd.read_csv(file,skiprows=(4))
    a=df_stats['Indicator Name']
    df_stats=df_stats.iloc[[4181,4182,4183,4184,4214],[55,56,58,59,60]]
    df_stats = df_stats.fillna(0)
    df_stats.insert(loc=0,column='Indicator Name',value=a)
    df_stats=df_stats.dropna(axis=1)
    df_stats=df_stats.set_index('Indicator Name').T
    b=df_stats.corr()
    print(b)
    months = df_stats.index.values
    years =  df_stats.columns.values

    fig, ax = plt.subplots(figsize=(10,10))
    im = ax.imshow(b,cmap='coolwarm')
    #cbar = ax.figure.colorbar(im, ax = ax,shrink=0.5 )
    fig.tight_layout()
    ax.set_xticks(np.arange(len(months)), 
              labels=months)
    ax.set_yticks(np.arange(len(years)), 
              labels=years)
    plt.setp(ax.get_xticklabels(),
         rotation = 45,
         ha = "right",
         rotation_mode = "anchor")
    ax.set_title("Germany", 
             size=20)
    valfmt="{x:.2f}"
    textcolors=("black", "black")
    threshold=None
    if not isinstance(b, (list, np.ndarray)):
        b = im.get_array()

    # Normalize the threshold to the images color range.
    if threshold is not None:
        threshold = im.norm(threshold)
    else:
        threshold = im.norm(b.max())/2.

    # Set default alignment to center, but allow it to be
    # overwritten by textkw.
    kw = dict(horizontalalignment="center",
              verticalalignment="center")
    #kw.update(textkw)
    if isinstance(valfmt, str):
        valfmt = mpl.ticker.StrMethodFormatter(valfmt)

    # Loop over the data and create a `Text` for each "pixel".
    # Change the text's color depending on the data.
    texts = []
    for i in range(b.shape[0]):
        for j in range(b.shape[1]):
            kw.update(color=textcolors[int(im.norm(b[i, j]) > threshold)])
            text = im.axes.text(j, i, valfmt(b[i, j], None), **kw)
            texts.append(text)
    fig.tight_layout()
    plt.savefig("Heatmap_in_matplotlib.png",format='png',dpi=150)
    return
corr_plot("API_19_DS2_en_csv_v2_4700503.csv")