#!/usr/bin/python

# MockOMPA
# Uses: 
# <> fully quantified knowlegde of team strengths and weaknesses
# <> program runnable at any time of the season, good for tracking team improvemts
# <> just for fun, the total scores can be like the BCS of OMPA swimming
# code written and designed by Nick Stefan copyright 2014
# all of the preset variables to be imported into MockOMPA

# the order matters in determing the way ties are awarded points. changing the order will only change
# say a 10th 11 points and a 11th 9 points between a tie. So it only changes a total team score by a few points
SwimTeamList = ["SH","OCC","PARK","MEAD","MVP","MIRA","MCC","MRSC","CCC"]

# point totals for each age group
SixUnderGirls_Points = {}
SixUnderBoys_Points = {}
SevenEightGirls_Points = {}
SevenEightBoys_Points = {}
NineTenGirls_Points = {}
NineTenBoys_Points = {}
ElevenTwelveGirls_Points = {}
ElevenTwelveBoys_Points = {}
ThirteenFourteenGirls_Points = {}
ThirteenFourteenBoys_Points = {}
FifteenEighteenGirls_Points = {}
FifteenEighteenBoys_Points = {}

# point totals for each age group each stroke
SixUnderGirls_Free_Points = {}
SixUnderGirls_Breast_Points = {}
SixUnderGirls_Back_Points = {}
SixUnderGirls_Fly_Points = {}
SixUnderGirls_IM_Points = {}

SixUnderBoys_Free_Points = {}
SixUnderBoys_Breast_Points = {}
SixUnderBoys_Back_Points = {}
SixUnderBoys_Fly_Points = {}
SixUnderBoys_IM_Points = {}

SevenEightGirls_Free_Points = {}
SevenEightGirls_Breast_Points = {}
SevenEightGirls_Back_Points = {}
SevenEightGirls_Fly_Points = {}
SevenEightGirls_IM_Points = {}

SevenEightBoys_Free_Points = {}
SevenEightBoys_Breast_Points = {}
SevenEightBoys_Back_Points = {}
SevenEightBoys_Fly_Points = {}
SevenEightBoys_IM_Points = {}

NineTenGirls_Free_Points = {}
NineTenGirls_Breast_Points = {}
NineTenGirls_Back_Points = {}
NineTenGirls_Fly_Points = {}
NineTenGirls_IM_Points = {}

NineTenBoys_Free_Points = {}
NineTenBoys_Breast_Points = {}
NineTenBoys_Back_Points = {}
NineTenBoys_Fly_Points = {}
NineTenBoys_IM_Points = {}

ElevenTwelveGirls_Free_Points = {}
ElevenTwelveGirls_Breast_Points = {}
ElevenTwelveGirls_Back_Points = {}
ElevenTwelveGirls_Fly_Points = {}
ElevenTwelveGirls_IM_Points = {}

ElevenTwelveBoys_Free_Points = {}
ElevenTwelveBoys_Breast_Points = {}
ElevenTwelveBoys_Back_Points = {}
ElevenTwelveBoys_Fly_Points = {}
ElevenTwelveBoys_IM_Points = {}

ThirteenFourteenGirls_Free_Points = {}
ThirteenFourteenGirls_Breast_Points = {}
ThirteenFourteenGirls_Back_Points = {}
ThirteenFourteenGirls_Fly_Points = {}
ThirteenFourteenGirls_IM_Points = {}

ThirteenFourteenBoys_Free_Points = {}
ThirteenFourteenBoys_Breast_Points = {}
ThirteenFourteenBoys_Back_Points = {}
ThirteenFourteenBoys_Fly_Points = {}
ThirteenFourteenBoys_IM_Points = {}

FifteenEighteenGirls_Free_Points = {}
FifteenEighteenGirls_Breast_Points = {}
FifteenEighteenGirls_Back_Points = {}
FifteenEighteenGirls_Fly_Points = {}
FifteenEighteenGirls_IM_Points = {}

FifteenEighteenBoys_Free_Points = {}
FifteenEighteenBoys_Breast_Points = {}
FifteenEighteenBoys_Back_Points = {}
FifteenEighteenBoys_Fly_Points = {}
FifteenEighteenBoys_IM_Points = {}

