
# swimmer lists begin empty before sorting the data
SH_Swimmer6UGirlsList = []
OCC_Swimmer6UGirlsList = []
OPP_Swimmer6UGirlsList = []
MEAD_Swimmer6UGirlsList = []
MVP_Swimmer6UGirlsList = []
MIRA_Swimmer6UGirlsList = []
MCC_Swimmer6UGirlsList = []
MRSC_Swimmer6UGirlsList = []
CCC_Swimmer6UGirlsList = []

SH_Swimmer78BoysList = []
OCC_Swimmer78BoysList = []
OPP_Swimmer78BoysList = []
MEAD_Swimmer78BoysList = []
MVP_Swimmer78BoysList = []
MIRA_Swimmer78BoysList = []
MCC_Swimmer78BoysList = []
MRSC_Swimmer78BoysList = []
CCC_Swimmer78BoysList = []

# point totals for each age group
SixUnderGirls_Points = {}
SevenEightBoys_Points = {}

# point totals for each age group each stroke
SixUnderGirls_Free_Points = {}
SixUnderGirls_Fly_Points = {}

SevenEightBoys_Free_Points = {}
SevenEightBoys_Fly_Points = {}

# age group stroke gender events
SixUnderGirls_Free_Event = []
SixUnderGirls_Fly_Event = []

SevenEightBoys_Free_Event = []
SevenEightBoys_Fly_Event = []

# 2013 county times
SixUnderGirlsCounty = {"FreeCounty": 20.48, "BreastCounty": 28.81, "BackCounty": 25.75, "FlyCounty": 24.87, "IMCounty": 1.00}
SevenEightBoysCounty = {"FreeCounty": 16.00, "BreastCounty": 22.22, "BackCounty": 20.35, "FlyCounty": 18.58, "IMCounty": 97.44}

# scoring system to be used
ScoringScheme1 = [24,21,20,19,18,17,16,15,14,13,11,9,8,7,6,5,4,3,2,1]
ScoringScheme2 = [48,42,40,38,36,34,32,30,28,26]

#Example data that would come from the bots. Each stroke is in the SAME order of the names!
#Need a solution of how to get the bots to do this...excel???

# IMPORTANT: CANNOT HAVE DUPLICATE NAMES HERE. DUPLICATE WILL ENTER THE FIRST ONE OVER THE SECOND AND
# DOUBLES THE SCORE OF THE FIRST BY ENTERING IT TWICE
SixUnderGirls = ["Mary S", "Suzie J", "Sarah S", "Jozie Q", "Rosie R", 
"Berta M", "Mary A", "Lindsay k", "Jordan S", "Lucy F", "Kelly M", "Josie U", 
"Remy E", "Monica E", "Gladys Y", "Maddie S", "Katie G", "Lisa F", "Eliza G", "Erica H",
"Suzie","Tammy","Amy", "Kylie", "Ramona", "Tiffany", "Ronda", "Barbara", "Gladys", "Joelle",
"Swim1","Swim2","Swim3","Swim4","Swim5","swim6","swim7","swim8","swim9","swim10","swim11","swim12","swim13",
"swim14","swim15","swim16","swim17","swim18","swim19","swim20","swim21","swim22","swim23","swim24","swim25"]

SixUnderGirls_Teams = ["MCC", "SH", "MCC", "OPP", "OPP", "OPP", "MCC", "OCC", "SH", "OPP", 
"MCC", "SH", "OCC", "SH", "OCC", "OCC", "MCC", "SH","OPP", "OCC",
"OCC","SH","OPP","MCC","OCC","SH","OPP","MCC","OPP","MCC",
"MEAD","MEAD","MEAD","MEAD","MEAD","MVP","MVP","MVP","MVP","MVP","MIRA","MIRA","MIRA","MIRA","MIRA",
"MRSC","MRSC","MRSC","MRSC","MRSC","CCC","CCC","CCC","CCC","CCC"]

# IMPORTANT: EVERY SWIMMER MUST HAVE A TIME. AN EMPTY SWIM TIME CRASHES
SixUnderGirls_Free = [15.2, 15.45, 15.85, 16, 16.05, 16.85, 16.91, 17.00, 17.5, 17.91, 
18.00, 18.5, 18.9, 18.99, 19.55, 21.87, 30.00, 25.00, 26.00, 27,
16.02,16.67,16.32,16.81,17.1,15.01,14.8,14.7,14.85,15.00,
15.13,14.52,15.23,15.235,15.53,14.75,16.24,16.62,16.74,17.75,18.24,15.52,16.53,17.74,15.63,14.35,
15.24,16.24,17.13,16.13,15.41,16.41,17.52,15.54,19.43]

SixUnderGirls_Breast = [25,23.3,21.00,22,35,28,23,19,25,23,26,22,28,23,23.43,23.12,33,
25.01,24.99,25.01,24,23,21,25,26.7,23.5,24.8,24.88,24.87,24,
24.213,21.42,20.23,19.12,18.21,18.34,19.34,20.53,21.65,22.56,23.76,24.45,25.87,24.43,23.64,23.46,
21.23,20.64,21.67,22.35,19.76,18.23,23.76,24.63,25.90]

SixUnderGirls_Back = [21.00, 20.01, 21.00,20,19,18,23,22.3,24.5,28.1,25.01,25,25.00,29,23,
20.5,30,23.4,22.99,28,18.9,19,19.01,19.05,20.4,24.5,28.1,25.01,26.09,23.01,
17.34,18.454,18.45,17.56,18.77,19.22,20.45,20.37,
22.73,21.345,20.456,19.34,18.74,17.34,19.63,20.34,19.34,18.67,21.64,22,23.123,21.235,20.123,21.23,21.42,20.65]

SixUnderGirls_Fly = [18.9, 18.91, 18,99,16.9,18.05,19,20,21,22,23,22,21,20,18,19,37,22.01,
22,21.05,16.01,16.01,16.02,16.05,17,18,17.03,18,19,20,17,
15.25,16.512,15.654,14.57,15.75,16.46,15.246,16.56,17.75,18.345,15.24,19.24,17.63,18.63,15.73,16.36,17.52,19.36,18.74,
19.74,16.25,17.63,19.74,16.75,17.35]

SixUnderGirls_IM = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

# IMPORTANT: CANNOT HAVE DUPLICATE NAMES HERE. DUPLICATE WILL ENTER THE FIRST ONE OVER THE SECOND AND
# DOUBLES THE SCORE OF THE FIRST BY ENTERING IT TWICE
SevenEightBoys = ["Bob","Joey","Tim R","Jon","Swimmer","Tim F","TimA","Swimmer1","Swimmer2","Swimmer3",
"Swimmer4","Swimmer5","Swimmer6","Swimmer7","Swimmer8","Swimmer9","Swimmer10","Swimmer11","Swimmer12","Swimmer13",
"Swim1","Swim2","Swim3","Swim4","Swim5","swim6","swim7","swim8","swim9","swim10","swim11","swim12","swim13",
"swim14","swim15","swim16","swim17","swim18","swim19","swim20","swim21","swim22","swim23","swim24","swim25"]

SevenEightBoys_Teams = ["MCC", "SH", "OPP","OCC","SH","OCC","OPP","MCC","OPP","MCC","SH","OPP","OPP","MCC","SH",
"MCC","OCC","SH","OCC","OCC",
"MEAD","MEAD","MEAD","MEAD","MEAD","MVP","MVP","MVP","MVP","MVP","MIRA","MIRA","MIRA","MIRA","MIRA",
"MRSC","MRSC","MRSC","MRSC","MRSC","CCC","CCC","CCC","CCC","CCC"]

# IMPORTANT: EVERY SWIMMER MUST HAVE A TIME. AN EMPTY SWIM TIME CRASHES
SevenEightBoys_Free = [14.12,14.30,14.65,14.56,14.01,15.11,15.10,15.29,15.92,15.83,16.34,16.04,16.02,
16.09,17.34,17.22,16.20,15.24,17.63,15.34,
15.13,14.52,15.23,15.235,15.53,14.75,16.24,16.62,16.74,17.75,18.24,15.52,16.53,17.74,15.63,14.35,
15.24,16.24,17.13,16.13,15.41,16.41,17.52,15.54,19.43]

SevenEightBoys_Breast = [18.99,18.76,19.55,19.66,19.77,20.62,21.23,21.89,20.23,19.53,23.02,24.09,
24.79,24.52,24.50,25.43,18.32,19.10,20.34,21.9,
24.213,21.42,20.23,19.12,18.21,18.34,19.34,20.53,21.65,22.56,23.76,24.45,25.87,24.43,23.64,23.46,
21.23,20.64,21.67,22.35,19.76,18.23,23.76,24.63,25.90]

SevenEightBoys_Back = [17.09,17.10,17.11,17.22,17.87,18.45,18.43,18.89,18.78,19.22,19.66,20.33,
20.23,20.63,20.32,21.87,21.76,21.34,20.65,19.23,
17.34,18.454,18.45,17.56,18.77,19.22,20.45,20.37,
22.73,21.345,20.456,19.34,18.74,17.34,19.63,20.34,19.34,18.67,21.64,22,23.123,21.235,20.123,
20.56,17.76,18.51,19.12,20.23,23.42,20.52,19.23,18.22,20.51,22.23,23.34]

