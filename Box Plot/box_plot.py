#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 15:03:07 2017

@author: Sayali Sonawane
"""
# Import packages
import numpy as np
import plotly
from plotly.graph_objs import Layout,Box

# Create data 
y0 = np.random.randn(50)-1
y1 = np.random.randn(50)+1

# Define trace
trace1 =Box(y=y0,showlegend=True,name='Trace_y0')
trace2 =Box(y=y1,showlegend=True,name='Trace_y1')

# Create chart 
# Output will be stored as a html file. 
# Whenever we will open output html file, one popup option will ask us about if want to save it in jpeg format.
# Font family can be used in a layout to define font type, font size and font color for title           
plotly.offline.plot({
                         "data": [
                                  trace1,trace2
                                  ], 
                        "layout": Layout(title="Basic Box Chart",font=dict(family='Courier New, monospace', size=18, color='rgb(0,0,0)'))
                                  },filename='basic_box_chart.html',image='jpeg')

