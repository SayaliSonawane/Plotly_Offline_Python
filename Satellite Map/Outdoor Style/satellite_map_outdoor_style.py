#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 14:43:14 2017

@author: Sayali Sonawane
"""
# Import packages 
import plotly
import pandas as pd
from plotly.graph_objs import Scattermapbox,Data,Layout

# Read data
# Dataset: Starbucks Locations in USA
# Data Source: https://gist.github.com/dankohn/09e5446feb4a8faea24f
df = pd.read_csv('/home/local/ALGOANALYTICS/sayali/Desktop/Data Visualisation/Satellite map/starbucks_us_locations.csv')
df.columns = ['Longitude','Latitude','ADR_Line_1','ADR_Line_2']

# Open mapbox account and pass your access token over here
# Mapbox account sign up and access token is free. 
# Mapbox information: https://www.mapbox.com/help/how-access-tokens-work/#rotating-tokens
mapbox_access_token = 'Enter_your_access_token'
                           
data = Data([Scattermapbox(
        lat= df['Latitude'],
        lon= df['Longitude'],
        #color = df['MAPE_scaled'],
        text = [str(n) for n in df['ADR_Line_2']],
        mode='markers',
        marker = dict(color = 'rgb(0, 128, 0)',size=10),  
        hoverinfo='skip'
    ) ])    
                      

    
layout = Layout(
    title = "STARBUCKS LOCATIONS IN USA",
    font=dict(family='Courier New, monospace', size=18, color='rgb(0,0,0)'),
    autosize=False,
    hovermode='closest',
    showlegend=False,
    width=1800,
    height=1000,
    mapbox=dict(
        accesstoken=mapbox_access_token,
        #width=1415,
        bearing=0,
        center=dict(
            lat=38,
            lon=-94
        ),
        pitch=0,
        zoom=4,
        style = 'outdoors'
    ),
)                    

plotly.offline.plot({"data":data, "layout":layout},filename = 'starbucks_stores_usa_Satellite_map_outdoors_style.html')