SevenEightBoys_Fly = [15.30,16.53,17.56,18.76,14.67,20,21.08,20.90,20.09,19.16,17.26,18.23,15.32,18.23,19.52,15.25,
16.65,17.23,18.45,16.47,
15.25,16.512,15.654,14.57,15.75,16.46,15.246,16.56,17.75,18.345,15.24,19.24,17.63,18.63,15.73,16.36,17.52,19.36,18.74,
19.74,16.25,17.63,19.74,16.75,17.35]

SevenEightBoys_IM = [100.02,101.01,102.04,104.09,100,94,98,91,90,100,120,110,111,113,101,103.2,102.5,103.8,104.9,100.1,
105.234,106.524,107.234,108.23,109.524,110.25,111.51,112.42,108.24,103.52,108.63,108.75,103.57,101.46,102.35,100.24,
103.13,106.63,109.57,110.75,111.75,112.64,109.13,103.22,101.525]

#Load the swimmers Free, Breast, Back, Fly times into the correct team swimmer list

#AgeGroup = ie SixUnderGirls, AgeGroupTeam = ie SixUnderGirls_Teams (list of teams),AgeGroupFree = ie SixUnderGirls_Free, OPP = ie #OPP_Swimmer6UGirlsList
def SortTeamSwimmers(AgeGroup,AgeGroupTeams,AgeGroupFree,AgeGroupBreast,AgeGroupBack,AgeGroupFly,AgeGroupIM,SH,OCC,OPP,MEAD,MVP,MIRA,MCC,MRSC,CCC):
    #for each swimmername in the list
    for swimmer in AgeGroup:
        #index rank of each swimmer name
        swimmerID = AgeGroup.index(swimmer)
        
        #SH
        if AgeGroupTeams[swimmerID] == "SH":
             SH.append({"Free":AgeGroupFree[swimmerID],
             "Breast":AgeGroupBreast[swimmerID],"Back":AgeGroupBack[swimmerID],
             "Fly":AgeGroupFly[swimmerID],"IM":AgeGroupIM[swimmerID]})
        # OCC
        elif AgeGroupTeams[swimmerID] == "OCC":
             OCC.append({"Free":AgeGroupFree[swimmerID],
             "Breast":AgeGroupBreast[swimmerID],"Back":AgeGroupBack[swimmerID],
             "Fly":AgeGroupFly[swimmerID],"IM":AgeGroupIM[swimmerID]})
        # OPP
        elif AgeGroupTeams[swimmerID] == "OPP":
             OPP.append({"Free":AgeGroupFree[swimmerID],
             "Breast":AgeGroupBreast[swimmerID],"Back":AgeGroupBack[swimmerID],
             "Fly":AgeGroupFly[swimmerID],"IM":AgeGroupIM[swimmerID]})
        # MEAD
        elif AgeGroupTeams[swimmerID] == "MEAD":
             MEAD.append({"Free":AgeGroupFree[swimmerID],
             "Breast":AgeGroupBreast[swimmerID],"Back":AgeGroupBack[swimmerID],
             "Fly":AgeGroupFly[swimmerID],"IM":AgeGroupIM[swimmerID]})
        # MVP
        elif AgeGroupTeams[swimmerID] == "MVP":
             MVP.append({"Free":AgeGroupFree[swimmerID],
             "Breast":AgeGroupBreast[swimmerID],"Back":AgeGroupBack[swimmerID],
             "Fly":AgeGroupFly[swimmerID],"IM":AgeGroupIM[swimmerID]})
        # MIRA
        elif AgeGroupTeams[swimmerID] == "MIRA":
             MIRA.append({"Free":AgeGroupFree[swimmerID],
             "Breast":AgeGroupBreast[swimmerID],"Back":AgeGroupBack[swimmerID],
             "Fly":AgeGroupFly[swimmerID],"IM":AgeGroupIM[swimmerID]})
        # MCC
        elif AgeGroupTeams[swimmerID] == "MCC":
             MCC.append({"Free":AgeGroupFree[swimmerID],
             "Breast":AgeGroupBreast[swimmerID],"Back":AgeGroupBack[swimmerID],
             "Fly":AgeGroupFly[swimmerID],"IM":AgeGroupIM[swimmerID]})
        # MRSC
        elif AgeGroupTeams[swimmerID] == "MRSC":
             MRSC.append({"Free":AgeGroupFree[swimmerID],
             "Breast":AgeGroupBreast[swimmerID],"Back":AgeGroupBack[swimmerID],
             "Fly":AgeGroupFly[swimmerID],"IM":AgeGroupIM[swimmerID]})
        # CCC
        elif AgeGroupTeams[swimmerID] == "CCC":
             CCC.append({"Free":AgeGroupFree[swimmerID],
             "Breast":AgeGroupBreast[swimmerID],"Back":AgeGroupBack[swimmerID],
             "Fly":AgeGroupFly[swimmerID],"IM":AgeGroupIM[swimmerID]})
    return 

#use the function

SortTeamSwimmers(SixUnderGirls,SixUnderGirls_Teams,SixUnderGirls_Free,SixUnderGirls_Breast,SixUnderGirls_Back,SixUnderGirls_Fly,SixUnderGirls_IM,
SH_Swimmer6UGirlsList,OCC_Swimmer6UGirlsList,OPP_Swimmer6UGirlsList,MEAD_Swimmer6UGirlsList,MVP_Swimmer6UGirlsList,MIRA_Swimmer6UGirlsList, 
MCC_Swimmer6UGirlsList,MRSC_Swimmer6UGirlsList,CCC_Swimmer6UGirlsList)

SortTeamSwimmers(SevenEightBoys,SevenEightBoys_Teams,SevenEightBoys_Free,SevenEightBoys_Breast,SevenEightBoys_Back,SevenEightBoys_Fly,SevenEightBoys_IM,
SH_Swimmer78BoysList,OCC_Swimmer78BoysList,OPP_Swimmer78BoysList,MEAD_Swimmer78BoysList,MVP_Swimmer78BoysList,MIRA_Swimmer78BoysList, 
MCC_Swimmer78BoysList,MRSC_Swimmer78BoysList,CCC_Swimmer78BoysList)

print "========================"
print "6/under swimmer lists"
print "========================"
print "SH List"
print SH_Swimmer6UGirlsList
print "========================"
print "OCC List"
print OCC_Swimmer6UGirlsList
print "========================"
print "OPP List"
print OPP_Swimmer6UGirlsList
print "========================"
print "MEAD List"
print MEAD_Swimmer6UGirlsList
print "========================"
print "MVP List"
print MVP_Swimmer6UGirlsList
print "========================"
print "MIRA List"
print MIRA_Swimmer6UGirlsList
print "========================"
print "MCC List"
print MCC_Swimmer6UGirlsList
print "========================"
print "MRSC List"
print MRSC_Swimmer6UGirlsList
print "========================"
print "CCC List"
print CCC_Swimmer6UGirlsList
print "========================"

print "========================"
print "7/8 swimmer lists"
print "========================"
print "SH List"
print SH_Swimmer78BoysList
print "========================"
print "OCC List"
print OCC_Swimmer78BoysList
print "========================"
print "OPP List"
print OPP_Swimmer78BoysList
print "========================"
print "MEAD List"
print MEAD_Swimmer78BoysList
print "========================"
print "MVP List"
print MVP_Swimmer78BoysList
print "========================"
print "MIRA List"
print MIRA_Swimmer78BoysList
print "========================"
print "MCC List"
print MCC_Swimmer78BoysList
print "========================"
print "MRSC List"
print MRSC_Swimmer78BoysList
print "========================"
print "CCC List"
print CCC_Swimmer78BoysList
print "========================"

# We will enter every swimmer into every event, but "simulate" only swimming the OMPA allowed number of events
# by changing their "worst" strokes into 1000 seconds (ie last place and no points for those events)
# we will select "worst" strokes by dividing each stroke by the county time. the largest numbers are "worst"
# need to make sure that the "division" process only permanently effects the bad strokes

