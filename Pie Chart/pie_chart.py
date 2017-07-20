#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 15:03:07 2017

@author: Sayali Sonawane
"""
# Import packages
import pandas as pd
import plotly
from plotly.graph_objs import Layout,Pie

# Read data
# Dataset Link: https://www.kaggle.com/c/walmart-recruiting-store-sales-forecasting/data
# Dataset: Kaggle Walmart Sales Forecasting
stores = pd.read_csv('/sayali/Downloads/Walmart sales forecasting/Data/stores.csv')

# Calculating type distribution for all stores
types = stores['Type'].value_counts()
labels=types.index
values=types

# Define trace
# Set colors for partitions inside pie chart by assigning value to colors
# Font family is used to change font name,size and color of text inside pie chart.
trace=Pie(labels=labels,values=values,marker=dict(colors=["rgb( 255, 182, 193)","rgb(132,112,255)","rgb(0,171,169)"]),insidetextfont=dict(family='Courier New, monospace', size=18, color='rgb(0,0,0)'))

# Create chart 
# Output will be stored as a html file. 
# Whenever we will open output html file, one popup option will ask us about if want to save it in jpeg format.
# Font family can be used in a layout to define font type, font size and font color for title           
plotly.offline.plot({
                         "data": [
                                  trace
                                  ], 
                        "layout": Layout(title="Store Type Distribution",font=dict(family='Courier New, monospace', size=18, color='rgb(0,0,0)'))
                                  },filename='Store_Type.html',image='jpeg')



