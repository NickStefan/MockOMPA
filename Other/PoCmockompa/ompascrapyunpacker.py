

def LoadScrapyData(jsonscrapy):
    import json
    import ast
    import re

    with open(jsonscrapy) as json_file:
        json_data = json.load(json_file)
        json_data = ast.literal_eval(json.dumps(json_data))

    # gets rid of the json crap, u', and extra brackets
    namelist = []
    agelist = []
    teamlist = []
    timelist = []
    
    for swimmers in json_data:
        namelist.extend(swimmers["names"])
        agelist.extend(swimmers["age"])
        teamlist.extend(swimmers["team"])
        timelist.extend(swimmers["time"])
   
    # gets rid of swimmers from wrong teams who sometimes find there way into the database
    # for some reason the team filter needs to be run twice! 
    # it works on one team fine, but with say: swims == "OCC" or swims == "SH" will take out all SH and all but 1 OCC.
    for swims in teamlist:
        swimmerID = teamlist.index(swims)
        if swims == "LMYA" or swims == "SB" or swims == "LARKEY":
            del namelist[swimmerID]
            del agelist[swimmerID]
            del teamlist[swimmerID]
            del timelist[swimmerID]
        for swimmers2 in teamlist:
            swimmerID2 = teamlist.index(swimmers2)
            if swimmers2 == "SB" or swimmers2 == "LMYA" or swimmers2 == "LARKEY":
                del namelist[swimmerID2]
                del agelist[swimmerID2]
                del teamlist[swimmerID2]
                del timelist[swimmerID2]
        
        # fixes the "21.05y" into an actual float
        for times in timelist:
            timeID = timelist.index(times)
            timelist[timeID]= float(re.match(r'[-+]?\d*\.\d+|\d+', str(times)).group())
    
    #returns a tuple. so to print only the list of names: print namelist[0]
    return namelist, agelist, teamlist, timelist

# use function

# six and under girls load scrapy data
SixUnderGirlsFreestyle = LoadScrapyData("sixundergirlsfree.json")
SixUnderGirlsBreastroke = LoadScrapyData("sixundergirlsbreast.json")
SixUnderGirlsBackstroke = LoadScrapyData("sixundergirlsback.json")
SixUnderGirlsButterfly = LoadScrapyData("sixundergirlsfly.json")
SixUnderGirlsIM = [[],[],[],[]]

# seven and eight boys load scrapy data
SevenEightBoysFreestyle = LoadScrapyData("seveneightboysfree.json")
SevenEightBoysBreastroke = LoadScrapyData("seveneightboysbreast.json")
SevenEightBoysBackstroke = LoadScrapyData("seveneightboysback.json")
SevenEightBoysButterfly = LoadScrapyData("seveneightboysfly.json")
SevenEightBoysIM = LoadScrapyData("seveneightboysim.json")

# need to have all the lists match the same index as name.
# so the nameslist[1] needs to be the same person as freeslist[1]
# and flylist[1]. otherwise there doesnt need to be any speed or rank order
# could try to first 

# something like this could correctly fill a list of breastroke times
# that matches the index list of freestyle times. repeat for all strokes,
# alays match with names in sixundergirlsfreestyle.
    