# relay points
SixUnderGirls_MedRelay_Points = {}
SixUnderBoys_MedRelay_Points = {}
SevenEightGirls_MedRelay_Points = {}
SevenEightBoys_MedRelay_Points = {}
NineTenGirls_MedRelay_Points = {}
NineTenBoys_MedRelay_Points = {}
ElevenTwelveGirls_MedRelay_Points = {}
ElevenTwelveBoys_MedRelay_Points = {}
ThirteenFourteenGirls_MedRelay_Points = {}
ThirteenFourteenBoys_MedRelay_Points = {}
FifteenEighteenGirls_MedRelay_Points = {}
FifteenEighteenBoys_MedRelay_Points = {}

SixUnderGirls_FreeRelay_Points = {}
SixUnderBoys_FreeRelay_Points = {}
SevenEightGirls_FreeRelay_Points = {}
SevenEightBoys_FreeRelay_Points = {}
NineTenGirls_FreeRelay_Points = {}
NineTenBoys_FreeRelay_Points = {}
ElevenTwelveGirls_FreeRelay_Points = {}
ElevenTwelveBoys_FreeRelay_Points = {}
ThirteenFourteenGirls_FreeRelay_Points = {}
ThirteenFourteenBoys_FreeRelay_Points = {}
FifteenEighteenGirls_FreeRelay_Points = {}
FifteenEighteenBoys_FreeRelay_Points = {}

TotalFreeRelay_Points = []

# 2014 county times
SixUnderGirlsCounty = {"FreeCounty": 20.88, "BreastCounty": 29.21, "BackCounty": 25.95, "FlyCounty": 25.37, "IMCounty": 10000.00}
SixUnderBoysCounty = {"FreeCounty": 20.59, "BreastCounty": 29.14, "BackCounty": 25.74, "FlyCounty": 25.95, "IMCounty": 10000.00}
SevenEightGirlsCounty = {"FreeCounty": 16.44, "BreastCounty": 22.10, "BackCounty": 20.69, "FlyCounty": 18.18, "IMCounty": 97.9}
SevenEightBoysCounty = {"FreeCounty": 16.00, "BreastCounty": 22.22, "BackCounty": 20.35, "FlyCounty": 18.58, "IMCounty": 97.40}
NineTenGirlsCounty = {"FreeCounty": 31.68, "BreastCounty": 41.28, "BackCounty": 38.33, "FlyCounty": 36.6, "IMCounty": 83.10}
NineTenBoysCounty = {"FreeCounty": 31.60, "BreastCounty": 42.10, "BackCounty": 38.53, "FlyCounty": 37.08, "IMCounty": 83.70}
ElevenTwelveGirlsCounty = {"FreeCounty": 28.97, "BreastCounty": 37.61, "BackCounty": 34.66, "FlyCounty": 32.29, "IMCounty": 75.34}
ElevenTwelveBoysCounty = {"FreeCounty": 28.28, "BreastCounty": 37.45, "BackCounty": 35.04, "FlyCounty": 32.56, "IMCounty": 74.80}
ThirteenFourteenGirlsCounty = {"FreeCounty": 27.78, "BreastCounty": 35.93, "BackCounty": 32.57, "FlyCounty": 30.82, "IMCounty": 71.90}
ThirteenFourteenBoysCounty = {"FreeCounty": 25.88, "BreastCounty": 33.49, "BackCounty": 31.69, "FlyCounty": 28.99, "IMCounty": 67.73}
FifteenEighteenGirlsCounty = {"FreeCounty": 26.99, "BreastCounty": 34.99, "BackCounty": 31.50, "FlyCounty": 30.25, "IMCounty": 68.50}
FifteenEighteenBoysCounty = {"FreeCounty": 23.99, "BreastCounty": 31.39, "BackCounty": 29.10, "FlyCounty": 26.75, "IMCounty": 61.70}

# individual event scoring system
ScoringScheme1 = [24,21,20,19,18,17,16,15,14,13,11,9,8,7,6,5,4,3,2,1]

# relay event scoring system
ScoringScheme2 = [48,42,40,38,36,34,32,30,28,26,24,22,20,18,16,14,12,10,8,6]

# traditional dual meet scoring system
ScoringScheme3 = [5,3,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

# traditional dual meet relay scoring system
ScoringScheme4 = [7,3]