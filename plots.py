#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 22 11:18:42 2021

@author: Tina
"""

import pandas as pd
import matplotlib.pyplot as plt
a1 = pd.read_csv(('../Resources/cities.csv'))

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8, 6))
ax.scatter(a1['Lat'], a1['Max Temp'])
ax.set_facecolor('cyan')
ax.set_xlabel('Latitude')
ax.set_ylabel('Max Temperature (F)')
ax.set_title('City Latitude vs. Max Temperature')
plt.grid(True, color='w')
plt.savefig(('./assets/image/temperature.png'))

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8, 6))
ax.scatter(a1['Lat'], a1['Humidity'])
ax.set_facecolor('cyan')
ax.set_xlabel('Latitude')
ax.set_ylabel('Humidity (%)')
ax.set_title('City Latitude vs.Humidity')
plt.grid(True, color='w')
plt.savefig(('./assets/image/humidity.png'))

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8, 6))
ax.scatter(a1['Lat'], a1['Cloudiness'])
ax.set_facecolor('cyan')
ax.set_xlabel('Latitude')
ax.set_ylabel('Cloudiness (%)')
ax.set_title('City Latitude vs. Cloudiness')
plt.grid(True, color='w')
plt.savefig(('./assets/image/cloudiness.png'))

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8, 6))
ax.scatter(a1['Lat'], a1['Wind Speed'])
ax.set_facecolor('cyan')
ax.set_xlabel('Latitude')
ax.set_ylabel('Wind Speed (mph)')
ax.set_title('City Latitude vs. Wind Speed')
plt.grid(True, color='w')
plt.savefig(('./assets/image/windspeed.png'))

a2 = a1.to_html()
with open('./assets/image/data_html.txt', 'w') as file:
    file.write(a2)
