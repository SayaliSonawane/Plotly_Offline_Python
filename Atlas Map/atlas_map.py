#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 14:43:14 2017

@author: Sayali Sonawane
"""
# Import packages
import plotly
import pandas as pd

# Import data
# Dataset: Starbucks Locations in USA
# Data Source: https://gist.github.com/dankohn/09e5446feb4a8faea24f
df = pd.read_csv('sayali/Desktop/Data Visualisation/Satellite map/starbucks_us_locations.csv')
df.columns = ['Longitude','Latitude','ADR_Line_1','ADR_Line_2']
 
# Atlas Map: Scattergeo type 
data = [ dict(
    type = 'scattergeo',
    lat = df['Latitude'],
    lon = df['Longitude'],
    text = df['ADR_Line_2'],
    mode = 'markers',
    marker = dict(color = 'rgb(128, 0, 0)'),
    )]

# In layout you can set scope to USA and projetions to 'albers usa', this will only display USA map.               
layout = dict(
    title = "STARBUCKS LOCATIONS IN USA",
    # Font type,size and color for title
    font=dict(family='Courier New, monospace', size=18, color='rgb(0,0,0)'),
    geo = dict(
        scope = 'usa',
        projection=dict(type='albers usa'),
        showframe = False,
        #showcoastlines = True,
        showland = True,
        showcountries = True,
        #landcolor = 'rgb(12,12,12)',
        subunitcolor = 'rgb(0,0,0)',
        countrycolor = 'rgb(0,0,0)',
        coastlinecolor = "rgb(0, 0, 0)",
        countrywidth = 2,
        #oceancolor = 'rgb(0, 119, 190)',
        coastlinewidth=4,
        subunitwidth = 0.5
        )
    )

plotly.offline.plot({"data":data, "layout":layout},filename = 'starbucks_stores_usa_atlas_map.html')
