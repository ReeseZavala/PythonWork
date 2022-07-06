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

##############################################################################
###########     GENERATE WEEKDAYS FUNCTION     ###############################
##############################################################################
def getWeekdays(data, dateVar):
    weekDays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 
            'Friday', 'Saturday', 'Sunday']
    dayzNdayz = []
    hold = []
    for i in data[dateVar]:
        date = dt.strptime(i, '%m/%d/%Y')
        hold.append(date)
        dayzNdayz.append(weekDays[date.weekday()])
    data[dateVar] = hold
    data['Weekday'] = dayzNdayz
    ## And then sorting so it's not fucky, and rounding decimals so rooms don't 
    #  freak out business bois for having 4 decimals
    data = data.sort_values(by = dateVar)
    return(data)
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

infRooms = getWeekdays(infRooms, 'Date')
allRooms = getWeekdays(allRooms, 'Date')
Exams    = getWeekdays(Exams, 'Date')
###############################################################################
###########################      INFUSION PLOT      ###########################
###############################################################################
## Next step would be to create function, probably, for the template, but might
#  have so many variables it's easier to just do this.  Idk, we'll see

infRooms = infRooms.rename(columns = {'Rooms' : 'Chairs'})
## Plot object, changing hover date format
inFig = px.bar(infRooms, x = "Date", y = "Chairs", hover_data={"Date":"|%B %d"},
                color = "Weekday")
## Adding title, title location, blank background, titling axes, TNR font
inFig.update_layout(title = {'text': "Rheumatology Infusion Chairs Estimated Use", 
                             'x': .5, 'y':.95},
                             plot_bgcolor = "white",
                             yaxis_title = "Chairs Used",
                             font_family = "Times New Roman",
                             hovermode = 'x unified')
## Get Axes lines to show, format date
inFig.update_xaxes(showline = True, linewidth = 2, linecolor = 'black', 
                   showgrid = True, gridwidth = 1, gridcolor = 'black', 
                   tick0 = '2022-02-28',
                   dtick = 86400000.0 * 7, tickformat = "%d - %b \n%Y")
inFig.update_yaxes(showline = True, linewidth = 2, linecolor = 'black')
## Add rooms available
inFig.add_trace(go.Scatter(x = Exams['Date'], 
                           y = np.repeat(6, len(Exams['Date'])), 
                           line_dash="dash", 
                           line_color="yellow", 
                           #hover_data = "Chairs Available"
                           showlegend = True,
                           name = "Chairs Available")
                )
## Add 80% Benchmark
inFig.add_trace(go.Scatter(x = infRooms['Date'], 
                           y = np.repeat(5, len(infRooms['Date'])), 
                           line_dash="dash", 
                           line_color="gold", 
                           #hover_data = "Chairs Available"
                           showlegend = True,
                           name = "80% Benchmark")
                )
## Add range slider
#  Note that weeks are 8 days so that grids show up in presentation, this makes
#  it easier to slide with reference up

inFig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=8,
                     label="This Week",
                     step="day",
                     stepmode="todate"),
                dict(count=1,
                     label="This Month",
                     step="month",
                     stepmode="todate"),
                dict(count=8,
                     label="Last Week",
                     step="day",
                     stepmode="backward"),
                dict(count=1,
                     label="Last Month",
                     step="month",
                     stepmode="backward"),
                dict(count=1,
                     label="This Year",
                     step="year",
                     stepmode="todate"),
                dict(step="all")
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type="date"
    )
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
exFig.update_xaxes(showline = True, linewidth = 2, linecolor = 'black', 
                   showgrid = True, gridwidth = 1, gridcolor = 'black', 
                   tick0 = '2022-02-28',
                   dtick = 86400000.0 * 7, tickformat = "%d - %b \n%Y")
exFig.update_yaxes(showline = True, linewidth = 2, linecolor = 'black')
## Add rooms available
exFig.add_trace(go.Scatter(x = Exams['Date'], 
                           y = np.repeat(9, len(Exams['Date'])), 
                           line_dash="dash", 
                           line_color="yellow", 
                           #hover_data = "Chairs Available"
                           showlegend = True,
                           name = "Rooms Available")
                )
## Add 80% Benchmark
exFig.add_trace(go.Scatter(x = infRooms['Date'], 
                           y = np.repeat(7, len(infRooms['Date'])), 
                           line_dash="dash", 
                           line_color="gold", 
                           #hover_data = "Chairs Available"
                           showlegend = True,
                           name = "80% Benchmark")
                )
## Add range slider
#  Note that weeks are 8 days so that grids show up in presentation, this makes
#  it easier to slide with reference up
exFig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=8,
                     label="This Week",
                     step="day",
                     stepmode="todate"),
                dict(count=1,
                     label="This Month",
                     step="month",
                     stepmode="todate"),
                dict(count=8,
                     label="Last Week",
                     step="day",
                     stepmode="backward"),
                dict(count=1,
                     label="Last Month",
                     step="month",
                     stepmode="backward"),
                dict(count=1,
                     label="This Year",
                     step="year",
                     stepmode="todate"),
                dict(step="all")
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type="date"
    )
)
exFig.write_html("Rooms.html")

###############################################################################
############################    EXAMS DAY BARPT    ############################
###############################################################################


allFig = px.bar(allRooms, x = "Date", y = "Rooms", hover_data={"Date":"|%B %d"},
                color = "Weekday")
