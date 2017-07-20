#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 12:00:27 2017

@author: Sayali Sonawane
"""
# Import packages
import pandas as pd
import plotly
from plotly.graph_objs import Scatter,Layout

# Read data
# Dataset: Life Expectancy and per capita income (Rosling) 
df = pd.read_csv('/sayali/Desktop/Data Visualisation/Scatterplot/Multi_trace_scatterplot/rosling_full.csv')

# Define trace
# Create multiple  traces for each continent 
trace1 = Scatter(x= df['"Africa, x"'], y=df['"Africa, y"'],mode = 'markers',showlegend=True,name='Africa')
trace2 = Scatter(x= df['"Americas, x"'], y=df['"Americas, y"'],mode = 'markers',showlegend=True,name='America')
trace3 = Scatter(x= df['"Asia, x"'], y=df['"Asia, y"'],mode = 'markers',showlegend=True,name='Asia')
trace4 = Scatter(x= df['"Europe, x"'], y=df['"Europe, y"'],mode = 'markers',showlegend=True,name='Europe')
trace5 = Scatter(x= df['"Oceania, x"'], y=df['"Oceania, y"'],mode = 'markers',showlegend=True,name='Oceania')

# Create chart 
# Output will be stored as a html file. 
# Whenever we will open output html file, one popup option will ask us about if want to save it in jpeg format. 
# If you want basic bubble chart with only one continent just include that particular trace while providing input. 
# Example of basic bubble chart for only one continent
# "data":[trace1]
plotly.offline.plot({
                         "data": [trace1,trace2,trace3,trace4,trace5], 
                         # <b> and </b>: Bold title 
                         # <br> use this for line break.
                        "layout": Layout(title="<b> GDP Per Capita Vs Life Expectancy</b>", 
                                                   xaxis= dict(
                                                        title= '<b>GDP Per Capita</b>',
                                                        zeroline= False,
                                                        gridcolor='rgb(183,183,183)',
                                                        showline=True
                                                    ),
                                                    yaxis=dict(
                                                        title= '<b>Life Expectancy</b>',
                                                        gridcolor='rgb(183,183,183)',
                                                        zeroline=False,
                                                        showline=True
                                                    ))
                                  },filename='bubble_chart.html',image='jpeg')  
