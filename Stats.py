# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 22:00:22 2022

@author: Huawei
"""

import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns
# import numpy as np

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
    df1=df.set_index('Country Name').T
    print(df)
    a1=df['Country Name']
    b1=df[['2006','2007','2008','2009','2010']]
    print(a1)
    plt.figure(figsize=(20,10),dpi=144)                   #resolution and clarity purpose of graph
    plt.plot(a1,b1["2006"],label="2006")    #calling function to plot line
    plt.plot(a1,b1["2007"],label="2007")  
    plt.plot(a1,b1["2008"],label="2008")  
    plt.plot(a1,b1["2009"],label="2009")  
    plt.plot(a1,b1["2010"],label="2010")  
    #plt.plot(df, df["Female"],"Female","blue")
    plt.xlabel("Countries")
    plt.ylabel("Energy per Capita")
    plt.title("Electric Consumption per Capita")
    plt.legend(loc="best")   
    return df,df1 


# def pie(values, labels, title=""):
#     plt.pie(values,labels=labels)
#     plt.title(title)
#     return

a,b=electric("electricityconsumption.csv")

#print(df1)
# df1=file
# #extract countries of interest
# df1= df1[(df1["Country Name"] == "United States")
#                     | (df1["Country Name"] == "Ireland")
#                     | (df1["Country Name"] == "Russian Federation")
#                     | (df1["Country Name"] == "India")
#                     | (df1["Country Name"] == "China")
#                     | (df1["Country Name"] == "South Africa")]

# #plt.subplot(2,1,1)
# pie(df1["2005"], labels=df1["Country Name"], title="Electric Power Consumption(kWh per Capita)in the year 2005")



#def stacked_barplot(df, x, columns, xlabel, ylabel, title, file):
    
#     plt.figure(figsize=144)
    
#     # start with first column
#     plt.bar(x, df_electricity[columns[0]], width=10.0, label=columns[0])

#     # loop over remaining columns
#     for i in range(1, len(columns)):
#         plt.bar(x, df_electricity[columns[i]], bottom=df_electricity[columns[i-1]], width=10.0, 
#                 label=columns[i])
        

#     plt.title(title)
#     plt.xlabel(xlabel)
#     plt.ylabel(ylabel)
#     plt.legend()    

#     plt.savefig(file)
#     plt.show()

# stacked_barplot(df_electricity, df_2014["2014"],df_2014["Country Name"],"year",
#                 "Country", "Electric Consumption", "pop.png")

# columns= df2[(df2["2005"] =="2005")
#                     | (df2["2006"] == "2006")
#                     | (df2["2007"] == "2007")
#                     | (df2["2010"] == "2010")
#                     | (df2["2014"] == "2014")]
#(columns)
# #columns =df1['2005', '2006', '2007', '2010', '2014']
# plt.figure(dpi=144)
# plt.bar(df1[df1[columns[0]],"Country Name"]=="Ireland",width=10.0, label=columns[0])
# # if optional argument bottom is used, the bars of height are plotted
# # from the value of bottom
# #plt.bar(df1["2006"],df1["Country Name"]=="Ireland",bottom=df1["Country Name"]=="Ireland",width=1.0,label="Ireland")
# #general matters
# plt.title("Electric Consumption")
# plt.xlabel("Years")
# plt.ylabel("Countries")
# plt.legend()
# plt.show()

# def stacked_barplot(df, x, columns, xlabel, ylabel, title):
#     """
#     Produces a bar plot with dat from more than one column stacked on each 
#     other. 
#     df: name of the dataframe
#     x: 1D array or dataseries with the x-values
#     columns: names of the columns in df to be plotted. Also used for the 
#             legend.
#     xlabel, ylabels: labels for x and y axis.
#     title: title for the plot
#     file: file name to store the plot as png file
#     """
    
#     plt.figure()
    
#     # start with first column
#     plt.bar(x, df2[columns[0]], width=10.0, label=columns[0])

#     # loop over remaining columns
#     for i in range(1, len(columns)):
#         plt.bar(x, df2[columns[i]], bottom=df2[columns[i-1]], width=10.0, 
#                 label=columns[i])
        

#     plt.title(title)
#     plt.xlabel(xlabel)
#     plt.ylabel(ylabel)
#     plt.legend()    

#     #plt.savefig(file)
#     plt.show()



# stacked_barplot(df2, df2["2005"], ["China", "Ireland","India"], "year",
#                 "population (millions)", "Population of London")


