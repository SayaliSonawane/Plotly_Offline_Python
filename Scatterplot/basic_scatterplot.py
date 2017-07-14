#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 12:00:27 2017

@author: Sayali Sonawane
"""
# Import packages
import pandas as pd
import plotly
from plotly.graph_objs import Scatter,Layout

# Read data
# Data Source: https://www.kaggle.com/deepmatrix/imdb-5000-movie-dataset
# Dataset Name: IMDB 5000 Movie Dataset
df = pd.read_csv('/Data Visualisation/Data/movie_metadata.csv')

# Define trace
# X-axis: Number of voted users.
# Y-axis: IMDB Score.
trace1 = Scatter(x= df['num_voted_users'], y=df['imdb_score'], mode = 'markers')

# Create chart 
# Output will be stored as a html file. 
# Whenever we will open output html file, one popup option will ask us about if want to save it in jpeg format. 
plotly.offline.plot({
                         "data": [trace1], 
                         # <b> and </b>: Bold title 
                         # <br> use this for line break.
                        "layout": Layout(title="<b>Number of Voted Users Vs IMDB Score</b>", 
                                                   xaxis= dict(
                                                        title= '<b>Number of Voted Users</b>',
                                                        zeroline= False,
                                                        gridcolor='rgb(183,183,183)',
                                                        showline=True
                                                    ),
                                                    yaxis=dict(
                                                        title= '<b>IMDB_score</b>',
                                                        gridcolor='rgb(183,183,183)',
                                                        zeroline=False,
                                                        showline=True
                                                    ))
                                  },filename='No_voted_users_vs_imdb_score.html',image='jpeg')  