def PickEvents(swimmerlist,countylist):
    for swimmerdict in swimmerlist:
        fly = swimmerdict["Fly"]
        back = swimmerdict["Back"]
        breast = swimmerdict["Breast"]
        free = swimmerdict["Free"]
        IM = swimmerdict["IM"]
        
        flytest = float((fly / countylist["FlyCounty"]))
        backtest = float((back / countylist["BackCounty"]))
        breasttest = float((breast / countylist["BreastCounty"]))
        freetest = float((free / countylist["FreeCounty"]))
        imtest = float((IM / countylist["IMCounty"]))
        
        # fly, back, breast, free, im
        if flytest > backtest and backtest > breasttest and breasttest > freetest and freetest > imtest:
            del swimmerdict["Fly"]
            del swimmerdict["Back"]
            swimmerdict["Fly"] = 1000
            swimmerdict["Back"] = 1000
        # fly, back, breast, im, free
        elif flytest > backtest and backtest > breasttest and breasttest > imtest and imtest > freetest:
            del swimmerdict["Fly"]
            del swimmerdict["Back"]
            swimmerdict["Fly"] = 1000
            swimmerdict["Back"] = 1000
        # fly, back, free, breast, im
        elif flytest > backtest and backtest > freetest and freetest > breasttest and breasttest > imtest:
            del swimmerdict["Fly"]
            del swimmerdict["Back"]
            swimmerdict["Fly"] = 1000
            swimmerdict["Back"] = 1000
        # fly, back, free, im, breast
        elif flytest > backtest and backtest > freetest and freetest > imtest and imtest > breasttest:
            del swimmerdict["Fly"]
            del swimmerdict["Back"]
            swimmerdict["Fly"] = 1000
            swimmerdict["Back"] = 1000
        # fly, back, im, breast, free
        elif flytest > backtest and backtest > imtest and imtest > breasttest and breasttest > freetest:
            del swimmerdict["Fly"]
            del swimmerdict["Back"]
            swimmerdict["Fly"] = 1000
            swimmerdict["Back"] = 1000
        # fly, back, im, free, breast
        elif flytest > backtest and backtest > imtest and imtest > freetest and freetest > breasttest:
            del swimmerdict["Fly"]
            del swimmerdict["Back"]
            swimmerdict["Fly"] = 1000
            swimmerdict["Back"] = 1000
            
            
        # fly, breast, back, free, im
        elif flytest > breasttest and breasttest > backtest and backtest > freetest and freetest > imtest:
            del swimmerdict["Fly"]
            del swimmerdict["Breast"]
            swimmerdict["Fly"] = 1000
            swimmerdict["Breast"] = 1000       
        # fly, breast, back, im, free
        elif flytest > breasttest and breasttest > backtest and backtest > imtest and imtest > freetest:
            del swimmerdict["Fly"]
            del swimmerdict["Breast"]
            swimmerdict["Fly"] = 1000
            swimmerdict["Breast"] = 1000
        # fly, breast, free, back, im
        elif flytest > breasttest and breasttest > freetest and freetest > backtest and backtest > imtest:
            del swimmerdict["Fly"]
            del swimmerdict["Breast"]
            swimmerdict["Fly"] = 1000
            swimmerdict["Breast"] = 1000        
        # fly, breast, free, im, back
        elif flytest > breasttest and breasttest > freetest and freetest > imtest and imtest > backtest:
            del swimmerdict["Fly"]
            del swimmerdict["Breast"]
            swimmerdict["Fly"] = 1000
            swimmerdict["Breast"] = 1000
        # fly, breast, im, free, back
        elif flytest > breasttest and breasttest > imtest and imtest > freetest and freetest > backtest:
            del swimmerdict["Fly"]
            del swimmerdict["Breast"]
            swimmerdict["Fly"] = 1000
            swimmerdict["Breast"] = 1000
        # fly, breast, im, back, free
        elif flytest > breasttest and breasttest > imtest and imtest > backtest and backtest > freetest:
            del swimmerdict["Fly"]
            del swimmerdict["Breast"]
            swimmerdict["Fly"] = 1000
            swimmerdict["Breast"] = 1000
            
            
        # fly, free, breast, back, im
        elif flytest > freetest and freetest > breasttest and breasttest > backtest and backtest > imtest:
            del swimmerdict["Fly"]
            del swimmerdict["Free"]
            swimmerdict["Fly"] = 1000
            swimmerdict["Free"] = 1000            
        # fly, free, breast, im, back
        elif flytest > freetest and freetest > breasttest and breasttest > imtest and imtest > backtest:
            del swimmerdict["Fly"]
            del swimmerdict["Free"]
            swimmerdict["Fly"] = 1000
            swimmerdict["Free"] = 1000     
        # fly, free, back, breast, im
        elif flytest > freetest and freetest > backtest and backtest > breasttest and breasttest > imtest:
            del swimmerdict["Fly"]
            del swimmerdict["Free"]
            swimmerdict["Fly"] = 1000
            swimmerdict["Free"] = 1000
        # fly, free, back, im, breast
        elif flytest > freetest and freetest > backtest and backtest > imtest and imtest > breasttest:
            del swimmerdict["Fly"]
            del swimmerdict["Free"]
            swimmerdict["Fly"] = 1000
            swimmerdict["Free"] = 1000
        # fly, free, im, back, breast
        elif flytest > freetest and freetest > imtest and imtest > backtest and backtest > breasttest:
            del swimmerdict["Fly"]
            del swimmerdict["Free"]
            swimmerdict["Fly"] = 1000
            swimmerdict["Free"] = 1000
        # fly, free, im, breast, back
        elif flytest > freetest and freetest > imtest and imtest > breasttest and breasttest > backtest:
           del swimmerdict["Fly"]
           del swimmerdict["Free"]
           swimmerdict["Fly"] = 1000
           swimmerdict["Free"] = 1000
           
           
        # fly, im, back, breast, free
        elif flytest > imtest and imtest > backtest and backtest > breasttest and breasttest > freetest:
            del swimmerdict["Fly"]
            del swimmerdict["IM"]
            swimmerdict["Fly"] = 1000
            swimmerdict["IM"] = 1000
        # fly, im, back, free, breast
        elif flytest > imtest and imtest > backtest and backtest > freetest and freetest > breasttest:
            del swimmerdict["Fly"]
            del swimmerdict["IM"]
            swimmerdict["Fly"] = 1000
            swimmerdict["IM"] = 1000
        # fly, im, breast, free, back
        elif flytest > imtest and imtest > breasttest and breasttest > freetest and freetest > backtest:
            del swimmerdict["Fly"]
            del swimmerdict["IM"]
            swimmerdict["Fly"] = 1000
            swimmerdict["IM"] = 1000
        # fly, im, breast, back, free
        elif flytest > imtest and imtest > breasttest and breasttest > backtest and backtest > freetest:
            del swimmerdict["Fly"]
            del swimmerdict["IM"]
            swimmerdict["Fly"] = 1000
            swimmerdict["IM"] = 1000
        # fly, im, free, back, breast
        elif flytest > imtest and imtest > freetest and freetest > backtest and backtest > breasttest:
            del swimmerdict["Fly"]
            del swimmerdict["IM"]
            swimmerdict["Fly"] = 1000
            swimmerdict["IM"] = 1000
        # fly, im, free, breast, back
        elif flytest > imtest and imtest > freetest and freetest > breasttest and breasttest > backtest:
            del swimmerdict["Fly"]
            del swimmerdict["IM"]
            swimmerdict["Fly"] = 1000
            swimmerdict["IM"] = 1000
            
            
        # back, fly, free, breast, im
        elif backtest > flytest and flytest > freetest and freetest > breasttest and breasttest > imtest:
            del swimmerdict["Back"]
            del swimmerdict["Fly"]
            swimmerdict["Back"] = 1000
            swimmerdict["Fly"] = 1000
        # back, fly, free, im, breast
        elif backtest > flytest and flytest > freetest and freetest > imtest and imtest > breasttest:
            del swimmerdict["Back"]
            del swimmerdict["Fly"]
            swimmerdict["Back"] = 1000
            swimmerdict["Fly"] = 1000
        # back, fly, breast, free, im
        elif backtest > flytest and flytest > breasttest and breasttest > freetest and freetest > imtest:
            del swimmerdict["Back"]
            del swimmerdict["Fly"]
            swimmerdict["Back"] = 1000
            swimmerdict["Fly"] = 1000
        # back, fly, breast, im, free
        elif backtest > flytest and flytest > breasttest and breasttest > imtest and imtest > freetest:
            del swimmerdict["Back"]
            del swimmerdict["Fly"]
            swimmerdict["Back"] = 1000
            swimmerdict["Fly"] = 1000
        # back, fly, im, breast, free
        elif backtest > flytest and flytest > imtest and imtest > breasttest and breasttest > freetest:
            del swimmerdict["Back"]
            del swimmerdict["Fly"]
            swimmerdict["Back"] = 1000
            swimmerdict["Fly"] = 1000
        # back, fly, im, free, breast
        elif backtest > flytest and flytest > imtest and imtest > freetest and freetest > breasttest:
            del swimmerdict["Back"]
            del swimmerdict["Fly"]
            swimmerdict["Back"] = 1000
            swimmerdict["Fly"] = 1000
            

        # back, breast, free, fly, im
        elif backtest > breasttest and breasttest > freetest and freetest > flytest and flytest > imtest:
            del swimmerdict["Back"]
            del swimmerdict["Breast"]
            swimmerdict["Back"] = 1000
            swimmerdict["Breast"] = 1000
        # back, breast, free, im, fly
        elif backtest > breasttest and breasttest > freetest and freetest > imtest and imtest > flytest:
            del swimmerdict["Back"]
            del swimmerdict["Breast"]
            swimmerdict["Back"] = 1000
            swimmerdict["Breast"] = 1000
        # back, breast, fly, free, im
        elif backtest > breasttest and breasttest > flytest and flytest > freetest and freetest > imtest:
            del swimmerdict["Back"]
            del swimmerdict["Breast"]
            swimmerdict["Back"] = 1000
            swimmerdict["Breast"] = 1000
        # back, breast, fly, im, free
        elif backtest > breasttest and breasttest > flytest and flytest > imtest and imtest > freetest:
            del swimmerdict["Back"]
            del swimmerdict["Breast"]
            swimmerdict["Back"] = 1000
            swimmerdict["Breast"] = 1000
        # back, breast, im, free, fly
        elif backtest > breasttest and breasttest > imtest and imtest > freetest and freetest > flytest:
            del swimmerdict["Back"]
            del swimmerdict["Breast"]
            swimmerdict["Back"] = 1000
            swimmerdict["Breast"] = 1000
        # back, breast, im, fly, free
        elif backtest > breasttest and breasttest > imtest and imtest > flytest and flytest > freetest:
            del swimmerdict["Back"]
            del swimmerdict["Breast"]
            swimmerdict["Back"] = 1000
            swimmerdict["Breast"] = 1000
 
        # back, free, fly, breast, im
        elif backtest > freetest and freetest > flytest and flytest > breasttest and breasttest > imtest:
            del swimmerdict["Back"]
            del swimmerdict["Free"]
            swimmerdict["Back"] = 1000
            swimmerdict["Free"] = 1000
        # back, free, fly, im, breast
        elif backtest > freetest and freetest > flytest and flytest > imtest and imtest > breasttest:
            del swimmerdict["Back"]
            del swimmerdict["Free"]
            swimmerdict["Back"] = 1000
            swimmerdict["Free"] = 1000
        # back, free, breast, fly, im
        elif backtest > freetest and freetest > breasttest and breasttest > flytest and flytest > imtest:
            del swimmerdict["Back"]
            del swimmerdict["Free"]
            swimmerdict["Back"] = 1000
            swimmerdict["Free"] = 1000
        # back, free, breast, im, fly
        elif backtest > freetest and freetest > breasttest and breasttest > imtest and imtest > flytest:
            del swimmerdict["Back"]
            del swimmerdict["Free"]
            swimmerdict["Back"] = 1000
            swimmerdict["Free"] = 1000
        # back, free, im, fly, breast
        elif backtest > freetest and freetest > imtest and imtest > flytest and flytest > breattest:
            del swimmerdict["Back"]
            del swimmerdict["Free"]
            swimmerdict["Back"] = 1000
            swimmerdict["Free"] = 1000
        # back, free, im, breast, fly
        elif backtest > freetest and freetest > imtest and imtest > breasttest and breasttest > flytest:
            del swimmerdict["Back"]
            del swimmerdict["Free"]
            swimmerdict["Back"] = 1000
            swimmerdict["Free"] = 1000


        # back, im, fly, breast, free
        elif backtest > imtest and imtest > flytest and flytest > breasttest and breasttest > freetest:
            del swimmerdict["Back"]
            del swimmerdict["IM"]
            swimmerdict["Back"] = 1000
            swimmerdict["IM"] = 1000
        # back, im, fly, free, breast
        elif backtest > imtest and imtest > flytest and flytest > freetest and freetest > breasttest:
            del swimmerdict["Back"]
            del swimmerdict["IM"]
            swimmerdict["Back"] = 1000
            swimmerdict["IM"] = 1000
        # back, im, breast, free, fly
        elif backtest > imtest and imtest > breasttest and breasttest > freetest and freetest > flytest:
            del swimmerdict["Back"]
            del swimmerdict["IM"]
            swimmerdict["Back"] = 1000
            swimmerdict["IM"] = 1000
        # back, im, breast, fly, free
        elif backtest > imtest and imtest > breasttest and breasttest > flytest and flytest > freetest:
            del swimmerdict["Back"]
            del swimmerdict["IM"]
            swimmerdict["Back"] = 1000
            swimmerdict["IM"] = 1000
        # back, im, free, breast, fly
        elif backtest > imtest and imtest > freetest and freetest > breasttest and breasttest > flytest:
            del swimmerdict["Back"]
            del swimmerdict["IM"]
            swimmerdict["Back"] = 1000
            swimmerdict["IM"] = 1000
        # back, im, free, fly, breast
        elif backtest > imtest and imtest > freetest and freetest > flytest and flytest > breasttest:
            del swimmerdict["Back"]
            del swimmerdict["IM"]
            swimmerdict["Back"] = 1000
            swimmerdict["IM"] = 1000
            
        
        # breast, fly, back, free, im
        elif breasttest > flytest and flytest > backtest and backtest > freetest and freetest > imtest:
            del swimmerdict["Breast"]
            del swimmerdict["Fly"]
            swimmerdict["Breast"] = 1000
            swimmerdict["Fly"] = 1000
        # breast, fly, back, im, free
        elif breasttest > flytest and flytest > backtest and backtest > imtest and imtest > freetest:
            del swimmerdict["Breast"]
            del swimmerdict["Fly"]
            swimmerdict["Breast"] = 1000
            swimmerdict["Fly"] = 1000
        # breast, fly, free, back, im
        elif breasttest > flytest and flytest > freetest and freetest > backtest and backtest > imtest:
            del swimmerdict["Breast"]
            del swimmerdict["Fly"]
            swimmerdict["Breast"] = 1000
            swimmerdict["Fly"] = 1000
        # breast, fly, free, im, back
        elif breasttest > flytest and flytest > freetest and freetest > imtest and imtest > backtest:
            del swimmerdict["Breast"]
            del swimmerdict["Fly"]
            swimmerdict["Breast"] = 1000
            swimmerdict["Fly"] = 1000
        # breast, fly, im, free, back
        elif breasttest > flytest and flytest > imtest and imtest > freetest and freetest > backtest:
            del swimmerdict["Breast"]
            del swimmerdict["Fly"]
            swimmerdict["Breast"] = 1000
            swimmerdict["Fly"] = 1000
        # breast, fly, im, back, free
        elif breasttest > flytest and flytest > imtest and imtest > backtest and backtest > freetest:
            del swimmerdict["Breast"]
            del swimmerdict["Fly"]
            swimmerdict["Breast"] = 1000
            swimmerdict["Fly"] = 1000
            
        
        # breast, back, free, fly, im
        elif breasttest > backtest and backtest > freetest and freetest > flytest and flytest > imtest:
            del swimmerdict["Breast"]
            del swimmerdict["Back"]
            swimmerdict["Breast"] = 1000
            swimmerdict["Back"] = 1000
        # breast, back, free, im, fly
        elif breasttest > backtest and backtest > freetest and freetest > imtest and imtest > flytest:
            del swimmerdict["Breast"]
            del swimmerdict["Back"]
            swimmerdict["Breast"] = 1000
            swimmerdict["Back"] = 1000
        # breast, back, fly, free, im
        elif breasttest > backtest and backtest > flytest and flytest > freetest and freetest > imtest:
            del swimmerdict["Breast"]
            del swimmerdict["Back"]
            swimmerdict["Breast"] = 1000
            swimmerdict["Back"] = 1000
        # breast, back, fly, im, free
        elif breasttest > backtest and backtest > flytest and flytest > imtest and imtest > freetest:
            del swimmerdict["Breast"]
            del swimmerdict["Back"]
            swimmerdict["Breast"] = 1000
            swimmerdict["Back"] = 1000
        # breast, back, im, fly, free
        elif breasttest > backtest and backtest > imtest and imtest > flytest and flytest > freetest:
            del swimmerdict["Breast"]
            del swimmerdict["Back"]
            swimmerdict["Breast"] = 1000
            swimmerdict["Back"] = 1000
        # breast, back, im, free, fly
        elif breasttest > backtest and backtest > imtest and imtest > freetest and freetest > flytest:
            del swimmerdict["Breast"]
            del swimmerdict["Back"]
            swimmerdict["Breast"] = 1000
            swimmerdict["Back"] = 1000
            
        
        # breast, free, back, fly, im
        elif breasttest > freetest and freetest > backtest and backtest > flytest and flytest > imtest:
            del swimmerdict["Breast"]
            del swimmerdict["Free"]
            swimmerdict["Breast"] = 1000
            swimmerdict["Free"] = 1000
        # breast, free, back, im, fly
        elif breasttest > freetest and freetest > backtest and backtest > imtest and imtest > flytest:
            del swimmerdict["Breast"]
            del swimmerdict["Free"]
            swimmerdict["Breast"] = 1000
            swimmerdict["Free"] = 1000
        # breast, free, fly, back, im
        elif breasttest > freetest and freetest > flytest and flytest > backtest and backtest > imtest:
            del swimmerdict["Breast"]
            del swimmerdict["Free"]
            swimmerdict["Breast"] = 1000
            swimmerdict["Free"] = 1000
        # breast, free, fly, im, back
        elif breasttest > freetest and freetest > flytest and flytest > imtest and imtest > backtest:
            del swimmerdict["Breast"]
            del swimmerdict["Free"]
            swimmerdict["Breast"] = 1000
            swimmerdict["Free"] = 1000
        # breast, free, im, fly, back
        elif breasttest > freetest and freetest > imtest and imtest > flytest and flytest > backtest:
            del swimmerdict["Breast"]
            del swimmerdict["Free"]
            swimmerdict["Breast"] = 1000
            swimmerdict["Free"] = 1000
        # breast, free, im, back, fly
        elif breasttest > freetest and freetest > imtest and imtest > backtest and backtest > flytest:
            del swimmerdict["Breast"]
            del swimmerdict["Free"]
            swimmerdict["Breast"] = 1000
            swimmerdict["Free"] = 1000
        
        # breast, im, fly, back, free
        elif breasttest > imtest and imtest > flytest and flytest > backtest and backtest > freetest:
            del swimmerdict["Breast"]
            del swimmerdict["IM"]
            swimmerdict["Breast"] = 1000
            swimmerdict["IM"] = 1000
        # breast, im, fly, free, back
        elif breasttest > imtest and imtest > flytest and flytest > freetest and freetest > backtest:
            del swimmerdict["Breast"]
            del swimmerdict["IM"]
            swimmerdict["Breast"] = 1000
            swimmerdict["IM"] = 1000
        # breast, im, back, fly, free
        elif breasttest > imtest and imtest > backtest and backtest > flytest and flytest > freetest:
            del swimmerdict["Breast"]
            del swimmerdict["IM"]
            swimmerdict["Breast"] = 1000
            swimmerdict["IM"] = 1000
        # breast, im, back, free, fly
        elif breasttest > imtest and imtest > backtest and backtest > freetest and freetest > flytest:
            del swimmerdict["Breast"]
            del swimmerdict["IM"]
            swimmerdict["Breast"] = 1000
            swimmerdict["IM"] = 1000
        # breast, im, free, back, fly
        elif breasttest > imtest and imtest > freetest and freetest > backtest and backtest > flytest:
            del swimmerdict["Breast"]
            del swimmerdict["IM"]
            swimmerdict["Breast"] = 1000
            swimmerdict["IM"] = 1000
        # breast, im, free, fly, back
        elif breasttest > imtest and imtest > freetest and freetest > flytest and flytest > backtest:
            del swimmerdict["Breast"]
            del swimmerdict["IM"]
            swimmerdict["Breast"] = 1000
            swimmerdict["IM"] = 1000
        
        
        # free, fly, back, breast, im
        elif freetest > flytest and flytest > backtest and backtest > breasttest and breasttest > imtest:
            del swimmerdict["Free"]
            del swimmerdict["Fly"]
            swimmerdict["Free"] = 1000
            swimmerdict["Fly"] = 1000
        # free, fly, back, im, breast
        elif freetest > flytest and flytest > backtest and backtest > imtest and imtest > breasttest:
            del swimmerdict["Free"]
            del swimmerdict["Fly"]
            swimmerdict["Free"] = 1000
            swimmerdict["Fly"] = 1000
        # free, fly, breast, back, im
        elif freetest > flytest and flytest > breasttest and breasttest > backtest and backtest > imtest:
            del swimmerdict["Free"]
            del swimmerdict["Fly"]
            swimmerdict["Free"] = 1000
            swimmerdict["Fly"] = 1000
        # free, fly, breast, im, back
        elif freetest > flytest and flytest > breasttest and breasttest > imtest and imtest > backtest:
            del swimmerdict["Free"]
            del swimmerdict["Fly"]
            swimmerdict["Free"] = 1000
            swimmerdict["Fly"] = 1000
        # free, fly, im, breast, back
        elif freetest > flytest and flytest > imtest and imtest > breasttest and breasttest > backtest:
            del swimmerdict["Free"]
            del swimmerdict["Fly"]
            swimmerdict["Free"] = 1000
            swimmerdict["Fly"] = 1000
        # free, fly, im, back, breast
        elif freetest > flytest and flytest > imtest and imtest > backtest and backtest > breasttest:
            del swimmerdict["Free"]
            del swimmerdict["Fly"]
            swimmerdict["Free"] = 1000
            swimmerdict["Fly"] = 1000
            
        
        # free, back, breast, fly, im
        elif freetest > backtest and backtest > breasttest and breasttest > flytest and flytest > imtest:
            del swimmerdict["Free"]
            del swimmerdict["Back"]
            swimmerdict["Free"] = 1000
            swimmerdict["Back"] = 1000
        # free, back, breast, im, fly
        elif freetest > backtest and backtest > breasttest and breasttest > imtest and imtest > flytest:
            del swimmerdict["Free"]
            del swimmerdict["Back"]
            swimmerdict["Free"] = 1000
            swimmerdict["Back"] = 1000
        # free, back, fly, breast, im
        elif freetest > backtest and backtest > flytest and flytest > breasttest and breasttest > imtest:
            del swimmerdict["Free"]
            del swimmerdict["Back"]
            swimmerdict["Free"] = 1000
            swimmerdict["Back"] = 1000
        # free, back, fly, im, breast
        elif freetest > backtest and backtest > flytest and flytest > imtest and imtest > breasttest:
            del swimmerdict["Free"]
            del swimmerdict["Back"]
            swimmerdict["Free"] = 1000
            swimmerdict["Back"] = 1000
        # free, back, im, fly, breast
        elif freetest > backtest and backtest > imtest and imtest > flytest and flytest > breasttest:
            del swimmerdict["Free"]
            del swimmerdict["Back"]
            swimmerdict["Free"] = 1000
            swimmerdict["Back"] = 1000
        # free, back, im, breast, fly
        elif freetest > backtest and backtest > imtest and imtest > breasttest and breasttest > flytest:
            del swimmerdict["Free"]
            del swimmerdict["Back"]
            swimmerdict["Free"] = 1000
            swimmerdict["Back"] = 1000
        
        
        # free, breast, back, fly, im
        elif freetest > breasttest and breasttest > backtest and backtest > flytest and flytest > imtest:
            del swimmerdict["Free"]
            del swimmerdict["Breast"]
            swimmerdict["Free"] = 1000
            swimmerdict["Breast"] = 1000
        # free, breast, back, im, fly
        elif freetest > breasttest and breasttest > backtest and backtest > imtest and imtest > flytest:
            del swimmerdict["Free"]
            del swimmerdict["Breast"]
            swimmerdict["Free"] = 1000
            swimmerdict["Breast"] = 1000
        # free, breast, fly, back, im
        elif freetest > breasttest and breasttest > flytest and flytest > backtest and backtest > imtest:
            del swimmerdict["Free"]
            del swimmerdict["Breast"]
            swimmerdict["Free"] = 1000
            swimmerdict["Breast"] = 1000
        # free, breast, fly, im, back
        elif freetest > breasttest and breasttest > flytest and flytest > imtest and imtest > backtest:
            del swimmerdict["Free"]
            del swimmerdict["Breast"]
            swimmerdict["Free"] = 1000
            swimmerdict["Breast"] = 1000
        # free, breast, im, fly, back
        elif freetest > breasttest and breasttest > imtest and imtest > flytest and flytest > backtest:
            del swimmerdict["Free"]
            del swimmerdict["Breast"]
            swimmerdict["Free"] = 1000
            swimmerdict["Breast"] = 1000
        # free, breast, im, back, fly
        elif freetest > breasttest and breasttest > imtest and imtest > backtest and backtest > flytest:
            del swimmerdict["Free"]
            del swimmerdict["Breast"]
            swimmerdict["Free"] = 1000
            swimmerdict["Breast"] = 1000
        
        
        # free, im, fly, back, breast
        elif freetest > imtest and imtest > flytest and flytest > backtest and backtest > breasttest:
            del swimmerdict["Free"]
            del swimmerdict["IM"]
            swimmerdict["Free"] = 1000
            swimmerdict["IM"] = 1000
        # free, im, fly, breast, back
        elif freetest > imtest and imtest > flytest and flytest > breasttest and breasttest > backtest:
            del swimmerdict["Free"]
            del swimmerdict["IM"]
            swimmerdict["Free"] = 1000
            swimmerdict["IM"] = 1000
        # free, im, back, breast, fly
        elif freetest > imtest and imtest > backtest and backtest > breasttest and breasttest > flytest:
            del swimmerdict["Free"]
            del swimmerdict["IM"]
            swimmerdict["Free"] = 1000
            swimmerdict["IM"] = 1000
        # free, im, back, fly, breast
        elif freetest > imtest and imtest > backtest and backtest > flytest and flytest > breasttest:
            del swimmerdict["Free"]
            del swimmerdict["IM"]
            swimmerdict["Free"] = 1000
            swimmerdict["IM"] = 1000
        # free, im, breast, back, fly
        elif freetest > imtest and imtest > breasttest and breasttest > backtest and backtest > flytest:
            del swimmerdict["Free"]
            del swimmerdict["IM"]
            swimmerdict["Free"] = 1000
            swimmerdict["IM"] = 1000
        # free, im, breast, fly, back
        elif freetest > imtest and imtest > breasttest and breasttest > flytest and flytest > backtest:
            del swimmerdict["Free"]
            del swimmerdict["IM"]
            swimmerdict["Free"] = 1000
            swimmerdict["IM"] = 1000
            
        
        # im, fly, back, breast, free
        elif imtest > flytest and flytest > backtest and backtest > breasttest and breasttest > freetest:
            del swimmerdict["IM"]
            del swimmerdict["Fly"]
            swimmerdict["IM"] = 1000
            swimmerdict["Fly"] = 1000
        # im, fly, back, free, breast
        elif imtest > flytest and flytest > backtest and backtest > freetest and freetest > breasttest:
            del swimmerdict["IM"]
            del swimmerdict["Fly"]
            swimmerdict["IM"] = 1000
            swimmerdict["Fly"] = 1000
        # im, fly, breast, back, free
        elif imtest > flytest and flytest > breasttest and breasttest > backtest and backtest > freetest:
            del swimmerdict["IM"]
            del swimmerdict["Fly"]
            swimmerdict["IM"] = 1000
            swimmerdict["Fly"] = 1000
        # im, fly, breast, free, back
        elif imtest > flytest and flytest > breasttest and breasttest > freetest and freetest > backtest:
            del swimmerdict["IM"]
            del swimmerdict["Fly"]
            swimmerdict["IM"] = 1000
            swimmerdict["Fly"] = 1000
        # im, fly, free, breast, back
        elif imtest > flytest and flytest > freetest and freetest > breasttest and breasttest > backtest:
            del swimmerdict["IM"]
            del swimmerdict["Fly"]
            swimmerdict["IM"] = 1000
            swimmerdict["Fly"] = 1000
        # im, fly, free, back, breast
        elif imtest > flytest and flytest > freetest and freetest > backtest and backtest > breasttest:
            del swimmerdict["IM"]
            del swimmerdict["Fly"]
            swimmerdict["IM"] = 1000
            swimmerdict["Fly"] = 1000
        
        
        # im, back, fly, breast, free
        elif imtest > backtest and backtest > flytest and flytest > breasttest and breasttest > freetest:
            del swimmerdict["IM"]
            del swimmerdict["Back"]
            swimmerdict["IM"] = 1000
            swimmerdict["Back"] = 1000
        # im, back, fly, free, breast
        elif imtest > backtest and backtest > flytest and flytest > freetest and freetest > breasttest:
            del swimmerdict["IM"]
            del swimmerdict["Back"]
            swimmerdict["IM"] = 1000
            swimmerdict["Back"] = 1000
        # im, back, breast, fly, free
        elif imtest > backtest and backtest > breasttest and breasttest > flytest and flytest > freetest:
            del swimmerdict["IM"]
            del swimmerdict["Back"]
            swimmerdict["IM"] = 1000
            swimmerdict["Back"] = 1000
        # im, back, breast, free, fly
        elif imtest > backtest and backtest > breasttest and breasttest > freetest and freetest > flytest:
            del swimmerdict["IM"]
            del swimmerdict["Back"]
            swimmerdict["IM"] = 1000
            swimmerdict["Back"] = 1000
        # im, back, free, breast, fly
        elif imtest > backtest and backtest > freetest and freetest > breasttest and breasttest > flytest:
            del swimmerdict["IM"]
            del swimmerdict["Back"]
            swimmerdict["IM"] = 1000
            swimmerdict["Back"] = 1000
        # im, back, free, fly, breast
        elif imtest > backtest and backtest > freetest and freetest > flytest and flytest > breasttest:
            del swimmerdict["IM"]
            del swimmerdict["Back"]
            swimmerdict["IM"] = 1000
            swimmerdict["Back"] = 1000
        
        
        # im, breast, fly, back, free
        elif imtest > breasttest and breasttest > flytest and flytest > backtest and backtest > freetest:
            del swimmerdict["IM"]
            del swimmerdict["Breast"]
            swimmerdict["IM"] = 1000
            swimmerdict["Breast"] = 1000
        # im, breast, fly, free, back
        elif imtest > breasttest and breasttest > flytest and flytest > freetest and freetest > backtest:
            del swimmerdict["IM"]
            del swimmerdict["Breast"]
            swimmerdict["IM"] = 1000
            swimmerdict["Breast"] = 1000
        # im, breast, back, fly, free
        elif imtest > breasttest and breasttest > backtest and backtest > flytest and flytest > freetest:
            del swimmerdict["IM"]
            del swimmerdict["Breast"]
            swimmerdict["IM"] = 1000
            swimmerdict["Breast"] = 1000
        # im, breast, back, free, fly
        elif imtest > breasttest and breasttest > backtest and backtest > freetest and freetest > flytest:
            del swimmerdict["IM"]
            del swimmerdict["Breast"]
            swimmerdict["IM"] = 1000
            swimmerdict["Breast"] = 1000
        # im, breast, free, back, fly
        elif imtest > breasttest and breasttest > freetest and freetest > backtest and backtest > flytest:
            del swimmerdict["IM"]
            del swimmerdict["Breast"]
            swimmerdict["IM"] = 1000
            swimmerdict["Breast"] = 1000
        # im, breast, free, fly, back
        elif imtest > breasttest and breasttest > freetest and freetest > flytest and flytest > backtest:
            del swimmerdict["IM"]
            del swimmerdict["Breast"]
            swimmerdict["IM"] = 1000
            swimmerdict["Breast"] = 1000
        
        
        # im, free, fly, back, breast
        elif imtest > freetest and freetest > flytest and flytest > backtest and backtest > breasttest:
            del swimmerdict["IM"]
            del swimmerdict["Free"]
            swimmerdict["IM"] = 1000
            swimmerdict["Free"] = 1000
        # im, free, fly, breast, back
        elif imtest > freetest and freetest > flytest and flytest > breasttest and breasttest > backtest:
            del swimmerdict["IM"]
            del swimmerdict["Free"]
            swimmerdict["IM"] = 1000
            swimmerdict["Free"] = 1000
        # im, free, back, breast, fly
        elif imtest > freetest and freetest > backtest and backtest > breasttest and breasttest > flytest:
            del swimmerdict["IM"]
            del swimmerdict["Free"]
            swimmerdict["IM"] = 1000
            swimmerdict["Free"] = 1000
        # im, free, back, fly, breast
        elif imtest > freetest and freetest > backtest and backtest > flytest and flytest > breasttest:
            del swimmerdict["IM"]
            del swimmerdict["Free"]
            swimmerdict["IM"] = 1000
            swimmerdict["Free"] = 1000
        # im, free, breast, fly, back
        elif imtest > freetest and freetest > breasttest and breasttest > flytest and flytest > backtest:
            del swimmerdict["IM"]
            del swimmerdict["Free"]
            swimmerdict["IM"] = 1000
            swimmerdict["Free"] = 1000
        # im, free, breast, back, fly
        elif imtest > freetest and freetest > breasttest and breasttest > backtest and backtest > flytest:
            del swimmerdict["IM"]
            del swimmerdict["Free"]
            swimmerdict["IM"] = 1000
            swimmerdict["Free"] = 1000
    
    return swimmerlist