def ReOrderStrokes(ScrapyFree,ScrapyBreast,ScrapyBack,ScrapyFly,ScrapyIM):
    #all of the strokes, teams, times, really all of the data in this age 
    #groups tuple will be lined up with the index of their name in the freestyle names list
    #therefore we need to make sure that kids who are in the top 50 for other strokes, but 
    #not in freestyle, get added to freestyle before we reorder everything:
    
    # find the missed names
    missednames = []
    for names in ScrapyBreast[0]:
        try: 
            matchid = ScrapyFree[0].index(names)
        except ValueError:
            missednames.append(names)
    for names in ScrapyBack[0]:
        try: 
            matchid = ScrapyFree[0].index(names)
        except ValueError:
            try: 
                matchid = missednames.index(names)
            except ValueError:
                missednames.append(names)
    for names in ScrapyFly[0]:
        try: 
            matchid = ScrapyFree[0].index(names)
        except ValueError:
            try:
                matchid = missednames.index(names)
            except ValueError:
                missednames.append(names)
    for names in ScrapyIM[0]:
        try: 
            matchid = ScrapyFree[0].index(names)
        except ValueError:
            try:
                matchid = missednames.index(names)
            except ValueError:
                missednames.append(names)
    
    # add the missed names to the freestyle tuples (ie name,age,team,time)
    for names in missednames:
        #add names
        ScrapyFree[0].append(names)
        #add a made up swim time
        ScrapyFree[3].append(1000)
        try:
            #add their team
            breastid = ScrapyBreast[0].index(names)
            ScrapyFree[2].append(ScrapyBreast[2][breastid])
            #add their age
            ScrapyFree[1].append(ScrapyBreast[1][breastid])
        except ValueError:
            try:
                #add their team
                backid = ScrapyBack[0].index(names)
                ScrapyFree[2].append(ScrapyBack[2][backid])
                #add their age
                ScrapyFree[1].append(ScrapyBack[1][backid])
            except ValueError:
                try:
                    #add their team
                    flyid = ScrapyFly[0].index(names)
                    ScrapyFree[2].append(ScrapyFly[2][flyid])
                    #add their age
                    ScrapyFree[1].append(ScrapyFly[1][flyid])
                except ValueError:
                        #add their team
                        imid = ScrapyIM[0].index(names)
                        ScrapyFree[2].append(ScrapyIM[2][imid])
                        #add their age
                        ScrapyFree[1].append(ScrapyIM[1][imid])
    
    #now that we're sure everyone has a freestyle name and time entry (even a dummy one), we can properly "re-index"
    #everything off of the freestyle lists.
    
    OutputBreast = []
    OutputBack = []
    OutputFly = []
    OutputIM = []
    
    for names in ScrapyFree[0]:
        nameid = ScrapyFree[0].index(names)
        
        #re-order breastroke list to match the name order of the freestyle list
        try:
            breastid = ScrapyBreast[0].index(names)
        except ValueError:
            ScrapyBreast[0].append(names)
            breastid = ScrapyBreast[0].index(names)
            ScrapyBreast[3].append(1000)
        OutputBreast.append(ScrapyBreast[3][breastid])
    
        #re-order backstroke list to match the name order of the freestyle list
        try:
            backid = ScrapyBack[0].index(names)
        except ValueError:
            ScrapyBack[0].append(names)
            backid = ScrapyBack[0].index(names)
            ScrapyBack[3].append(1000)
        OutputBack.append(ScrapyBack[3][backid])
    
        #re-order fly list to match the name order of the freestyle list
        try:
            flyid = ScrapyFly[0].index(names)
        except ValueError:
            ScrapyFly[0].append(names)
            flyid = ScrapyFly[0].index(names)
            ScrapyFly[3].append(1000)
        OutputFly.append(ScrapyFly[3][flyid])
    
        #re-order im list to match the name order of the freestyle list
        try:
            imid = ScrapyIM[0].index(names)
        except ValueError:
            ScrapyIM[0].append(names)
            imid = ScrapyIM[0].index(names)
            if ScrapyFree[1][nameid] > 6:
                ScrapyIM[3].append(1000)
            else:
                ScrapyIM[3].append(0)
        OutputIM.append(ScrapyIM[3][imid])
        
    return ScrapyFree[0],ScrapyFree[2],ScrapyFree[3],OutputBreast, OutputBack, OutputFly, OutputIM
# use function

SixUnderGirls = ReOrderStrokes(SixUnderGirlsFreestyle,SixUnderGirlsBreastroke,SixUnderGirlsBackstroke,SixUnderGirlsButterfly,SixUnderGirlsIM)
print "6 and Under Girls"
print "names" + str(SixUnderGirls[0])
print "team" + str(SixUnderGirls[1])
print "free" + str(SixUnderGirls[2])
print "breast" + str(SixUnderGirls[3])
print "back" + str(SixUnderGirls[4])
print "fly" + str(SixUnderGirls[5])
print "im" + str(SixUnderGirls[6])

print "Seven and Eight Boys"
SevenEightBoys = ReOrderStrokes(SevenEightBoysFreestyle,SevenEightBoysBreastroke,SevenEightBoysBackstroke,SevenEightBoysButterfly,SevenEightBoysIM)
print "names" + str(SevenEightBoys[0])
print "team" + str(SevenEightBoys[1])
print "free" + str(SevenEightBoys[2])
print "breast" + str(SevenEightBoys[3])
print "back" + str(SevenEightBoys[4])
print "fly" + str(SevenEightBoys[5])
print "im" + str(SevenEightBoys[6])