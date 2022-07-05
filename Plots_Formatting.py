# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 10:48:48 2022

@author: rzava
"""

import os
inputFile  = "visitData.csv"
path = 'C:\\Users\\rzava\\OneDrive\\Documents\\Work\\ER Bullshit'
## Establish Path
os.chdir(path)
import pandas as pd
from RoomEstimation_RHM import estimateRooms
import plotly.graph_objs as go
import numpy as np
import plotly.express as px
from datetime import datetime as dt

##############################################################################
################## STANDARD DATA READING/TRANSFORMATION ######################
##############################################################################
vDat = pd.read_csv(inputFile)

RHM = vDat[vDat['Department_Name'].str.contains("RHM")]
## DF of just infusions b/c different rooms
RHMinf = RHM[RHM['Visit_ID'] == 6965]
RHMnot = RHM[RHM['Visit_ID'] != 6965]
## DF of all in-person visits, not infusions
#  fjuu = RHM[RHM['Visit_Type'].str.contains('VIRTUAL')]
#  set(fjuu['Visit_ID'])
RHMels = RHM[~RHM['Visit_ID'].isin([6965, 7421, 7557, 7580, 21037, 21031, 21039])]
## DF of all virtual visits
RHMtel = RHM[RHM['Visit_ID'].isin([7421, 7557, 7580, 21037, 21031, 21039])]

infRooms = estimateRooms(data = RHMinf, dates = 'Date', times = 'Appointment_Length', hours = 8)
elsRooms = estimateRooms(data = RHMels, dates = 'Date', times = 'Appointment_Length', hours = 8)
telRooms = estimateRooms(data = RHMtel, dates = 'Date', times = 'Appointment_Length', hours = 8)
allRooms = estimateRooms(data = RHMnot, dates = 'Date', times = 'Appointment_Length', hours = 8)
##############################################################################
##############################################################################
##############################################################################

### NEXT STEPS
##  Put all dfs into one df with designations ('tele' 'in person' etc)
##  Interactive plot broken down by df
##  Add average rooom usage mark
##  Perhaps separate plot for infusion

infRooms = infRooms.assign(Breakdown = 'Infusion Visits')
elsRooms = elsRooms.assign(Breakdown = 'In Person Exam Visits')
telRooms = telRooms.assign(Breakdown = 'Tele-Exam Visits')
allRooms = allRooms.assign(Breakdown = 'All Exam Visits')

## DF of all exams
Exams = pd.concat([elsRooms, telRooms, allRooms])

## Loop turning strings into date values.  Could probably do this earlier in
#  ETL, but might fuck something up, so doing it now for display purposes
hold = []
for i in infRooms['Date']:
    hold.append(dt.strptime(i, '%m/%d/%Y'))
infRooms['Date'] = hold
## And then sorting so it's not fucky, and rounding decimals so rooms don't 
#  freak out business bois for having 4 decimals
infRooms = infRooms.sort_values(by = 'Date')
infRooms = infRooms.round(2)

## Loop turning strings into date values.  Could probably do this earlier in
#  ETL, but might fuck something up, so doing it now for display purposes
hold = []
for i in Exams['Date']:
    hold.append(dt.strptime(i, '%m/%d/%Y'))
Exams['Date'] = hold
## And then sorting so it's not fucky, and rounding decimals so rooms don't 
#  freak out business bois for having 4 decimals
Exams = Exams.sort_values(by = 'Date')
Exams = Exams.round(2)



###############################################################################
###########################      INFUSION PLOT      ###########################
###############################################################################
## Next step would be to create function, probably, for the template, but might
#  have so many variables it's easier to just do this.  Idk, we'll see

infRooms = infRooms.rename(columns = {'Rooms' : 'Chairs'})
## Plot object, changing hover date format
inFig = px.line(infRooms, x = "Date", y = "Chairs", hover_data={"Date":"|%B %d"},
                color = "Breakdown")
## Adding title, title location, blank background, titling axes, TNR font
inFig.update_layout(title = {'text': "Rheumatology Infusion Chairs Estimated Use", 
                             'x': .5, 'y':.95},
                             plot_bgcolor = "white",
                             yaxis_title = "Chairs Used",
                             font_family = "Times New Roman",
                             hovermode = 'x unified')
## Get Axes lines to show, format date
inFig.update_xaxes(showline = True, linewidth = 1, linecolor = 'black', 
                   dtick = "M1", tickformat = "%b \n%Y")
inFig.update_yaxes(showline = True, linewidth = 1, linecolor = 'black')
## Add rooms available
inFig.add_trace(go.Scatter(x = infRooms['Date'], 
                           y = np.repeat(7, len(infRooms['Date'])), 
                           line_dash="dash", 
                           line_color="yellow", 
                           #hover_data = "Chairs Available"
                           showlegend = True,
                           name = "Chairs Available")
                )
inFig.write_html("infusion.html")

###############################################################################
############################      EXAMS PLOT      #############################
###############################################################################

## Plot object, changing hover date format
exFig = px.line(Exams, x = "Date", y = "Rooms", hover_data={"Date":"|%B %d"},
                color = "Breakdown")
## Adding title, title location, blank background, titling axes, TNR font
exFig.update_layout(title = {'text': "Rheumatology Exam Rooms Estimated Use", 
                             'x': .5, 'y':.95},
                             plot_bgcolor = "white",
                             yaxis_title = "Rooms Used",
                             font_family = "Times New Roman",
                             hovermode = 'x unified')
## Get Axes lines to show, format date
exFig.update_xaxes(showline = True, linewidth = 1, linecolor = 'black', 
                   dtick = "M1", tickformat = "%b \n%Y")
exFig.update_yaxes(showline = True, linewidth = 1, linecolor = 'black')
## Add rooms available
exFig.add_trace(go.Scatter(x = Exams['Date'], 
                           y = np.repeat(10, len(hold)), 
                           line_dash="dash", 
                           line_color="yellow", 
                           #hover_data = "Chairs Available"
                           showlegend = True,
                           name = "Rooms Available")
                )
exFig.write_html("Rooms.html")