#use the function

SH_Swimmer6UGirlsList = PickEvents(SH_Swimmer6UGirlsList,SixUnderGirlsCounty)
OCC_Swimmer6UGirlsList = PickEvents(OCC_Swimmer6UGirlsList,SixUnderGirlsCounty)
OPP_Swimmer6UGirlsList = PickEvents(OPP_Swimmer6UGirlsList,SixUnderGirlsCounty)
MEAD_Swimmer6UGirlsList = PickEvents(MEAD_Swimmer6UGirlsList,SixUnderGirlsCounty)
MVP_Swimmer6UGirlsList = PickEvents(MVP_Swimmer6UGirlsList,SixUnderGirlsCounty)
MIRA_Swimmer6UGirlsList = PickEvents(MIRA_Swimmer6UGirlsList,SixUnderGirlsCounty)
MCC_Swimmer6UGirlsList = PickEvents(MCC_Swimmer6UGirlsList,SixUnderGirlsCounty)
MRSC_Swimmer6UGirlsList = PickEvents(MRSC_Swimmer6UGirlsList,SixUnderGirlsCounty)
CCC_Swimmer6UGirlsList = PickEvents(CCC_Swimmer6UGirlsList,SixUnderGirlsCounty)

SH_Swimmer78BoysList = PickEvents(SH_Swimmer78BoysList,SevenEightBoysCounty)
OCC_Swimmer78BoysList = PickEvents(OCC_Swimmer78BoysList,SevenEightBoysCounty)
OPP_Swimmer78BoysList = PickEvents(OPP_Swimmer78BoysList,SevenEightBoysCounty)
MEAD_Swimmer78BoysList = PickEvents(MEAD_Swimmer78BoysList,SevenEightBoysCounty)
MVP_Swimmer78BoysList = PickEvents(MVP_Swimmer78BoysList,SevenEightBoysCounty)
MIRA_Swimmer78BoysList = PickEvents(MIRA_Swimmer78BoysList,SevenEightBoysCounty)
MCC_Swimmer78BoysList = PickEvents(MCC_Swimmer78BoysList,SevenEightBoysCounty)
MRSC_Swimmer78BoysList = PickEvents(MRSC_Swimmer78BoysList,SevenEightBoysCounty)
CCC_Swimmer78BoysList = PickEvents(CCC_Swimmer78BoysList,SevenEightBoysCounty)

