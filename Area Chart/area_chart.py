#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 15:03:07 2017

@author: Sayali Sonawane
"""
# Import packages
import plotly
from plotly.graph_objs import Layout,Scatter

# Define trace
# Pass data values in trace directly
# Using fill parameter we can choose the color of overlapping area
# possible value for fill: 'tonexty' or fill: 'tozeroy' 
trace1 =Scatter(x=[1, 2, 3, 4],y=[0, 2, 3, 5],showlegend=True,marker = dict(color = 'rgb(128, 0, 0)',),name='Trace_1',fill='tozeroy')
trace2 =Scatter(x=[1, 2, 3, 4],y=[3, 5, 1, 7],showlegend=True,marker = dict(color = 'rgb(0, 128, 0)',),name='Trace_2',fill='tonexty')

# Create chart 
# Output will be stored as a html file. 
# Whenever we will open output html file, one popup option will ask us about if want to save it in jpeg format.
# Font family can be used in a layout to define font type, font size and font color for title           
plotly.offline.plot({
                         "data": [
                                  trace1,trace2
                                  ], 
                        "layout": Layout(title="Area Chart",font=dict(family='Courier New, monospace', size=18, color='rgb(0,0,0)'))
                                  },filename='Area_chart.html',image='jpeg')
