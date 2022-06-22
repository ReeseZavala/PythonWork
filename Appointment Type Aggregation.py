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
outputFile = "PPV_Visit_Times.csv"
path = 'C:\\Users\\rzava\\OneDrive\\Documents\\Work\\ER Bullshit'
writing = path + '\\' + outputFile


os.chdir(path)

vDat = pd.read_csv(inputFile)

##### Need to first find unique appt types
    # Then find avg time
    # modal time
    # Perhaps also std error.....?
    # EZ

## List of unique appointments, ordered numerically   
 # Need list command around set or else not subscriptable
 # This will be used to call unique ID's to find matching names
apts = list(set(vDat['Visit_ID']))
## Isolate code values as list for iteration
 # aptsNames used so that we have same index as dataframe
aptsNames = list(vDat['Visit_Type'])
visitID = list(set(aptsNames))
visitID.sort()
## For loop iterating over apptmt codes to get corresponding names
codDic = []
for x in apts:
    codDic.append(aptsNames[list(vDat['Visit_ID']).index(x)])

## Then into a dictionary  
 # Key is Code, Value is String Name  
myDic = {}    
for i in codDic:
    myDic[apts[codDic.index(i)]] = i

#######################################
## This shit is so fucked, I can't even
 # Debugging because not all keys added
 # Try, except bug finding to manually add fuckbeans

for i in apts:
    try:
        myDic[i]
    except KeyError:
        line = list(vDat['Visit_ID']).index(i)
        askingForALine = list(vDat['Visit_Type'])[line]
        # print(askingForALine)
        myDic[i] = askingForALine


## myDic is ready
## So hungry, going to return to do the calculations later
 # Left:
 # Aggregate average time by apptmt type
 # Find mean time per apptmt type
 # Write csv with code, apptmt name, mean, mode

## Aggregating mean time, and mode time, then putting them together
 # Probably not efficient, but it works
 # Could have fed data directly into columns, but this reads clearly
meanTime = vDat[['Visit_ID', 'Appointment_Length']].groupby(['Visit_ID']).mean()
modeTime = vDat[['Visit_ID', 'Appointment_Length']].groupby(['Visit_ID']).agg(lambda x: pd.Series.mode(x)[0])
meanTime['Mode'] = modeTime
time = meanTime

#######################################################################
# Function for rounding up -- Works only for sorted input lists
def nearestValue(inputList, keyValue):
    # NULL list for differences
    bigDif = []
    # Loop to get |difference|
    for i in range(0,len(inputList)):
        bigDif.append(abs(inputList[i] - keyValue))
    # Need to create new list to sort so we can find two lowest values    
    hold = list(bigDif)
    bigDif.sort()
    # Grab first and second values
    lilOne = bigDif[0]
    lilTwo = bigDif[1]
    # Find key from differences list
    keyOne = hold.index(lilOne)
    keyTwo = hold.index(lilTwo)
    # Return higher key's value from input list
    return(inputList[max([keyOne, keyTwo])])
########################################################################

## Now to replace mean values with rounding up
 # Then pick the higher between mean and mode
 # First generating list of benchmark times to round into
wellRounded = list(range(5, 90, 5))
hold = list(range(90, 400, 30))
wellRounded.extend(hold)
# Now using function to create list of new rounders
tendies = []
for t in meanTime['Appointment_Length']:
    tendies.append(nearestValue(wellRounded, t))

time['Mean_Time_Rounded'] = tendies
# Pick out higher number between two apptmt estimates
kicker = []
for (a, m) in zip(tendies, modeTime['Appointment_Length']):
    kicker.append(max([a,int(m)]))
# Add it to our DF   
time['Appointment_Estimate'] = kicker
apts.sort()
orderedNames = []
for i in apts:
    orderedNames.append(myDic[i])




funLilTable = pd.DataFrame()
funLilTable['Visit_ID'] = apts
funLilTable['Visit_Name'] = orderedNames
funLilTable['Appointment_Length'] = kicker

funLilTable.to_csv(writing)