print "========================"
print "6/under Entries"
print "========================"
print "SH Entries"
print SH_Swimmer6UGirlsList
print "========================"
print "OCC Entries"
print OCC_Swimmer6UGirlsList
print "========================"
print "OPP Entries"
print OPP_Swimmer6UGirlsList
print "========================"
print "MEAD Entries"
print MEAD_Swimmer6UGirlsList
print "========================"
print "MVP Entries"
print MVP_Swimmer6UGirlsList
print "========================"
print "MIRA Entries"
print MIRA_Swimmer6UGirlsList
print "========================"
print "MCC Entries"
print MCC_Swimmer6UGirlsList
print "========================"
print "MRSC Entries"
print MRSC_Swimmer6UGirlsList
print "========================"
print "CCC Entries"
print CCC_Swimmer6UGirlsList
print "========================"

print "========================"
print "7/8 Entries"
print "========================"
print "SH Entries"
print SH_Swimmer78BoysList
print "========================"
print "OCC Entries"
print OCC_Swimmer78BoysList
print "========================"
print "OPP Entries"
print OPP_Swimmer78BoysList
print "========================"
print "MEAD Entries"
print MEAD_Swimmer78BoysList
print "========================"
print "MVP Entries"
print MVP_Swimmer78BoysList
print "========================"
print "MIRA Entries"
print MIRA_Swimmer78BoysList
print "========================"
print "MCC Entries"
print MCC_Swimmer78BoysList
print "========================"
print "MRSC Entries"
print MRSC_Swimmer78BoysList
print "========================"
print "CCC Entries"
print CCC_Swimmer78BoysList
print "========================"