## Adding title, title location, blank background, titling axes, TNR font
allFig.update_layout(title = {'text': "Rheumatology Exam Rooms Estimated Use, All Exam Types", 
                             'x': .5, 'y':.95},
                             plot_bgcolor = "white",
                             yaxis_title = "Rooms Used",
                             font_family = "Times New Roman",
                             hovermode = 'x unified')
## Get Axes lines to show, format date
allFig.update_xaxes(showline = True, linewidth = 2, linecolor = 'black', 
                   showgrid = True, gridwidth = 1, gridcolor = 'black', 
                   tick0 = '2022-02-28',
                   dtick = 86400000.0 * 7, tickformat = "%d - %b \n%Y")
allFig.update_yaxes(showline = True, linewidth = 2, linecolor = 'black')
## Add rooms available
allFig.add_trace(go.Scatter(x = Exams['Date'], 
                           y = np.repeat(9, len(Exams['Date'])), 
                           line_dash="dash", 
                           line_color="yellow", 
                           #hover_data = "Chairs Available"
                           showlegend = True,
                           name = "Rooms Available")
                )
## Add 80% Benchmark
allFig.add_trace(go.Scatter(x = infRooms['Date'], 
                           y = np.repeat(7, len(infRooms['Date'])), 
                           line_dash="dash", 
                           line_color="gold", 
                           #hover_data = "Chairs Available"
                           showlegend = True,
                           name = "80% Benchmark")
                )
## Add range slider
#  Note that weeks are 8 days so that grids show up in presentation, this makes
#  it easier to slide with reference up

allFig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=8,
                     label="This Week",
                     step="day",
                     stepmode="todate"),
                dict(count=1,
                     label="This Month",
                     step="month",
                     stepmode="todate"),
                dict(count=8,
                     label="Last Week",
                     step="day",
                     stepmode="backward"),
                dict(count=1,
                     label="Last Month",
                     step="month",
                     stepmode="backward"),
                dict(count=1,
                     label="This Year",
                     step="year",
                     stepmode="todate"),
                dict(step="all")
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type="date"
    )
)




allFig.write_html("All Exams By Day Bars.html")
###############################################################################
############################    WEEKDAY BARPLOT    ############################
###############################################################################
## First let's do some aggregation
dayzz = list(set(allRooms['Weekday']))
# Empty list for room estimates
rooms = []
# for loop iterating over unique dates
for i in dayzz:
    # subset df to day i
    now  = allRooms[allRooms['Weekday'] == i]
    # total time on appointments
    rooms.append(np.mean(now['Rooms']))

examDays = pd.DataFrame({'Day' : dayzz, 
                         'Rooms': rooms})
examDays = examDays.round(2)


dayEx= px.bar(examDays, x = 'Day', y = 'Rooms')
dayEx.update_layout(title = {'text': "Exam Room Use by Weekday", 
                             'x': .5, 'y':.95},
                             plot_bgcolor = "white",
                             yaxis_title = "Rooms Used",
                             font_family = "Times New Roman")
## Get Axes lines to show, format date
dayEx.update_xaxes(showline = True, linewidth = 2, linecolor = 'black')
dayEx.update_yaxes(showline = True, linewidth = 2, linecolor = 'black')
## Add rooms available
dayEx.add_trace(go.Scatter(x = examDays['Day'], 
                            y = np.repeat(6, len(examDays['Day'])), 
                            line_dash="dash", 
                            line_color="yellow", 
                            #hover_data = "Chairs Available"
                            showlegend = True,
                            name = "Chairs Available")
                 )
## Add 80% Benchmark
dayEx.add_trace(go.Scatter(x = examDays['Day'], 
                           y = np.repeat(5, len(examDays['Day'])), 
                           line_dash="dash", 
                           line_color="gold", 
                           #hover_data = "Chairs Available"
                           showlegend = True,
                           name = "80% Benchmark")
)

dayEx.write_html("Average Exam Rooms by Day.html")



##########  FOR INFUSIONS   ##################
## First let's do some aggregation
dayzz = list(set(allRooms['Weekday']))
# Empty list for room estimates
rooms = []
# for loop iterating over unique dates
for i in dayzz:
    # subset df to day i
    now  = infRooms[infRooms['Weekday'] == i]
    # total time on appointments
    rooms.append(np.mean(now['Chairs']))

infDays = pd.DataFrame({'Day' : dayzz, 
                         'Chairs': rooms})
infDays = infDays.round(2)


dayInf = px.bar(infDays, x = 'Day', y = 'Chairs')
dayInf.update_layout(title = {'text': "Average Infusion Chair Use by Weekday", 
                             'x': .5, 'y':.95},
                             plot_bgcolor = "white",
                             yaxis_title = "Chairs Used",
                             font_family = "Times New Roman")
## Get Axes lines to show, format date
dayInf.update_xaxes(showline = True, linewidth = 2, linecolor = 'black')
dayInf.update_yaxes(showline = True, linewidth = 2, linecolor = 'black')
## Add rooms available
dayInf.add_trace(go.Scatter(x = infDays['Day'], 
                            y = np.repeat(6, len(infDays['Day'])), 
                            line_dash="dash", 
                            line_color="yellow", 
                            #hover_data = "Chairs Available"
                            showlegend = True,
                            name = "Chairs Available")
                 )
## Add 80% Benchmark
dayInf.add_trace(go.Scatter(x = infDays['Day'], 
                           y = np.repeat(5, len(infDays['Day'])), 
                           line_dash="dash", 
                           line_color="gold", 
                           #hover_data = "Chairs Available"
                           showlegend = True,
                           name = "80% Benchmark")
)

dayInf.write_html("Average Infusion Chairs by Day.html")

