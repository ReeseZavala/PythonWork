# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 17:14:15 2021

@author: rzava
"""
import numpy as np
import pandas as pd
import os
import statsmodels.api as sm
## For formatting strings w/ commas as floats
from locale import atof, setlocale, LC_NUMERIC
import math
## 'English_Canada.1252' definitely formats commas correctly
setlocale(LC_NUMERIC, 'English_Canada.1252')
os.chdir("C:/Users/rzava/Box Sync/Tech Saliency/")

GDP_DF = pd.read_csv("GDP.csv", index_col=0)
theDF = pd.read_csv("DiD_scores.csv")

## Need to recode the country codes in DF to strings
 # Then add GDP info based on country and year

## Dictionary of country codes from manifesto project
getDict = {11 : 'Sweden', 12 : 'Norway', 13 : 'Denmark', 14 : 'Finland',
           15 : 'Iceland', 21 : 'Belgium', 22 : 'Netherlands', 23 : 'Luxembourg',
           31 : 'France', 32 : 'Italy', 33 : 'Spain', 34 : 'Greece', 
           35 : 'Portugal', 41 : 'Germany', 42 : 'Austria', 43 : 'Switzerland',
           51 : 'United Kingdom', 52 : 'United Kingdom', 53 : 'Ireland', 
           54 : 'Malta', 55 : 'Cyprus', 61 : 'United States', 62 : 'Canada',
           63 : 'Australia', 64 : 'New Zealand', 71 : 'Japan', 72 : 'Israel',
           73 : 'Sri Lanka', 74 : 'Turkey', 75 : 'Albania', 76 : 'Armenia',
           77 : 'Azerbaijan', 78 : 'Belarus', 79 : 'Bosnia and Herzegovina',
           80 : 'Bulgaria', 81 : 'Croatia', 82 : 'Czechia', 83 : 'Estonia',
           84 : 'Georgia', 85 : 'German Democratic Republic', 86 : 'Hungary',
           87 : 'Latvia', 88 : 'Lithuania', 89 : 'North Macedonia', 90 : 'Moldova',
           91 : 'Montenegro', 92 : 'Poland', 93 : 'Romania', 94 : 'Russia',
           95 : 'Serbia', 96 : 'Slovakia', 97 : 'Slovenia', 98 : 'Ukraine',
           113 : 'South Korea', 171 : 'Mexico', 181 : 'South Africa'}

## Replace country codes with names that match GDP dataframe
i = 0
for c in theDF['Country']:
    theDF['Country'][i] = getDict[c]
    i += 1

## Find GDP for each country for each year
GDP = []
for i in range(0, len(theDF)):
    yr = str(theDF['Year'][i])
    cn = theDF['Country'][i]
    if cn == "Canada":
        GDP.append(np.NaN)
    elif GDP_DF.loc[cn, yr] == ':':
        GDP.append(np.NaN)
    else:
        GDP.append(math.log(atof(GDP_DF.loc[cn, yr])))
        
theDF['GDP'] = GDP
theDF.to_csv('DiD_Scores.csv')

## Regression
 # Drop Na's
theDF = theDF.dropna()
X = theDF[['DiD', 'GDP']]
Y = theDF['Score']
X2 = sm.add_constant(X)
est = sm.OLS(Y.astype(float), X2.astype(float)).fit()
print(est.summary())