def FillEvent(Stroke,AgeGroupStroke, SH, OCC, OPP, MEAD, MVP, MIRA, MCC, MRSC, CCC): 
    # to access the dictionary inside of a list:
    # Index the list then the dict.
    # print List[1]['keyname']
    
    for swimmers in SH:
        swimmerID = SH.index(swimmers)
        AgeGroupStroke.append({"SH":SH[swimmerID][Stroke]})
    
    for swimmers in OCC:
        swimmerID = OCC.index(swimmers)
        AgeGroupStroke.append({"OCC":OCC[swimmerID][Stroke]})
    
    for swimmers in OPP:
        swimmerID = OPP.index(swimmers)
        AgeGroupStroke.append({"OPP":OPP[swimmerID][Stroke]})
     
    for swimmers in MEAD:
        swimmerID = MEAD.index(swimmers)
        AgeGroupStroke.append({"MEAD":MEAD[swimmerID][Stroke]})
        
    for swimmers in MVP:
       swimmerID = MVP.index(swimmers)
       AgeGroupStroke.append({"MVP":MVP[swimmerID][Stroke]})
       
    for swimmers in MIRA:
       swimmerID = MIRA.index(swimmers)
       AgeGroupStroke.append({"MIRA":MIRA[swimmerID][Stroke]})
    
    for swimmers in MCC:
       swimmerID = MCC.index(swimmers)
       AgeGroupStroke.append({"MCC":MCC[swimmerID][Stroke]})
        
    for swimmers in MRSC:
       swimmerID = MRSC.index(swimmers)
       AgeGroupStroke.append({"MRSC":MRSC[swimmerID][Stroke]})
    
    for swimmers in CCC:
       swimmerID = CCC.index(swimmers)
       AgeGroupStroke.append({"CCC":CCC[swimmerID][Stroke]})
    
    AgeGroupStroke = sorted(AgeGroupStroke, key=lambda k: k.values())    
    return AgeGroupStroke
    
