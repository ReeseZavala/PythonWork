# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 20:55:23 2021

@author: rzava
"""

import os
import pandas as pd
from statistics import mean
import math
import statsmodels.api as sm

## Set Working directory to DFM Locations
os.chdir("C:/Users/rzava/Box Sync/Tech Saliency/")

Load = pd.read_csv('TechScores_DFM.csv')
## Subsetting DFM to relevant datapoints
DFM = Load[['techScore', 'Country', 'Party', 'Year']]
## The plan:
 # We need a DF with Country/Year data, with mean tech scores, treated, and 
 # pre-post dummy. Then multiply for DiD variable 
 # Start with for loop subsetting DFM into by countries to get means and years
 # Also add treated (Pirate) dummy and time period dummy
 #      treated dummy using regex for docnames to find "PIR"
 # Should be easy to wrap everything into one loop w/o manual additions
 
## hold: first DF will all obs from one country
## Years: list of unique years from that country
## holden: DF to be updated by row with aggregates from each year from hold
## lilbit: Smaller DF of hold, just the year from list
## teenybit: list to be updated with columns from holden
## DiD_DF: the mamajama, what we've all been waiting for, the whole damn thing

countries = DFM['Country'].unique()
n = list(range(0, len(countries)))
DiD_DF = pd.DataFrame(columns = ['Country', 'Score', 'Year', 'Treated', 
                                 'Period'])

for c in countries:
# First subsetting down to country
    hold = DFM.loc[DFM['Country'] == c]  # Small DF for country
    years = hold['Year'].unique()
    n = list(range(0, len(years))) # defining n because append function was being fucky with lists
    holden = pd.DataFrame(columns = ['Country', 'Score', 'Year', 'Treated', 
                                     'Period'], index = [n])
    i = 0 # Step function for iterating through holden index
# Now for each individual year, produce list of avg score, country, year
    for y in years:
        lilbit = hold.loc[hold['Year'] == y] # Small DF for country & Year
        # Start easy: mean, country, year
        teenybit = [lilbit['Country'].tolist()[0], math.log(mean(lilbit['techScore'])), y] # row of information to add, must go country, mean, year
        if "PIR" in hold['Party'].tolist():
            teenybit.append(1)
        else:
            teenybit.append(0)
        if y >= 2009:
            teenybit.append(1)
        else: 
            teenybit.append(0)
        holden.iloc[i] = teenybit
        i += 1
    DiD_DF = DiD_DF.append(holden, ignore_index = False)

## Introducing DiD variable
DiD_DF['DiD'] = DiD_DF['Period'] * DiD_DF['Treated']

X = DiD_DF['DiD']
Y = DiD_DF['Score']
X2 = sm.add_constant(X)
est = sm.OLS(Y.astype(float), X2.astype(float)).fit()
print(est.summary())














