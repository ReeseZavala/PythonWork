# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
##### WORKING NOTES #####
# Need to redo codDic so that we are returning the codes associated with the appt names
# For some reason 1352 not associated with a name


# =============================================================================
# import sys
# ## Clear Environment
# sys.modules[__name__].__dict__.clear()
# =============================================================================

import pandas as pd
import os

inputFile  = "visitData.csv"
path = 'C:\\Users\\rzava\\OneDrive\\Documents\\Work\\ER Bullshit'
# outputFile = "PPV_Visit_Times.csv"
# writing = path + '\\' + outputFile


## Establish Path
os.chdir(path)
## Read in dataset of visits
vDat = pd.read_csv(inputFile)


#####  GOALS  #####
## Group by practice, then date
## formula (\sum{a_i*x_i} + \sum{a_i * 15})/(.8*480)
## For Rheum, probably going to have to separate infusions out

RHM = vDat[vDat['Department_Name'].str.contains("RHM")]

## Room/Day Function
#  data(dataframe) with all appointments
#  dates(string) name of variable in dataframe with dates of apptmts
#  times(string) name of variable with scheduled times
#  hours(integer) number of hours in a day clinic is open
def estimateRooms(data, dates, times, hours):
    # First find unique dates in dataset
    dateList = list(set(data[dates]))
    # Empty list for room estimates
    rooms = []
    # for loop iterating over unique dates
    for i in dateList:
        # subset df to day i
        now  = data[data[dates] == i]
        # total time on appointments
        apptmt = sum(now[times])
        # turnover time (# of apptmts * 15 min)
        turnover = now.shape[0] * 15
        # append row of date, room formula to output df
        rooms.append((apptmt + turnover) / (.8 * 60 * hours))
    # Output DF of dates w/ room usage
    letItOut = pd.DataFrame({'Date' : dateList, 
                                       'Rooms': rooms})
    return(letItOut)

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











