# use the function

def ScoreEvent(AgeGroupStroke, AgeGroupPoints, AgeGroupStrokePoints, ScoringScheme):

    # for each dictionary contained in the list
    for swimmers in AgeGroupStroke:
        # index rank of each dictionary contained in the list
        swimmerID = AgeGroupStroke.index(swimmers)
        
        # SH
        # if the key "SH" is in the dictionary, and the index is less than 20 (index 0-19 score) 
        if "SH" in swimmers and swimmerID < 20:
            print "Rank:" + str(swimmerID+1) + " " + str(swimmers) + " Points:" + str(ScoringScheme[swimmerID])
            if "SH" in AgeGroupPoints:
                AgeGroupPoints["SH"] = AgeGroupPoints["SH"] + ScoringScheme[swimmerID]
            else:
                 AgeGroupPoints["SH"] = ScoringScheme[swimmerID]
            if "SH" in AgeGroupStrokePoints:
                AgeGroupStrokePoints["SH"] = AgeGroupStrokePoints["SH"] + ScoringScheme[swimmerID]
            else:
                AgeGroupStrokePoints["SH"] = ScoringScheme[swimmerID]
        # if SH doesnt have anyone in the 0-19 index, still create an entry of {"SH":0}. this avoids errors later
        else:
            if "SH" in AgeGroupPoints:
                AgeGroupPoints["SH"] = AgeGroupPoints["SH"] + 0
            else:
                AgeGroupPoints["SH"] = 0
            if  "SH" in AgeGroupStrokePoints:
                AgeGroupStrokePoints["SH"] = AgeGroupStrokePoints["SH"] + 0
            else:
                AgeGroupStrokePoints["SH"] = 0
        # OCC
        if "OCC" in swimmers and swimmerID < 20:
            print "Rank:" + str(swimmerID+1) + " " + str(swimmers) + " Points:" + str(ScoringScheme[swimmerID])
            if "OCC" in AgeGroupPoints:
                AgeGroupPoints["OCC"] = AgeGroupPoints["OCC"] + ScoringScheme[swimmerID]
            else:
                 AgeGroupPoints["OCC"] = ScoringScheme[swimmerID]
            if "OCC" in AgeGroupStrokePoints:
                AgeGroupStrokePoints["OCC"] = AgeGroupStrokePoints["OCC"] + ScoringScheme[swimmerID]
            else:
                AgeGroupStrokePoints["OCC"] = ScoringScheme[swimmerID]
        else:
            if "OCC" in AgeGroupPoints:
                AgeGroupPoints["OCC"] = AgeGroupPoints["OCC"] + 0
            else:
                AgeGroupPoints["OCC"] = 0
            if  "OCC" in AgeGroupStrokePoints:
                AgeGroupStrokePoints["OCC"] = AgeGroupStrokePoints["OCC"] + 0
            else:
                AgeGroupStrokePoints["OCC"] = 0
        # OPP
        if "OPP" in swimmers and swimmerID < 20:
            print "Rank:" + str(swimmerID+1) + " " + str(swimmers) + " Points:" + str(ScoringScheme[swimmerID])
            if "OPP" in AgeGroupPoints:
                AgeGroupPoints["OPP"] = AgeGroupPoints["OPP"] + ScoringScheme[swimmerID]
            else:
                 AgeGroupPoints["OPP"] = ScoringScheme[swimmerID]
            if "OPP" in AgeGroupStrokePoints:
                AgeGroupStrokePoints["OPP"] = AgeGroupStrokePoints["OPP"] + ScoringScheme[swimmerID]
            else:
                AgeGroupStrokePoints["OPP"] = ScoringScheme[swimmerID]
        else:
            if "OPP" in AgeGroupPoints:
                AgeGroupPoints["OPP"] = AgeGroupPoints["OPP"] + 0
            else:
                AgeGroupPoints["OPP"] = 0
            if  "OPP" in AgeGroupStrokePoints:
                AgeGroupStrokePoints["OPP"] = AgeGroupStrokePoints["OPP"] + 0
            else:
                AgeGroupStrokePoints["OPP"] = 0
        # MEAD
        if "MEAD" in swimmers and swimmerID < 20:
            print "Rank:" + str(swimmerID+1) + " " + str(swimmers) + " Points:" + str(ScoringScheme[swimmerID])
            if "MEAD" in AgeGroupPoints:
                AgeGroupPoints["MEAD"] = AgeGroupPoints["MEAD"] + ScoringScheme[swimmerID]
            else:
                 AgeGroupPoints["MEAD"] = ScoringScheme[swimmerID]
            if "MEAD" in AgeGroupStrokePoints:
                AgeGroupStrokePoints["MEAD"] = AgeGroupStrokePoints["MEAD"] + ScoringScheme[swimmerID]
            else:
                AgeGroupStrokePoints["MEAD"] = ScoringScheme[swimmerID]
        else:
            if "MEAD" in AgeGroupPoints:
                AgeGroupPoints["MEAD"] = AgeGroupPoints["MEAD"] + 0
            else:
                AgeGroupPoints["MEAD"] = 0
            if  "MEAD" in AgeGroupStrokePoints:
                AgeGroupStrokePoints["MEAD"] = AgeGroupStrokePoints["MEAD"] + 0
            else:
                AgeGroupStrokePoints["MEAD"] = 0
        # MVP
        if "MVP" in swimmers and swimmerID < 20:
            print "Rank:" + str(swimmerID+1) + " " + str(swimmers) + " Points:" + str(ScoringScheme[swimmerID])
            if "MVP" in AgeGroupPoints:
                AgeGroupPoints["MVP"] = AgeGroupPoints["MVP"] + ScoringScheme[swimmerID]
            else:
                 AgeGroupPoints["MVP"] = ScoringScheme[swimmerID]
            if "MVP" in AgeGroupStrokePoints:
                AgeGroupStrokePoints["MVP"] = AgeGroupStrokePoints["MVP"] + ScoringScheme[swimmerID]
            else:
                AgeGroupStrokePoints["MVP"] = ScoringScheme[swimmerID]
        else:
            if "MVP" in AgeGroupPoints:
                AgeGroupPoints["MVP"] = AgeGroupPoints["MVP"] + 0
            else:
                AgeGroupPoints["MVP"] = 0
            if  "MVP" in AgeGroupStrokePoints:
                AgeGroupStrokePoints["MVP"] = AgeGroupStrokePoints["MVP"] + 0
            else:
                AgeGroupStrokePoints["MVP"] = 0
        # MIRA
        if "MIRA" in swimmers and swimmerID < 20:
            print "Rank:" + str(swimmerID+1) + " " + str(swimmers) + " Points:" + str(ScoringScheme[swimmerID])
            if "MIRA" in AgeGroupPoints:
                AgeGroupPoints["MIRA"] = AgeGroupPoints["MIRA"] + ScoringScheme[swimmerID]
            else:
                 AgeGroupPoints["MIRA"] = ScoringScheme[swimmerID]
            if "MIRA" in AgeGroupStrokePoints:
                AgeGroupStrokePoints["MIRA"] = AgeGroupStrokePoints["MIRA"] + ScoringScheme[swimmerID]
            else:
                AgeGroupStrokePoints["MIRA"] = ScoringScheme[swimmerID]
        else:
            if "MIRA" in AgeGroupPoints:
                AgeGroupPoints["MIRA"] = AgeGroupPoints["MIRA"] + 0
            else:
                AgeGroupPoints["MIRA"] = 0
            if  "MIRA" in AgeGroupStrokePoints:
                AgeGroupStrokePoints["MIRA"] = AgeGroupStrokePoints["MIRA"] + 0
            else:
                AgeGroupStrokePoints["MIRA"] = 0
        # MCC
        if "MCC" in swimmers and swimmerID < 20:
            print "Rank:" + str(swimmerID+1) + " " + str(swimmers) + " Points:" + str(ScoringScheme[swimmerID])
            if "MCC" in AgeGroupPoints:
                AgeGroupPoints["MCC"] = AgeGroupPoints["MCC"] + ScoringScheme[swimmerID]
            else:
                 AgeGroupPoints["MCC"] = ScoringScheme[swimmerID]
            if "MCC" in AgeGroupStrokePoints:
                AgeGroupStrokePoints["MCC"] = AgeGroupStrokePoints["MCC"] + ScoringScheme[swimmerID]
            else:
                AgeGroupStrokePoints["MCC"] = ScoringScheme[swimmerID]
        else:
            if "MCC" in AgeGroupPoints:
                AgeGroupPoints["MCC"] = AgeGroupPoints["MCC"] + 0
            else:
                AgeGroupPoints["MCC"] = 0
            if  "MCC" in AgeGroupStrokePoints:
                AgeGroupStrokePoints["MCC"] = AgeGroupStrokePoints["MCC"] + 0
            else:
                AgeGroupStrokePoints["MCC"] = 0
        # MRSC
        if "MRSC" in swimmers and swimmerID < 20:
            print "Rank:" + str(swimmerID+1) + " " + str(swimmers) + " Points:" + str(ScoringScheme[swimmerID])
            if "MRSC" in AgeGroupPoints:
                AgeGroupPoints["MRSC"] = AgeGroupPoints["MRSC"] + ScoringScheme[swimmerID]
            else:
                 AgeGroupPoints["MRSC"] = ScoringScheme[swimmerID]
            if "MRSC" in AgeGroupStrokePoints:
                AgeGroupStrokePoints["MRSC"] = AgeGroupStrokePoints["MRSC"] + ScoringScheme[swimmerID]
            else:
                AgeGroupStrokePoints["MRSC"] = ScoringScheme[swimmerID]
        else:
            if "MRSC" in AgeGroupPoints:
                AgeGroupPoints["MRSC"] = AgeGroupPoints["MRSC"] + 0
            else:
                AgeGroupPoints["MRSC"] = 0
            if  "MRSC" in AgeGroupStrokePoints:
                AgeGroupStrokePoints["MRSC"] = AgeGroupStrokePoints["MRSC"] + 0
            else:
                AgeGroupStrokePoints["MRSC"] = 0
        # CCC
        if "CCC" in swimmers and swimmerID < 20:
            print "Rank:" + str(swimmerID+1) + " " + str(swimmers) + " Points:" + str(ScoringScheme[swimmerID])
            if "CCC" in AgeGroupPoints:
                AgeGroupPoints["CCC"] = AgeGroupPoints["CCC"] + ScoringScheme[swimmerID]
            else:
                 AgeGroupPoints["CCC"] = ScoringScheme[swimmerID]
            if "CCC" in AgeGroupStrokePoints:
                AgeGroupStrokePoints["CCC"] = AgeGroupStrokePoints["CCC"] + ScoringScheme[swimmerID]
            else:
                AgeGroupStrokePoints["CCC"] = ScoringScheme[swimmerID]
        else:
            if "CCC" in AgeGroupPoints:
                AgeGroupPoints["CCC"] = AgeGroupPoints["CCC"] + 0
            else:
                AgeGroupPoints["CCC"] = 0
            if  "CCC" in AgeGroupStrokePoints:
                AgeGroupStrokePoints["CCC"] = AgeGroupStrokePoints["CCC"] + 0
            else:
                AgeGroupStrokePoints["CCC"] = 0
        
    return AgeGroupPoints
    
