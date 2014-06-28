#!/usr/bin/python

# the order matters in determing the way ties are awarded points. changing the order will only change
# say a 10th 11 points and a 11th 9 points between a tie. So it only changes a total team score by a few points
SwimTeamList = ["SH","OCC","PARK","MEAD","MVP","MIRA","MCC","MRSC","CCC"]

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

CountyTimes = [
    SixUnderGirlsCounty,SixUnderBoysCounty,SevenEightGirlsCounty,SevenEightBoysCounty,NineTenGirlsCounty,NineTenBoysCounty,
    ElevenTwelveGirlsCounty,ElevenTwelveBoysCounty,ThirteenFourteenGirlsCounty,ThirteenFourteenBoysCounty,
    FifteenEighteenGirlsCounty,FifteenEighteenBoysCounty
]

# individual event scoring system
ScoringScheme1 = [24,21,20,19,18,17,16,15,14,13,11,9,8,7,6,5,4,3,2,1]

# relay event scoring system
ScoringScheme2 = [48,42,40,38,36,34,32,30,28,26,24,22,20,18,16,14,12,10,8,6]

# traditional dual meet scoring system
ScoringScheme3 = [5,3,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

# traditional dual meet relay scoring system
ScoringScheme4 = [7,3]

# JSON data from web scraper only used to calculate number of swimmers per team
# including those who are not (fast enough to be) scoring

SwimmerCountJSONs = [
    "eightunderboysfree.json",
    "eightundergirlsfree.json",
    "nineupboysfree.json",
    "nineupgirlsfree.json"
]

TeamSwimmerCount = {}

# JSON data from the web scraper
AgeGroupStrokeJSONs = [
    "sixundergirlsfree.json",
    "sixundergirlsbreast.json",
    "sixundergirlsback.json",
    "sixundergirlsfly.json",
    "sixundergirlsim.json",

    "sixunderboysfree.json",
    "sixunderboysbreast.json",
    "sixunderboysback.json",
    "sixunderboysfly.json",
    "sixunderboysim.json",

    "seveneightgirlsfree.json",
    "seveneightgirlsbreast.json",
    "seveneightgirlsback.json",
    "seveneightgirlsfly.json",
    "seveneightgirlsim.json",

    "seveneightboysfree.json",
    "seveneightboysbreast.json",
    "seveneightboysback.json",
    "seveneightboysfly.json",
   "seveneightboysim.json",

    "ninetengirlsfree.json",
    "ninetengirlsbreast.json",
    "ninetengirlsback.json",
    "ninetengirlsfly.json",
    "ninetengirlsim.json",

   "ninetenboysfree.json",
   "ninetenboysbreast.json",
    "ninetenboysback.json",
   "ninetenboysfly.json",
    "ninetenboysim.json",

    "eleventwelvegirlsfree.json",
    "eleventwelvegirlsbreast.json",
    "eleventwelvegirlsback.json",
    "eleventwelvegirlsfly.json",
    "eleventwelvegirlsim.json",

    "eleventwelveboysfree.json",
    "eleventwelveboysbreast.json",
    "eleventwelveboysback.json",
    "eleventwelveboysfly.json",
    "eleventwelveboysim.json",

    "thirteenfourteengirlsfree.json",
    "thirteenfourteengirlsbreast.json",
    "thirteenfourteengirlsback.json",
    "thirteenfourteengirlsfly.json",
    "thirteenfourteengirlsim.json",

    "thirteenfourteenboysfree.json",
    "thirteenfourteenboysbreast.json",
    "thirteenfourteenboysback.json",
    "thirteenfourteenboysfly.json",
    "thirteenfourteenboysim.json",

    "fifteeneighteengirlsfree.json",
    "fifteeneighteengirlsbreast.json",
    "fifteeneighteengirlsback.json",
    "fifteeneighteengirlsfly.json",
    "fifteeneighteengirlsim.json",

    "fifteeneighteenboysfree.json",
    "fifteeneighteenboysbreast.json",
    "fifteeneighteenboysback.json",
    "fifteeneighteenboysfly.json",
    "fifteeneighteenboysim.json",
]

EventResults = {}

EventResultsKeys = [
            'SixUnderGirls_Free', 'SixUnderGirls_Breast', 'SixUnderGirls_Back', 'SixUnderGirls_Fly', 'SixUnderGirls_IM',
    
            'SixUnderBoys_Free','SixUnderBoys_Breast','SixUnderBoys_Back','SixUnderBoys_Fly','SixUnderBoys_IM',
    
            'SevenEightGirls_Free','SevenEightGirls_Breast','SevenEightGirls_Back','SevenEightGirls_Fly','SevenEightGirls_IM',
    
            'SevenEightBoys_Free','SevenEightBoys_Breast','SevenEightBoys_Back','SevenEightBoys_Fly','SevenEightBoy_IM',
    
            'NineTenGirls_Free','NineTenGirls_Breast','NineTenGirls_Back','NineTenGirls_Fly','NineTenGirls_IM',
    
            'NineTenBoys_Free','NineTenBoys_Breast','NineTenBoys_Back','NineTenBoys_Fly','NineTenBoys_IM',
    
            'ElevenTwelveGirls_Free','ElevenTwelveGirls_Breast','ElevenTwelveGirls_Back','ElevenTwelveGirls_Fly','ElevenTwelveGirls_IM',
    
            'ElevenTwelveBoys_Free','ElevenTwelveBoys_Breast','ElevenTwelveBoys_Back','ElevenTwelveBoys_Fly','ElevenTwelveBoys_IM',
    
            'ThirteenFourteenGirls_Free','ThirteenFourteenGirls_Breast','ThirteenFourteenGirls_Back','ThirteenFourteenGirls_Fly','ThirteenFourteenGirls_IM',
    
            'ThirteenFourteenBoys_Free','ThirteenFourteenBoys_Breast','ThirteenFourteenBoys_Back','ThirteenFourteenBoys_Fly','ThirteenFourteenBoys_IM',
    
            'FifteenEighteenGirls_Free','FifteenEighteenGirls_Breast','FifteenEighteenGirls_Back','FifteenEighteenGirls_Fly','FifteenEighteenGirls_IM',
    
            'FifteenEighteenBoys_Free','FifteenEighteenBoys_Breast','FifteenEighteenBoys_Back','FifteenEighteenBoys_Fly','FifteenEighteenBoys_IM'
    ]

FreeRelayResultsKeys = [
    
    'SixUnderGirls_FreeRelay','SixUnderBoys_FreeRelay','SevenEightGirls_FreeRelay','SevenEightBoys_FreeRelay',
    'NineTenGirls_FreeRelay','NineTenBoys_FreeRelay','ElevenTwelveGirls_FreeRelay','ElevenTwelveBoys_FreeRelay',
    'ThirteenFourteenGirls_FreeRelay','ThirteenFourteenBoys_FreeRelay',
    'FifteenEighteenGirls_FreeRelay','FifteenEighteenBoys_FreeRelay'
]

MedleyRelayResultsKeys = [

    'SixUnderGirls_MedleyRelay','SixUnderBoys_MedleyRelay','SevenEightGirls_MedleyRelay','SevenEightBoys_MedleyRelay',
    'NineTenGirls_MedleyRelay','NineTenBoys_MedleyRelay','ElevenTwelveGirls_MedleyRelay','ElevenTwelveBoys_MedleyRelay',
    'ThirteenFourteenGirls_MedleyRelay','ThirteenFourteenBoys_MedleyRelay',
    'FifteenEighteenGirls_MedleyRelay','FifteenEighteenBoys_MedleyRelay'
    
]

EventPoints = {}

AgeGroupPointsKeys = [
    "SixUnderGirls","SixUnderBoys","SevenEightGirls","SevenEightBoys","NineTenGirls","NineTenBoys",
    "ElevenTwelveGirls","ElevenTwelveBoys","ThirteenFourteenGirls","ThirteenFourteenBoys",
    "FifteenEighteenGirls","FifteenEighteenBoys"
]

AgeGroupPoints = {}
