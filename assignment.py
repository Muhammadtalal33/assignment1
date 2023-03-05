#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 03:09:29 2023

@author: Talal
"""

import pandas as pd
import matplotlib.pyplot as plt



def bar_plot_dog_max_life(data):
    """
    Parameters
    ----------
    data : DataFrame
        parameter representing dogs data.
    This plot represents expected ages of dogs in years
    Returns
    -------P
    None.
    """
    graph = data[0:20].plot(kind='bar', figsize=(10, 6), width=0.8)
    graph.set_xlabel("Dog")
    graph.set_ylabel("Year")
    graph.set_title("Max Life Expectations")
    graph.legend()
    plt.show()
    

def pieplot_language_distributaion_in_movies(data, languages):
    """
    Parameters
    ----------
    data : DataFrame
    Returns
    -------
    None.
    """
    percentages = (data/ data.sum()) * 100
    percentages["Other Languages"] = percentages.sum() - (percentages.loc[languages].sum())
    languages.append("Other Languages")
    plt.pie(percentages.loc[languages], labels=percentages.loc[languages].index, 
            autopct='%1.1f%%', startangle=90)
    plt.title("Languages by Percentage in different movies")
    plt.axis('equal')
    
    plt.show()
    

def line_graph_punjab(rain_data, title):
    """
    Parameters
    ----------
    data : DataFrame
        Rainfall data for Punjab India.
    title : String
        Title for the plot.
    Returns
    -------
    None.

    """
    plt.plot(rain_data['YEAR'], rain_data['JUN-SEP'])
    plt.title(title)
    plt.xlabel('Year')
    plt.ylabel("Rainfall from JUN to SEPT")
    plt.show()
    
    

# Dogs data file
data1 = pd.read_csv('dogbreeds2.csv')

data1.set_index('Name', inplace=True)
life_expectations = data1['max_life_expectancy']
bar_plot_dog_max_life(life_expectations)

# Movies Database
data2 = pd.read_csv('moviestmdb10000.csv')

counts = data2['original_language'].value_counts()
pieplot_language_distributaion_in_movies(counts, ['en', 'fr', 'it'])



# India Rain Fall Dataset
data3 = pd.read_csv('rainfaLLIndia.csv')
print(data3.info())
punjab_rainfall = data3[data3['subdivision'] == 'PUNJAB']
punjab_rainfall = punjab_rainfall.drop_duplicates(subset=['YEAR'])

line_graph_punjab(punjab_rainfall, "Rainfall in PUNJAB")