#use function

def OrderedScores(AgeGroupPoints):
    # this turns the AgeGroupPoints into an orderd tuple. Using this inside the ScoreEvent() 
    # doesnt work because the ordered tuples cant be continiously added to be key. 
    # thus they remain unordered dictionaries in most of the program
    OrderedScores = sorted(AgeGroupPoints.items(), key=lambda x: x[1], reverse = True)
    return OrderedScores


#use function

def AddTwoDictionaries(PointsOne,PointsTwo):
    TotalPoints = dict(PointsOne.items() + PointsTwo.items())
    for keys in TotalPoints:
        TotalPoints[keys] = PointsOne[keys] + PointsTwo[keys]
    return TotalPoints

#use function

################
# Six under girls freestyle
################
# fill the event
SixUnderGirls_Free_Event = FillEvent("Free",SixUnderGirls_Free_Event, SH_Swimmer6UGirlsList, OCC_Swimmer6UGirlsList, OPP_Swimmer6UGirlsList, 
MEAD_Swimmer6UGirlsList, MVP_Swimmer6UGirlsList, MIRA_Swimmer6UGirlsList, MCC_Swimmer6UGirlsList, MRSC_Swimmer6UGirlsList, CCC_Swimmer6UGirlsList)
# score the event and display the ordered score
print "  "
print "========================"
print "6/Under Girls Free: "
SixUnderGirls_Points = ScoreEvent(SixUnderGirls_Free_Event, SixUnderGirls_Points, SixUnderGirls_Free_Points, ScoringScheme1)
print "  "
print "6/Under Girls Free Points: "
print str(OrderedScores(SixUnderGirls_Free_Points))
print "  "
print "6/Under Girls Team Points: "
print str(OrderedScores(SixUnderGirls_Points))
print "  "
###############

################
# 7/8 boys freestyle
################
# fill the event
SevenEightBoys_Free_Event = FillEvent("Free",SevenEightBoys_Free_Event, SH_Swimmer78BoysList, OCC_Swimmer78BoysList, OPP_Swimmer78BoysList, 
MEAD_Swimmer78BoysList,MVP_Swimmer78BoysList,MIRA_Swimmer78BoysList,MCC_Swimmer78BoysList,MRSC_Swimmer78BoysList,CCC_Swimmer78BoysList)
# score the event and display the ordered score
print "  "
print "========================"
print "7/8 Boys Free: "
SevenEightBoys_Points = ScoreEvent(SevenEightBoys_Free_Event, SevenEightBoys_Points, SevenEightBoys_Free_Points, ScoringScheme1)
print "  "
print "7/8 Boys Free Points: "
print str(OrderedScores(SevenEightBoys_Free_Points))
print "  "
print "7/8 Boys Team Points: "
print str(OrderedScores(SevenEightBoys_Points))
print "  "
###############

###############
# Six under girls fly
###############
# fill the event
SixUnderGirls_Fly_Event = FillEvent("Fly",SixUnderGirls_Fly_Event, SH_Swimmer6UGirlsList, OCC_Swimmer6UGirlsList, OPP_Swimmer6UGirlsList, 
MEAD_Swimmer6UGirlsList,MVP_Swimmer6UGirlsList,MIRA_Swimmer6UGirlsList,MCC_Swimmer6UGirlsList,MRSC_Swimmer6UGirlsList,CCC_Swimmer6UGirlsList)
# score the event
print "  "
print "========================"
print "6/Under Girls Fly: "
SixUnderGirls_Points = ScoreEvent(SixUnderGirls_Fly_Event, SixUnderGirls_Points, SixUnderGirls_Fly_Points, ScoringScheme1)
print "  "
print "6/Under Girls Fly Points: "
print str(OrderedScores(SixUnderGirls_Fly_Points))
print "  "
print "6/Under Girls Team Points: "
print str(OrderedScores(SixUnderGirls_Points))
print "  "
###############

###############
# 7/8 boys fly
###############
# fill the event
SevenEightBoys_Fly_Event = FillEvent("Fly",SevenEightBoys_Fly_Event, SH_Swimmer78BoysList, OCC_Swimmer78BoysList, OPP_Swimmer78BoysList, 
MEAD_Swimmer78BoysList,MVP_Swimmer78BoysList,MIRA_Swimmer78BoysList,MCC_Swimmer78BoysList,MRSC_Swimmer78BoysList,CCC_Swimmer78BoysList)
# score the event and display the ordered score
print "  "
print "========================"
print "7/8 Boys Fly"
SevenEightBoys_Points = ScoreEvent(SevenEightBoys_Fly_Event, SevenEightBoys_Points, SevenEightBoys_Fly_Points, ScoringScheme1)
print "  "
print "7/8 Boys Fly Points: "
print str(OrderedScores(SevenEightBoys_Fly_Points))
print "  "
print "7/8 Boys Team Points: "
print str(OrderedScores(SevenEightBoys_Points))
print "  "
###############

###############
# scoring summary
###############
print "========================"
print "SCORING SUMMARY"
print "========================"
print "Team 6/Under Girls Total Points"
print str(OrderedScores(SixUnderGirls_Points))
print "  "
print "6/Under Girls Free"
print str(OrderedScores(SixUnderGirls_Free_Points))
print "6/Under Girls Fly"
print str(OrderedScores(SixUnderGirls_Fly_Points))
print "  "
print "========================"
print "Team 7/8 Boys Total Points"
print str(OrderedScores(SevenEightBoys_Points))
print "  "
print "7/8 Boys Free"
print str(OrderedScores(SevenEightBoys_Free_Points))
print "7/8 Boys Fly"
print str(OrderedScores(SevenEightBoys_Fly_Points))
print "  "
print "========================"
print "Team Free"
TotalPoints = AddTwoDictionaries(SevenEightBoys_Free_Points,SixUnderGirls_Free_Points)
print str(OrderedScores(TotalPoints))
print "  "
print "Team Fly"
TotalPoints = AddTwoDictionaries(SevenEightBoys_Fly_Points,SixUnderGirls_Fly_Points)
print str(OrderedScores(TotalPoints))
print "  "
print "========================"
print "Total Team Scores"
TotalPoints = AddTwoDictionaries(SevenEightBoys_Points,SixUnderGirls_Points)
print str(OrderedScores(TotalPoints))
print "  "

