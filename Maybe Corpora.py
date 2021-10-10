# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 10:18:01 2020

@author: rzava
"""

import os
import re
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import googletrans 
from googletrans import Translator

translator = Translator()

def getDicd(Dictionary, Folder = None):
    #Set working Directory and reference for filenames
    os.chdir('C:/Users/rzava/Box Sync/Tech Saliency/Corpora' + Folder)
    directory = os.fsencode('C:/Users/rzava/Box Sync/Tech Saliency/Corpora' + Folder)   
    #List of file names
    all_files = os.listdir(directory) 
    for file in all_files:
        #stringify docnames
        #add each name to a list so we can populate the dic
        k = re.split("b'", re.split(".txt", str(file))[0])[1]
        Dictionary[k] = [re.split("_", k)[0], re.split("_", k)[1], open(re.split("'", re.split("b'", str(file))[1])[0], encoding="latin-1").read()]
    return Dictionary 



CN_Man = {}
CZ_Man = {}
DE_Man = {}
IC_Man = {}
FR_Man = {}
IT_Man = {}
LV_Man = {}
NW_Man = {}
FI_Man = {}
UK_Man = {}

getDicd(CZ_Man, Folder = "/CZ")


translator.translate('ropy a plynu tvorí 95 % podílu na zneci\x9atování ovzdu\x9aí.\n\x95 Zprísníme kontroly velkých prumyslových zneci\x9atovatelu.').text

CZ_Man[0]

Men = [CZ_Man, CN_Man, DE_Man, FI_Man, FR_Man, IC_Man, IT_Man, LV_Man, NW_Man, UK_Man]
Folders = os.listdir('C:/Users/rzava/Box Sync/Tech Saliency/Corpora')
for i, k in zip(Men, Folders):
    getDicd(i, Folder = '\\' + k)

NewMen = [IC_Man, CZ_Man, DE_Man, FR_Man, IT_Man, LV_Man, NW_Man, FI_Man, UK_Man]
    


IC_WordsThatMatter = [["information", "upplýsingar"], ["data", "gögn"], ["transparency", 
                   "gegnsæi"], ["freedom", "frelsi"], ["freedom of expression", "tjáningarfrelsi"],
                   ["privacy", "næði"]]


CZ_WordsThatMatter = [["information", "informace"], ["data", "data"], ["transparency", 
                   "transparent"], ["freedom", "svoboda"], ["freedom of expression", "výraz"],
                   ["privacy", "soukromí"]]


DE_WordsThatMatter = [["information", "information"], ["data", "daten"], ["transparency", 
                   "transparenz"], ["freedom", "freiheit"], ["freedom of expression", "ausdruck"],
                   ["privacy", "privatsphäre"]]


FR_WordsThatMatter = [["information", "information"], ["data", "données"], ["transparency", 
                   "transparence"], ["freedom", "liberté"], ["freedom of expression", "expression"],
                   ["privacy", "intimité"]]


IT_WordsThatMatter = [["information", "informazione"], ["data", "dati"], ["transparency", 
                   "trasparenza"], ["freedom", "libertà"], ["freedom of expression", "espressione"],
                   ["privacy", "privacy"]]


LV_WordsThatMatter = [["information", "informāciju"], ["data", "dati"], ["transparency", 
                   "pārredzamība"], ["freedom", "brīvība"], ["freedom of expression", "izteiksme"],
                   ["privacy", "privātumu"]]

NW_WordsThatMatter = [["information", "informasjon"], ["data", "data"], ["transparency", 
                   "gjennomsiktig"], ["freedom", "frihet"], ["freedom of expression", "uttrykk"],
                   ["privacy", "privatliv"]]


FI_WordsThatMatter = [["information", "tiedot"], ["data", "tieto"], ["transparency", 
                   "selkeä"], ["freedom", "vapaus"], ["freedom of expression", "ilmaisun"],
                   ["privacy", "yksityisyys"]]


UK_WordsThatMatter = [["information", "information"], ["data", "data"], ["transparency", 
                   "transparency"], ["freedom", "freedom"], ["freedom of expression", "expression"],
                   ["privacy", "privacy"]]


WordsThatMatter = [IC_WordsThatMatter, CZ_WordsThatMatter, DE_WordsThatMatter, FR_WordsThatMatter, 
                   IT_WordsThatMatter, LV_WordsThatMatter, NW_WordsThatMatter,FI_WordsThatMatter, UK_WordsThatMatter]

IC_Words = []
CZ_Words = []
DE_Words = []
FR_Words = []
IT_Words = []
LV_Words = []
NW_Words = []
FI_Words = []
UK_Words = []

tran_Count = []
for i in range(0, len(IC_WordsThatMatter)):
    Eng = IC_WordsThatMatter[i][0]
    Oth = IC_WordsThatMatter[i][1]
    tran_Count.append(Eng)
    for item in IC_Man.values():
        tran_Count.append([item[2].count(Oth), item[1][0:4], item[0]])
    IC_Words.append(tran_Count)

tran_Count = []
for i in range(0, len(CZ_WordsThatMatter)):
    Eng = CZ_WordsThatMatter[i][0]
    Oth = CZ_WordsThatMatter[i][1]
    tran_Count.append(Eng)
    for item in CZ_Man.values():
        tran_Count.append([item[2].count(Oth), item[1][0:4], item[0]])
    CZ_Words.append(tran_Count)
    
tran_Count = []
for i in range(0, len(DE_WordsThatMatter)):
    Eng = DE_WordsThatMatter[i][0]
    Oth = DE_WordsThatMatter[i][1]
    tran_Count.append(Eng)
    for item in DE_Man.values():
        tran_Count.append([item[2].count(Oth), item[1][0:4], item[0]])
    DE_Words.append(tran_Count)

tran_Count = []
for i in range(0, len(FR_WordsThatMatter)):
    Eng = FR_WordsThatMatter[i][0]
    Oth = FR_WordsThatMatter[i][1]
    tran_Count.append(Eng)
    for item in FR_Man.values():
        tran_Count.append([item[2].count(Oth), item[1][0:4], item[0]])
    FR_Words.append(tran_Count)
    
tran_Count = []
for i in range(0, len(IT_WordsThatMatter)):
    Eng = IT_WordsThatMatter[i][0]
    Oth = IT_WordsThatMatter[i][1]
    tran_Count.append(Eng)
    for item in IT_Man.values():
        tran_Count.append([item[2].count(Oth), item[1][0:4], item[0]])
    IT_Words.append(tran_Count)
    
tran_Count = []
for i in range(0, len(LV_WordsThatMatter)):
    Eng = LV_WordsThatMatter[i][0]
    Oth = LV_WordsThatMatter[i][1]
    tran_Count.append(Eng)
    for item in LV_Man.values():
        tran_Count.append([item[2].count(Oth), item[1][0:4], item[0]])
    LV_Words.append(tran_Count)
    
tran_Count = []
for i in range(0, len(NW_WordsThatMatter)):
    Eng = NW_WordsThatMatter[i][0]
    Oth = NW_WordsThatMatter[i][1]
    tran_Count.append(Eng)
    for item in NW_Man.values():
        tran_Count.append([item[2].count(Oth), item[1][0:4], item[0]])
    NW_Words.append(tran_Count)
    
tran_Count = []
for i in range(0, len(FI_WordsThatMatter)):
    Eng = FI_WordsThatMatter[i][0]
    Oth = FI_WordsThatMatter[i][1]
    tran_Count.append(Eng)
    for item in FI_Man.values():
        tran_Count.append([item[2].count(Oth), item[1][0:4], item[0]])
    FI_Words.append(tran_Count)
    
tran_Count = []
for i in range(0, len(UK_WordsThatMatter)):
    Eng = UK_WordsThatMatter[i][0]
    Oth = UK_WordsThatMatter[i][1]
    tran_Count.append(Eng)
    for item in UK_Man.values():
        tran_Count.append([item[2].count(Oth), item[1][0:4], item[0]])
    UK_Words.append(tran_Count)

IC_Words = IC_Words[0]
CZ_Words = CZ_Words[0]
DE_Words = DE_Words[0]
FR_Words = FR_Words[0]
IT_Words = IT_Words[0]
LV_Words = LV_Words[0]
NW_Words = NW_Words[0]
FI_Words = FI_Words[0]
UK_Words = UK_Words[0]

wordsWordsWORDS = [IC_Words, CZ_Words, DE_Words, FR_Words, IT_Words, LV_Words, NW_Words, FI_Words, UK_Words]


IC_Dates = []
CZ_Dates = []
DE_Dates = []
FR_Dates = []
IT_Dates = []
LV_Dates = []
NW_Dates = []
FI_Dates = []
UK_Dates = []
allDates = [IC_Dates, CZ_Dates, DE_Dates, FR_Dates,  IT_Dates, LV_Dates, NW_Dates, FI_Dates, UK_Dates]
for i in IC_Words:           
   if i[1] not in IC_Dates and len(i[1]) > 2:
       IC_Dates.append(i[1])
       
for i in CZ_Words:           
   if i[1] not in CZ_Dates and len(i[1]) > 2:
       CZ_Dates.append(i[1])
       
for i in DE_Words:           
   if i[1] not in DE_Dates and len(i[1]) > 2:
       DE_Dates.append(i[1])
       
for i in FR_Words:           
   if i[1] not in FR_Dates and len(i[1]) > 2:
       FR_Dates.append(i[1])
       
for i in IT_Words:           
   if i[1] not in IT_Dates and len(i[1]) > 2:
       IT_Dates.append(i[1])
       
for i in LV_Words:           
   if i[1] not in LV_Dates and len(i[1]) > 2:
       LV_Dates.append(i[1])
       
for i in NW_Words:           
   if i[1] not in NW_Dates and len(i[1]) > 2:
       NW_Dates.append(i[1])
       
for i in FI_Words:           
   if i[1] not in FI_Dates and len(i[1]) > 2:
       FI_Dates.append(i[1])
       
for i in UK_Words:           
   if i[1] not in UK_Dates and len(i[1]) > 2:
       UK_Dates.append(i[1])
       
for i in allDates:
    i.sort()

for date in allDates:
    for n, i in enumerate(date):
        date[n] = i[0:4]

IC_IDs= []
CZ_IDs= []
DE_IDs= []
FR_IDs= []
IT_IDs= []
LV_IDs= []
NW_IDs= []
FI_IDs= []
UK_IDs= []
AllIDs = [IC_IDs, CZ_IDs, DE_IDs, FR_IDs, IT_IDs, LV_IDs, NW_IDs, FI_IDs, UK_IDs]
for i in IC_Words:           
   if i[2] not in IC_IDs and len(i[2]) > 2:
       IC_IDs.append(i[2])
       
for i in CZ_Words:           
   if i[2] not in CZ_IDs and len(i[2]) > 2:
       CZ_IDs.append(i[2])
       
for i in DE_Words:           
   if i[2] not in DE_IDs and len(i[2]) > 2:
       DE_IDs.append(i[2])
       
for i in FR_Words:           
   if i[2] not in FR_IDs and len(i[2]) > 2:
       FR_IDs.append(i[2])
       
for i in IT_Words:           
   if i[2] not in IT_IDs and len(i[2]) > 2:
       IT_IDs.append(i[2])
       
for i in LV_Words:           
   if i[2] not in LV_IDs and len(i[2]) > 2:
       LV_IDs.append(i[2])
       
for i in NW_Words:           
   if i[2] not in NW_IDs and len(i[2]) > 2:
       NW_IDs.append(i[2])
       
for i in FI_Words:           
   if i[2] not in FI_IDs and len(i[2]) > 2:
       FI_IDs.append(i[2])
       
for i in UK_Words:           
   if i[2] not in UK_IDs and len(i[2]) > 2:
       UK_IDs.append(i[2])

for i in AllIDs:
    i.sort()       
#######         IC PLOTS          ##########
IC_Values = []
for i in IC_Dates:
    a = 0
    for k in IC_Words:
        if k[1] == i:
            a += int(k[0])
        else: 
            pass
    IC_Values.append(a)
            
plt.plot(IC_Dates, IC_Values)
plt.xlabel("Election Year")
plt.ylabel("Technological Mentions")
plt.title("Total Iceland Mentions")



IC_ptyNames = ["Left Green Movement", "Alliance", "Liberal Party", "Citizens' Movement", "Bright Future", "Reform", "Independence", "Progressive", "Pirate", "People's"]
IC_Dics = {}
for item, name in zip(IC_IDs, IC_ptyNames):
    IC_Dics[item] = name


IC_partyVals = []
for j in IC_IDs:
    a = 0
    IC_partyVals.append(str(j))
    for i in IC_Dates:
        for k in IC_Words:
            if k[1] == i and k[2] == j:
                a += int(k[0])
            else: 
                pass
        IC_partyVals.append(a)

for n, i in enumerate(IC_partyVals):
    try:
        if i in IC_Dics.keys():
            IC_partyVals[n] = IC_Dics[i]
        else:
            pass
    except:
        pass

LGreen = [IC_partyVals[0:7]]
Alliance = [IC_partyVals[7:14]]
Liberal = [IC_partyVals[14:21]]
Citizen = [IC_partyVals[21:28]]
BFuture = [IC_partyVals[28:35]]
Reform = [IC_partyVals[35:42]]
Indep = [IC_partyVals[42:49]]
Prog = [IC_partyVals[49:56]]
Pi = [IC_partyVals[56:63]]
PPl = [IC_partyVals[63:70]]

IC_parties = [LGreen, Alliance, Liberal, Citizen, BFuture, Reform, Indep, Prog, Pi, PPl]

for party in IC_parties:
    plt.plot(IC_Dates, party[0][1:7], label = party[0][0])
    plt.legend(loc = "upper left")
    plt.xlabel("Dates")
    plt.ylabel("Technological Mentions")
    plt.title("Iceland Parties Use of Tech Words")
    
    
    
    
#######         CZ PLOTS          ##########
CZ_Values = []
for i in CZ_Dates:
    a = 0
    for k in CZ_Words:
        if k[1] == i:
            a += int(k[0])
        else: 
            pass
    CZ_Values.append(a)
            
plt.plot(CZ_Dates, CZ_Values)
plt.xlabel("Election Year")
plt.ylabel("Technological Mentions")
plt.title("Total Czech Mentions")



CZ_ptyNames = ["Greens", "Communist", "CSSD", "ODA", "ANO", "KDU", "TOP09", "STAN", " SPR-RSČ", "Úsvit", "SPD", "VV", "Pirate"]
CZ_Dics = {}
for item, name in zip(CZ_IDs, CZ_ptyNames):
    CZ_Dics[item] = name


CZ_partyVals = []
for j in CZ_IDs:
    a = 0
    CZ_partyVals.append(str(j))
    for i in CZ_Dates:
        for k in CZ_Words:
            if k[1] == i and k[2] == j:
                a += int(k[0])
            else: 
                pass
        CZ_partyVals.append(a)

for n, i in enumerate(CZ_partyVals):
    try:
        if i in CZ_Dics.keys():
            CZ_partyVals[n] = CZ_Dics[i]
        else:
            pass
    except:
        pass

LGreen = [CZ_partyVals[0:6]]
Com = [CZ_partyVals[6:12]]
CSSD = [CZ_partyVals[12:18]]
ODA = [CZ_partyVals[18:24]]
ANO = [CZ_partyVals[24:30]]
KDU = [CZ_partyVals[30:36]]
TOP = [CZ_partyVals[36:42]]
STAN = [CZ_partyVals[42:48]]
SPR = [CZ_partyVals[48:54]]
USVIT = [CZ_partyVals[54:60]]
SPD = [CZ_partyVals[60:66]]
VV = [CZ_partyVals[66:72]]
Pi = [CZ_partyVals[72:78]]

CZ_parties = [LGreen, Com, CSSD, ODA, ANO, KDU, TOP, STAN, SPR, USVIT, SPD, VV, Pi]

for party in CZ_parties:
    plt.plot(CZ_Dates, party[0][1:6], label = party[0][0])
    plt.legend(loc = "upper left")
    plt.xlabel("Dates")
    plt.ylabel("Technological Mentions")
    plt.title("Czech Parties Use of Tech Words")
    
    
    
    
#######         DE PLOTS          ##########
DE_Values = []
for i in DE_Dates:
    a = 0
    for k in DE_Words:
        if k[1] == i:
            a += int(k[0])
        else: 
            pass
    DE_Values.append(a)
            
plt.plot(DE_Dates, DE_Values)
plt.xlabel("Election Year")
plt.ylabel("Technological Mentions")
plt.title("Total German Mentions")



DE_ptyNames = ["Greens", "PDS", "L-PDS", "Linke", "SPD", "FDP", "CDU", "Pi", "AfD"]
DE_Dics = {}
for item, name in zip(DE_IDs, DE_ptyNames):
    DE_Dics[item] = name


DE_partyVals = []
for j in DE_IDs:
    a = 0
    DE_partyVals.append(str(j))
    for i in DE_Dates:
        for k in DE_Words:
            if k[1] == i and k[2] == j:
                a += int(k[0])
            else: 
                pass
        DE_partyVals.append(a)

for n, i in enumerate(DE_partyVals):
    try:
        if i in DE_Dics.keys():
            DE_partyVals[n] = DE_Dics[i]
        else:
            pass
    except:
        pass

Green = [DE_partyVals[0:6]]
PDS = [DE_partyVals[6:12]]
Linke = [DE_partyVals[12:18]]
LinkeR = [DE_partyVals[18:24]]
SPD = [DE_partyVals[24:30]]
FDP = [DE_partyVals[30:36]]
CD = [DE_partyVals[36:42]]
Pi = [DE_partyVals[42:48]]
AfD = [DE_partyVals[48:54]]


DE_parties = [Green, PDS, Linke, LinkeR, SPD, FDP, CD, Pi, AfD]

for party in DE_parties:
    plt.plot(DE_Dates, party[0][1:6], label = party[0][0])
    plt.legend(loc = "upper left")
    plt.xlabel("Dates")
    plt.ylabel("Technological Mentions")
    plt.title("German Parties Use of Tech Words")    
    
    
    
#######         FR PLOTS          ##########
FR_Values = []
for i in FR_Dates:
    a = 0
    for k in FR_Words:
        if k[1] == i:
            a += int(k[0])
        else: 
            pass
    FR_Values.append(a)
            
plt.plot(FR_Dates, FR_Values)
plt.xlabel("Election Year")
plt.ylabel("Technological Mentions")
plt.title("Total French Mentions")



FR_ptyNames = ["FDG", "Greens", "PCF", "PRG", "Left", "SIFO", "RRRS", "En Marche!", "UDI", "UDF", "UMP", "NC", "AC", "FN"]
FR_Dics = {}
for item, name in zip(FR_IDs, FR_ptyNames):
    FR_Dics[item] = name


FR_partyVals = []
for j in FR_IDs:
    a = 0
    FR_partyVals.append(str(j))
    for i in FR_Dates:
        for k in FR_Words:
            if k[1] == i and k[2] == j:
                a += int(k[0])
            else: 
                pass
        FR_partyVals.append(a)

for n, i in enumerate(FR_partyVals):
    try:
        if i in FR_Dics.keys():
            FR_partyVals[n] = FR_Dics[i]
        else:
            pass
    except:
        pass

LGreen = [FR_partyVals[0:4]]
Com = [FR_partyVals[4:8]]
CSSD = [FR_partyVals[8:12]]
ODA = [FR_partyVals[12:16]]
ANO = [FR_partyVals[16:20]]
KDU = [FR_partyVals[20:24]]
TOP = [FR_partyVals[24:28]]
STAN = [FR_partyVals[28:32]]
SPR = [FR_partyVals[32:36]]
USVIT = [FR_partyVals[36:40]]
SPD = [FR_partyVals[40:44]]
VV = [FR_partyVals[44:48]]
Pi = [FR_partyVals[48:52]]
X = [FR_partyVals[52:56]]

FR_parties = [LGreen, Com, CSSD, ODA, ANO, KDU, TOP, STAN, SPR, USVIT, SPD, VV, Pi, X]

for party in FR_parties:
    plt.plot(FR_Dates, party[0][1:4], label = party[0][0])
    plt.legend(loc = "upper left")
    plt.xlabel("Dates")
    plt.ylabel("Technological Mentions")
    plt.title("Frech Parties Use of Tech Words")
    
    
    

    
#######         NW PLOTS          ##########
NW_Values = []
for i in NW_Dates:
    a = 0
    for k in NW_Words:
        if k[1] == i:
            a += int(k[0])
        else: 
            pass
    NW_Values.append(a)
            
plt.plot(NW_Dates, NW_Values)
plt.xlabel("Election Year")
plt.ylabel("Technological Mentions")
plt.title("Total Norwegian Mentions")



NW_ptyNames = ["Greens", "Socialists", "Communists", "Liberal", "KrF", "Conservative", "Center", "FrP"]
NW_Dics = {}
for item, name in zip(NW_IDs, NW_ptyNames):
    NW_Dics[item] = name


NW_partyVals = []
for j in NW_IDs:
    a = 0
    NW_partyVals.append(str(j))
    for i in NW_Dates:
        for k in NW_Words:
            if k[1] == i and k[2] == j:
                a += int(k[0])
            else: 
                pass
        NW_partyVals.append(a)

for n, i in enumerate(NW_partyVals):
    try:
        if i in NW_Dics.keys():
            NW_partyVals[n] = NW_Dics[i]
        else:
            pass
    except:
        pass

Green = [NW_partyVals[0:6]]
PDS = [NW_partyVals[6:12]]
Linke = [NW_partyVals[12:18]]
LinkeR = [NW_partyVals[18:24]]
SPD = [NW_partyVals[24:30]]
FDP = [NW_partyVals[30:36]]
CD = [NW_partyVals[36:42]]
Pi = [NW_partyVals[42:48]]


NW_parties = [Green, PDS, Linke, LinkeR, SPD, FDP, CD, Pi, AfD]

for party in NW_parties:
    plt.plot(NW_Dates, party[0][1:6], label = party[0][0])
    plt.legend(loc = "upper left")
    plt.xlabel("Dates")
    plt.ylabel("Technological Mentions")
    plt.title("Norwegian Parties Use of Tech Words")    


#######         UK PLOTS          ##########
UK_Values = []
for i in UK_Dates:
    a = 0
    for k in UK_Words:
        if k[1] == i:
            a += int(k[0])
        else: 
            pass
    UK_Values.append(a)
            
plt.plot(UK_Dates, UK_Values)
plt.xlabel("Election Year")
plt.ylabel("Technological Mentions")
plt.title("Total UK Mentions")



UK_ptyNames = ["Greens", " Sinn Féin", "Labour", "SDLP", "LibDems", "Alliance", "Conservatives", "UUP", "PC", "SNP", "DUP", "UKIP"]
UK_Dics = {}
for item, name in zip(UK_IDs, UK_ptyNames):
    UK_Dics[item] = name


UK_partyVals = []
for j in UK_IDs:
    a = 0
    UK_partyVals.append(str(j))
    for i in UK_Dates:
        for k in UK_Words:
            if k[1] == i and k[2] == j:
                a += int(k[0])
            else: 
                pass
        UK_partyVals.append(a)

for n, i in enumerate(UK_partyVals):
    try:
        if i in UK_Dics.keys():
            UK_partyVals[n] = UK_Dics[i]
        else:
            pass
    except:
        pass

Green = [UK_partyVals[0:6]]
PDS = [UK_partyVals[6:12]]
Linke = [UK_partyVals[12:18]]
LinkeR = [UK_partyVals[18:24]]
SPD = [UK_partyVals[24:30]]
FDP = [UK_partyVals[30:36]]
CD = [UK_partyVals[36:42]]
Pi = [UK_partyVals[42:48]]
AfD = [UK_partyVals[48:54]]
er = [UK_partyVals[54:60]]
Pt = [UK_partyVals[60:66]]
Apo = [UK_partyVals[66:72]]

UK_parties = [Green, PDS, Linke, LinkeR, SPD, FDP, CD, Pi, AfD, er, Pt, Apo]

for party in UK_parties:
    plt.plot(UK_Dates, party[0][1:6], label = party[0][0])
    plt.legend(loc = "upper left")
    plt.xlabel("Dates")
    plt.ylabel("Technological Mentions")
    plt.title("UK Parties Use of Tech Words")    
    


#######     Extra Functions       ##########
# for i in range(0,len(IC_Words)):
#     for j, k in zip(range(1, len(IC_Words[i])), IC_Man.values()):
#         IC_Test[i][j].append(k[0])



# for i, k in zip(Men, Folders):
#     os.chdir('E:\Academic\Summer\Technology\Python\ManisnoPedis')
#     writer = csv.writer(io.open(k + '_ManisnoPedis.csv', 'w', encoding="latin-1"))
#     writer.writerow(["PartyName", "Date", "Text"])
#     for item in i.values():
#         if len(item[2]) < 8100:
#             csv_line = [item[0], item[1], item[2]]
#             writer.writerow(csv_line)
#         else:
#             a = len(item[2]) // 8100
#             b = len(item[2]) % 8100
#             for i in range(0,a-1):
#                 item.append(item[2][i*8100:(i + 1)*8100])
#             item.append(item[2][a * 8100:len(item[2])])
#             csv_line = [item[0], item[1], item[3:a+3]]
#             writer.writerow(csv_line)



