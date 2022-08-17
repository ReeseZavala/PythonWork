# -*- coding: utf-8 -*-

"""
Created on Mon Aug  1 09:54:37 2022
@author: zavalar
"""

import os
## Path to File
os.chdir('C:\\Users\\rzava\\OneDrive\\Documents\\Work\\ER Bullshit\\Code')
from RUT_firstPass import RUT
import pandas as pd


# inputFile  = "visitData.csv"

## Writiing Path
path = 'C:\\Users\\rzava\\OneDrive\\Documents\\Work\\ER Bullshit\\Data'
os.chdir(path)


def dicFill(DepartmentName):
    inPerson = []
    tele     = []
    which = vDat[vDat['DepartmentName'].isin(DepartmentName)]
    check = which[which['VisitType'].str.contains('PHONE|VIRTUAL')]
    tele = list(set(check['VisitTypeEpicId']))
    check = which[~which['VisitType'].str.contains('PHONE|VIRTUAL')]
    inPerson = list(set(check['VisitTypeEpicId']))
    return([inPerson, tele])


vDat = pd.read_csv('OHSU_1.csv')
dat2 = pd.read_csv('OHSU_2.csv')
dat3 = pd.read_csv('OHSU_3.csv')
dat4 = pd.read_csv('OHSU_4.csv')
dat5 = pd.read_csv('OHSU_5.csv')
dat6 = pd.read_csv('OHSU_6.csv')
vDat = vDat.append([dat2, dat3, dat4, dat5, dat6], ignore_index = True)





DepartmentName = ['DRM MED CHH1', 'DRM MED 5 CHH1']

mainDic = {'Name' : "DRM CHH",
          'lookUp' : DepartmentName,
          'Virtual' : dicFill(DepartmentName)[1],
          'In Person' : dicFill(DepartmentName)[0],
          'Hours' : 8}
specDic = {'Name' : "Infusions",
          'lookUp' : ['RHM INFUSION 4 PPV'],
          'Codes' : [6965],
          'Hours' : 8,
          'Spaces' : 5}
ts1Dicic = {'Name' : "CTS",
          'lookUp' : ['CTS CARDIAC CHH1'],
          'Virtual' : [21031],
          'In Person' : [7667, 21003, 21004, 21022, 21023],
          'Hours' : 8}

Depts = []

os.chdir('C:\\Users\\rzava\\OneDrive\\Documents\\Work\\ER Bullshit\\Code')
plotFolder = 'C:\\Users\\rzava\\OneDrive\\Documents\\Work\\ER Bullshit\\DRM_Figures'
RUT(DATA = vDat, plotFolder = plotFolder, firstMonday = "2020-12-28", deptSearch = Depts, 
    mainDic=mainDic, examRooms = 22, specialtyNeeded=False, timeShare = False)