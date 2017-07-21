#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 15:03:07 2017

@author: Sayali Sonawane
"""
# Import packages
import plotly
import numpy as np
from plotly.graph_objs import Layout,Scatter

#Create data
N = 500
random_x = np.linspace(0, 1, N)
random_y = np.random.randn(N)

# Define trace
trace =Scatter(x = random_x,y=random_y,marker = dict(color = 'rgb(128, 0, 0)',))

# Create chart 
# Output will be stored as a html file. 
# Whenever we will open output html file, one popup option will ask us about if want to save it in jpeg format.
# Font family can be used in a layout to define font type, font size and font color for title           
plotly.offline.plot({
                         "data": [
                                  trace
                                  ], 
                        "layout": Layout(title="Line Chart",font=dict(family='Courier New, monospace', size=18, color='rgb(0,0,0)'))
                                  },filename='Line_chart.html',image='jpeg')
