#!/usr/bin/python

import ompapresetvariables as ov
import ompafunctions as ofunc

#####################################################################
### LOAD THE INDIVIDUAL-EVENT JSON FILES (GENERATED BY WEB SCRAPER)

# array of .json file system paths --> ParseScrapyData() internally uses LoadScrapyData() --> Array of Age Group Strokes
ArrOfAgeGroupStrokes = ofunc.ParseScrapyData(ov.AgeGroupStrokeJSONs)

#####################################################################
### MATCH THE SWIMMERS FROM DIFFERENT EVENT JSON FILES 
### MATCH THEM INTO SINGLE SWIMMER DICTIONARIES
### SORT THESE DICTIONARIES BY AGE GROUP GENDER

# Array of Age Group Strokes --> SortWholeAgeGroupGender() internally uses ReOrderStrokes() --> AgeGroupGender Array
AgeGroupGender = ofunc.SortWholeAgeGroupGender(ArrOfAgeGroupStrokes)

#####################################################################
### REPLACE SWIMMER NAMES WITH TEAM NAME AND SORT INTO TEAMS

# AgeGroupGender Array --> AgeGroupWrapper() uses callback SortTeamSwimmers() --> TeamAgeGroupGender Array
TeamAgeGroupGender = ofunc.AgeGroupWrapper(AgeGroupGender,ov.SwimTeamList,ofunc.SortTeamSwimmers)

#####################################################################
### ENUMERATE BEST MEDLEY RELAY COMBINATIONS 
### ONLY USING TOP 5 SWIMMERS PER STROKE PER TEAM

# TeamAgeGroupGender Array --> AgeGroupWrapper() uses callback FillMedleyRelay() --> MedleyRelays Array
MedleyRelays = ofunc.AgeGroupWrapper(TeamAgeGroupGender,ov.SwimTeamList,ofunc.FillMedleyRelay)

#####################################################################
### BUILD FREE RELAYS WITH TOP 4 FREESTYLE TIMES

# TeamAgeGroupGender Array --> AgeGroupWrapper() uses callback FillFreeRelay() --> FreeRelays Array
FreeRelays = ofunc.AgeGroupWrapper(TeamAgeGroupGender,ov.SwimTeamList,ofunc.FillFreeRelay)

#####################################################################
### ENTER SWIMMERS INTO ONLY THEIR BEST 3 EVENTS (2 FOR 6/UNDERS)
### WE WILL EVENTUALLY ENTER EVERYONE INTO EVERY EVENT, BUT USE
### 1000 SECONDS TO REPRESENT STROKES THEY "ARENT SWIMMING"
### BEST STROKES SELECTED AS LOWEST % OF COUNTY TIMES

# TeamAgeGroupGender Array --> AgeGroupDoubleWrapper() uses callback PickEvents() --> TeamAgeGroupGender Array
TeamAgeGroupGender = ofunc.AgeGroupWrapperDoubleList(TeamAgeGroupGender,ov.CountyTimes,ofunc.PickEvents)

#####################################################################
### ACTUALLY FILL THE EVENTS AND SORT THEM FASTEST TO SLOWEST
### THIS SETS IT UP TO BE SCORED

# TeamAgeGroupGender Array --> AgeGroupWrapper() uses callback FillEvents() --> AgeGroupGenderEvents Array
AgeGroupGenderEvents = ofunc.AgeGroupWrapper(TeamAgeGroupGender,ov.SwimTeamList,ofunc.FillEvent)

#####################################################################
### SCORE THE MEET

# AgeGroupGenderEvents --> ScoreEventsWrapper() uses callback ScoreEvent() --> EventPoints and EventResults        
ofunc.ScoreEventsWrapper(AgeGroupGenderEvents, ov.ScoringScheme1, ov.SwimTeamList, ofunc.ScoreEvent)

ofunc.ScoreMedleyRelaysWrapper(FreeRelays, ov.ScoringScheme2, ov.SwimTeamList, ofunc.ScoreEvent)

ofunc.ScoreFreeRelaysWrapper(MedleyRelays, ov.ScoringScheme2, ov.SwimTeamList, ofunc.ScoreEvent)

#####################################################################
### CALCULATE POINTS PER SWIMMER

ofunc.SwimmerCountWrapper(ov.SwimmerCountJSONs,ov.SwimTeamList,ofunc.SwimmerCount)


#####################################################################
### WRITE THE OUTPUT TEXT FILE

# takes the command line arg of output pathfilename ie mockompa.py /outputfiles_2014/test.txt
file = ofunc.CreateOutPutFile()
filepathname = file
f = open(filepathname, "a")

f.write("========================================================================\n")
f.write("========================       MOCK OMPA        ========================\n")
f.write("========================================================================\n")

#####################################################################
### ENTER SWIMMERS INTO ONLY THEIR BEST 3 EVENTS (2 FOR 6/UNDERS)

### these each take the file object (f) and internally call f.write(--stuff to be outputed--)
ofunc.TeamScores(f)

ofunc.TeamScoresPerSwimmer(f)

ofunc.TeamStrokeScores(f)

ofunc.TeamMacroScores(f)

ofunc.TeamAgeGroupScores(f)

ofunc.MeetResults(f)