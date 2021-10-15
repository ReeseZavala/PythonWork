# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 12:42:35 2021

@author: rzava
"""
## Goal of this file is to plot tech scores against time to show full party 
 # trends
 
import pandas as pd
import os
import re
import matplotlib.pyplot as plt

## Set Working directory to translated corpora
os.chdir("C:/Users/rzava/Box Sync/Tech Saliency/")

## Importing DFM created in R, as Quanteda is more efficient
 # This will contain all countries, rather than the subsetted 4
 # Once read, going to append with tech scores
DFM = pd.read_csv('weighted_dfm_full.csv')
## Getting rid of index Column, resetting index to doc_id's
DFM = DFM.iloc[0:DFM.shape[0],1:DFM.shape[1]]
DFM.set_index('doc_id')
## Let's try finding tech words with new Pirate Parties in data
 # Start by subsetting to Pirate entries -- following logic in TechScores.R
Bool = []
ids  = list(DFM['doc_id'])
for i in ids:
    Bool.append(i[2:5] == "PIR")

piDFM = DFM[Bool]

## Now finding means and then sorting by most used
means = piDFM.mean(axis = 0)
BigWords = means.sort_values(ascending = False)[0:21]
## Manually checking list for problem words
BigWords
## Removing party-specific words and/or country specific
BigWords = BigWords.drop(['pirat', 'parti'])
JustWords = list(BigWords.index)
JustWords = JustWords[1:12] + JustWords[14:18]


## Now to regenerate tech scores
 # First subsetting to tech words alone + doc_id for identification
DFM_tech = DFM[JustWords + ['doc_id']]
DFM_tech['techScore'] = DFM_tech.mean(axis = 1)

## Now code in countries, parties, year
country = []
party   = []
year    = []
for id in DFM_tech['doc_id']:
    country.append(id[0:2])
    party.append(id[2:5])
    year.append(id[6:10])

DFM_tech['Country'] = country
DFM_tech['Party']   = party
DFM_tech['Year']    = year
DFM_tech.groupby(['Country', 'Party'])

##Initial Plot, next file will make it pretty
plt.plot(DFM_tech['Year'], DFM_tech['techScore'])

