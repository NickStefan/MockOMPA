#!/usr/bin/python

# MockOMPA
# Uses: 
# <> fully quantified knowlegde of team strengths and weaknesses
# <> program runnable at any time of the season, good for tracking team improvemts
# <> just for fun, the total scores can be like the BCS of OMPA swimming
# code written and designed by Nick Stefan

# functions to be imported to MockOMPA.py

# to add a team, add their name to the SwimTeamList variable, check loadscrapydata, and add their names into the LafOMPA version of the loadscrapydata() function (it takes more than one json)


def getSec(s):

# this function handles 1:09.22Y into 69.22 (turns minutes into seconds 
# and rids the Y or ! from the crg database)   

    try:
        try: 
            y = s.split('Y')
            l = y[0].split(':')
            r = float(l[0]) * 60 + float(l[1])
        except ValueError:
            try: 
                y = s.split('!')
                l = y[0].split(':')
                r = float(l[0]) * 60 + float(l[1])
            except IndexError:
                y = s.split('!')
                r = float(y[0])
        except IndexError:
            try:
                y = s.split('Y')
                r = float(y[0])
            except ValueError:
                y = s.split('!')
                r = float(y[0])
    except AttributeError:
        r = s
    return r
#



def LoadScrapyData(jsonscrapy):

# this function loads the names, age, team and time data from json file from say "sixundergirlsfreestyle".
# it removes non-OMPA teams (and could be modified to remove OMPA teams for interesting data mining)
# it (by using getSec() and other code) converts '1:09.22Y' str into something more usable like 69.22 float

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
    # datelist = []
    
    for swimmers in json_data:
        namelist.extend(swimmers["names"])
        agelist.extend(swimmers["age"])
        teamlist.extend(swimmers["team"])
        timelist.extend(swimmers["time"])
        # try:
#             datelist.extend(swimmers["date"])
#         except KeyError:
#             pass
   
    # gets rid of swimmers from wrong teams who sometimes find there way into the database
    # for some reason the team filter needs to be run twice! 
    # it works on one team fine, but with say: swims == "OCC" or swims == "SH" will take out all SH and all but 1 OCC.
    for swims in teamlist:
        swimmerID = teamlist.index(swims)
        if swims == "LMYA" or swims == "" or swims == "LMYA":
            del namelist[swimmerID]
            del agelist[swimmerID]
            del teamlist[swimmerID]
            del timelist[swimmerID]
            # del datelist[swimmerID]
        for swimmers2 in teamlist:
            swimmerID2 = teamlist.index(swimmers2)
            if swimmers2 == "LMYA" or swimmers2 == "LMYA" or swimmers2 == "":
                del namelist[swimmerID2]
                del agelist[swimmerID2]
                del teamlist[swimmerID2]
                del timelist[swimmerID2]
                # del datelist[swimmerID2]
    
    # for dates in datelist:
    #     dateID = datelist.index(dates)
    #     if dates contain "2012":
    #             del namelist[swimmerID]
    #             del agelist[swimmerID]
    #             del teamlist[swimmerID]
    #             del timelist[swimmerID]
    #             del datelist[swimmerID]
    #         for swimmers2 in teamlist:
    #             swimmerID2 = teamlist.index(swimmers2)
    #             if swimmers2 == "2012":
    #                 del namelist[swimmerID2]
    #                 del agelist[swimmerID2]
    #                 del teamlist[swimmerID2]
    #                 del timelist[swimmerID2]
    #                 del datelist[swimmerID]
                
        # fixes the "21.05y" into an actual float
        for times in timelist:
            timeID = timelist.index(times)
            timelist[timeID]= float(re.match(r'[-+]?\d*\.\d+|\d+', str(getSec(times))).group())
    
    #returns a tuple. so to print only the list of names: print namelist[0]
    return namelist, agelist, teamlist, timelist

#

def LoadScrapyData2(jsonscrapy,jsonscrapy2,jsonscrapy3):

# this function loads the names, age, team and time data from json file from say "sixundergirlsfreestyle".
# it removes non-OMPA teams (and could be modified to remove OMPA teams for interesting data mining)
# it (by using getSec() and other code) converts '1:09.22Y' str into something more usable like 69.22 float

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
    # datelist = []
    
    for swimmers in json_data:
        namelist.extend(swimmers["names"])
        agelist.extend(swimmers["age"])
        teamlist.extend(swimmers["team"])
        timelist.extend(swimmers["time"])
        # try:
#             datelist.extend(swimmers["date"])
#         except KeyError:
#             pass

    with open(jsonscrapy2) as json_file2:
        json_data2 = json.load(json_file2)
        json_data2 = ast.literal_eval(json.dumps(json_data2))
    
    for swimmers in json_data2:
        namelist.extend(swimmers["names"])
        agelist.extend(swimmers["age"])
        teamlist.extend(swimmers["team"])
        timelist.extend(swimmers["time"])
        
    with open(jsonscrapy3) as json_file3:
        json_data3 = json.load(json_file3)
        json_data3 = ast.literal_eval(json.dumps(json_data3))
    
    for swimmers in json_data3:
        namelist.extend(swimmers["names"])
        agelist.extend(swimmers["age"])
        teamlist.extend(swimmers["team"])
        timelist.extend(swimmers["time"])
   
    # gets rid of swimmers from wrong teams who sometimes find there way into the database
    # for some reason the team filter needs to be run twice! 
    # it works on one team fine, but with say: swims == "OCC" or swims == "SH" will take out all SH and all but 1 OCC.
    for swims in teamlist:
        swimmerID = teamlist.index(swims)
        if swims == "LMYA" or swims == "" or swims == "LMYA":
            del namelist[swimmerID]
            del agelist[swimmerID]
            del teamlist[swimmerID]
            del timelist[swimmerID]
            # del datelist[swimmerID]
        for swimmers2 in teamlist:
            swimmerID2 = teamlist.index(swimmers2)
            if swimmers2 == "LMYA" or swimmers2 == "LMYA" or swimmers2 == "":
                del namelist[swimmerID2]
                del agelist[swimmerID2]
                del teamlist[swimmerID2]
                del timelist[swimmerID2]
                # del datelist[swimmerID2]
    
    # for dates in datelist:
    #     dateID = datelist.index(dates)
    #     if dates contain "2012":
    #             del namelist[swimmerID]
    #             del agelist[swimmerID]
    #             del teamlist[swimmerID]
    #             del timelist[swimmerID]
    #             del datelist[swimmerID]
    #         for swimmers2 in teamlist:
    #             swimmerID2 = teamlist.index(swimmers2)
    #             if swimmers2 == "2012":
    #                 del namelist[swimmerID2]
    #                 del agelist[swimmerID2]
    #                 del teamlist[swimmerID2]
    #                 del timelist[swimmerID2]
    #                 del datelist[swimmerID]
                
        # fixes the "21.05y" into an actual float
        for times in timelist:
            timeID = timelist.index(times)
            timelist[timeID]= float(re.match(r'[-+]?\d*\.\d+|\d+', str(getSec(times))).group())
    
    #returns a tuple. so to print only the list of names: print namelist[0]
    return namelist, agelist, teamlist, timelist





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
                ScrapyIM[3].append(1000)
        OutputIM.append(ScrapyIM[3][imid])
        
    return ScrapyFree[0],ScrapyFree[2],ScrapyFree[3],OutputBreast, OutputBack, OutputFly, OutputIM
#




def SortTeamSwimmers(AgeGroupGender,SwimTeamList):
    # this function sorts the list of all agegroupgender swimmers, and sorts them into team lists:
    # 9 teams. ie:
    # TeamAgeGroupGender[0] (will contain a list of SH swimmers as a list of dictionaries), 
    # TeamAgeGroupGender[1] (will contain a list of OCC swimmers as a list of dictionaries),
    # etc
    # each swimmer dictionary contains the keys of free, breast, back, fly and im.
    # the values that correspond to each key is that swimmers swim time

    TeamAgeGroupGender = [[] for i in range(len(SwimTeamList))]
    
    #for each swimmername in the list
    for swimmer in AgeGroupGender[0]:
        #index rank of each swimmer name
        swimmerID = AgeGroupGender[0].index(swimmer)
        
        for swimteams in SwimTeamList:
            teamid = SwimTeamList.index(swimteams)
            
            if AgeGroupGender[1][swimmerID] == swimteams:
                 TeamAgeGroupGender[teamid].append({"Free":AgeGroupGender[2][swimmerID],
                 "Breast":AgeGroupGender[3][swimmerID],"Back":AgeGroupGender[4][swimmerID],
                 "Fly":AgeGroupGender[5][swimmerID],"IM":AgeGroupGender[6][swimmerID]})
        
        # # SH
#         if AgeGroupGender[1][swimmerID] == SwimTeamList:
#              TeamAgeGroupGender[0].append({"Free":AgeGroupGender[2][swimmerID],
#              "Breast":AgeGroupGender[3][swimmerID],"Back":AgeGroupGender[4][swimmerID],
#              "Fly":AgeGroupGender[5][swimmerID],"IM":AgeGroupGender[6][swimmerID]})
#         # OCC
#         elif AgeGroupGender[1][swimmerID] == "OCC":
#              TeamAgeGroupGender[1].append({"Free":AgeGroupGender[2][swimmerID],
#              "Breast":AgeGroupGender[3][swimmerID],"Back":AgeGroupGender[4][swimmerID],
#              "Fly":AgeGroupGender[5][swimmerID],"IM":AgeGroupGender[6][swimmerID]})
#         # PARK
#         elif AgeGroupGender[1][swimmerID] == "PARK":
#              TeamAgeGroupGender[2].append({"Free":AgeGroupGender[2][swimmerID],
#              "Breast":AgeGroupGender[3][swimmerID],"Back":AgeGroupGender[4][swimmerID],
#              "Fly":AgeGroupGender[5][swimmerID],"IM":AgeGroupGender[6][swimmerID]})
#         # MEAD
#         elif AgeGroupGender[1][swimmerID] == "MEAD":
#              TeamAgeGroupGender[3].append({"Free":AgeGroupGender[2][swimmerID],
#              "Breast":AgeGroupGender[3][swimmerID],"Back":AgeGroupGender[4][swimmerID],
#              "Fly":AgeGroupGender[5][swimmerID],"IM":AgeGroupGender[6][swimmerID]})
#         # MVP
#         elif AgeGroupGender[1][swimmerID] == "MVP":
#              TeamAgeGroupGender[4].append({"Free":AgeGroupGender[2][swimmerID],
#              "Breast":AgeGroupGender[3][swimmerID],"Back":AgeGroupGender[4][swimmerID],
#              "Fly":AgeGroupGender[5][swimmerID],"IM":AgeGroupGender[6][swimmerID]})
#         # MIRA
#         elif AgeGroupGender[1][swimmerID] == "MIRA":
#              TeamAgeGroupGender[5].append({"Free":AgeGroupGender[2][swimmerID],
#              "Breast":AgeGroupGender[3][swimmerID],"Back":AgeGroupGender[4][swimmerID],
#              "Fly":AgeGroupGender[5][swimmerID],"IM":AgeGroupGender[6][swimmerID]})
#         # MCC
#         elif AgeGroupGender[1][swimmerID] == "MCC":
#              TeamAgeGroupGender[6].append({"Free":AgeGroupGender[2][swimmerID],
#              "Breast":AgeGroupGender[3][swimmerID],"Back":AgeGroupGender[4][swimmerID],
#              "Fly":AgeGroupGender[5][swimmerID],"IM":AgeGroupGender[6][swimmerID]})
#         # MRSC
#         elif AgeGroupGender[1][swimmerID] == "MRSC":
#              TeamAgeGroupGender[7].append({"Free":AgeGroupGender[2][swimmerID],
#              "Breast":AgeGroupGender[3][swimmerID],"Back":AgeGroupGender[4][swimmerID],
#              "Fly":AgeGroupGender[5][swimmerID],"IM":AgeGroupGender[6][swimmerID]})
#         # CCC
#         elif AgeGroupGender[1][swimmerID] == "CCC":
#              TeamAgeGroupGender[8].append({"Free":AgeGroupGender[2][swimmerID],
#              "Breast":AgeGroupGender[3][swimmerID],"Back":AgeGroupGender[4][swimmerID],
#              "Fly":AgeGroupGender[5][swimmerID],"IM":AgeGroupGender[6][swimmerID]})
    
    return TeamAgeGroupGender

#




def PickEvents(TeamAgeGroupGender,countylist):
    # the online database has best times for up to all 5 events, but in the real ompa,
    # 7/up only swim 3 events and 6/under only swim 2.
    # this function takes everyones times, "temporarily" divides them by the county time,
    # the largest numbers in relation to the county times mean that its that swimmers
    # worst stroke. their two worst strokes are then replaced with 1000 seconds so that
    # while they can be entered into every event, they would only potentially score
    # in their best events. 6/unders already have their im times set to 0 or 1, and thus
    # im is never picked as one of their "slowest" events. this is okay, as that event is
    # simply not scored during the scoring section of the program
    
    for teams in TeamAgeGroupGender:
        for swimmerdict in teams:
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
            elif backtest > freetest and freetest > imtest and imtest > flytest and flytest > breasttest:
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
    
    return TeamAgeGroupGender

#





def FillEvent(TeamAgeGroupGender,SwimTeamList): 
    # this takes the lists of swimmer sorted by teams, and then uses them to fill up each event with swimmers
    # so that they then can be scored in the next part of the program
    
    AgeGroupStroke = [[],[],[],[],[]]
    swimevents = ["Free","Breast","Back","Fly","IM"]
    
    for event in swimevents:
        eventid = swimevents.index(event)
        
        for SwimTeams in SwimTeamList:
            teamid = SwimTeamList.index(SwimTeams)
        
            for swimmers in TeamAgeGroupGender[teamid]:
                swimmerID = TeamAgeGroupGender[teamid].index(swimmers)
                AgeGroupStroke[eventid].append({SwimTeams:TeamAgeGroupGender[teamid][swimmerID][event]})
   
    
#         for swimmers in TeamAgeGroupGender[0]:
#             swimmerID = TeamAgeGroupGender[0].index(swimmers)
#             AgeGroupStroke[eventid].append({"SH":TeamAgeGroupGender[0][swimmerID][event]})
#
#       # for swimmers in TeamAgeGroupGender[1]:
#             swimmerID = TeamAgeGroupGender[1].index(swimmers)
#             AgeGroupStroke[eventid].append({"OCC":TeamAgeGroupGender[1][swimmerID][event]})
#     
#         for swimmers in TeamAgeGroupGender[2]:
#             swimmerID = TeamAgeGroupGender[2].index(swimmers)
#             AgeGroupStroke[eventid].append({"PARK":TeamAgeGroupGender[2][swimmerID][event]})
#      
#         for swimmers in TeamAgeGroupGender[3]:
#             swimmerID = TeamAgeGroupGender[3].index(swimmers)
#             AgeGroupStroke[eventid].append({"MEAD":TeamAgeGroupGender[3][swimmerID][event]})
#         
#         for swimmers in TeamAgeGroupGender[4]:
#            swimmerID = TeamAgeGroupGender[4].index(swimmers)
#            AgeGroupStroke[eventid].append({"MVP":TeamAgeGroupGender[4][swimmerID][event]})
#        
#         for swimmers in TeamAgeGroupGender[5]:
#            swimmerID = TeamAgeGroupGender[5].index(swimmers)
#            AgeGroupStroke[eventid].append({"MIRA":TeamAgeGroupGender[5][swimmerID][event]})
#     
#         for swimmers in TeamAgeGroupGender[6]:
#            swimmerID = TeamAgeGroupGender[6].index(swimmers)
#            AgeGroupStroke[eventid].append({"MCC":TeamAgeGroupGender[6][swimmerID][event]})
#         
#         for swimmers in TeamAgeGroupGender[7]:
#            swimmerID = TeamAgeGroupGender[7].index(swimmers)
#            AgeGroupStroke[eventid].append({"MRSC":TeamAgeGroupGender[7][swimmerID][event]})
#     
#         for swimmers in TeamAgeGroupGender[8]:
#            swimmerID = TeamAgeGroupGender[8].index(swimmers)
#            AgeGroupStroke[eventid].append({"CCC":TeamAgeGroupGender[8][swimmerID][event]})
    
        AgeGroupStroke[eventid] = sorted(AgeGroupStroke[eventid], key=lambda k: k.values())    
    return AgeGroupStroke
    
##

def FillFreeRelay(TeamAgeGroupGender,SwimTeamList): 
    # this takes the lists of swimmer sorted by teams, and then uses them to fill up each event with swimmers
    # so that they then can be scored in the next part of the program
     
    AgeGroupStroke = []
    LegsOneTwo = {}
    LegsThreeFou = {}
    
    RelayPlaceHolder = [[] for i in range(len(SwimTeamList))]
          
    for SwimTeams in SwimTeamList:
        # RelayPlaceHolder.append(empty)
        teamid = SwimTeamList.index(SwimTeams)
        
        for swimmers in TeamAgeGroupGender[teamid]:
            swimmerID = TeamAgeGroupGender[teamid].index(swimmers)
            RelayPlaceHolder[teamid].append({SwimTeams:TeamAgeGroupGender[teamid][swimmerID]["Free"]})
            
        RelayPlaceHolder[teamid] = sorted(RelayPlaceHolder[teamid], key=lambda k: k.values()) 
        try:
            LegsOneTwo = AddTwoDictionaries(RelayPlaceHolder[teamid][0],RelayPlaceHolder[teamid][1])
            LegsThreeFour = AddTwoDictionaries(RelayPlaceHolder[teamid][2],RelayPlaceHolder[teamid][3])
            AgeGroupStroke.append(AddTwoDictionaries(LegsOneTwo,LegsThreeFour))
        except IndexError:
            norelay = {}
            norelay[SwimTeams] = 1000
            AgeGroupStroke.append(norelay)
    AgeGroupStroke = sorted(AgeGroupStroke, key=lambda k: k.values())
    
    return AgeGroupStroke
##

def CreateOutPutFile():
    filename = raw_input("What would you like to name the output file? (no extensions): ")
    with open(str(filename + ".txt"), "w") as f:
        f.write(str(filename)+ "\n")
        f.close
        return str(filename + ".txt")
##

def ScoreEvent(AgeGroupStroke, AgeGroupPoints, AgeGroupStrokePoints, ScoringScheme, SwimTeamList):
    # the event is scored and loaded into global agegroupgender_points dictionaries,
    # it returns a list of the event results (ie 1st place swimmer, 2nd place swimmer etc)
    
    eventresults = []
    
    # for each dictionary contained in the list
    for swimmers in AgeGroupStroke:
        # index rank of each dictionary contained in the list
        swimmerID = AgeGroupStroke.index(swimmers)
        
        for swimteams in SwimTeamList:
  # SH
  # if the key "SH" is in the dictionary, and the index is less than 20 (index 0-19 score) 
            if swimteams in swimmers and swimmerID < 20:
              eventresults.append((str(swimmerID+1) + " " + str(swimmers) + " Points:" + str(ScoringScheme[swimmerID]) + "\n"))
              if swimteams in AgeGroupPoints:
                  AgeGroupPoints[swimteams] = AgeGroupPoints[swimteams] + ScoringScheme[swimmerID]
              else:
                   AgeGroupPoints[swimteams] = ScoringScheme[swimmerID]
              if swimteams in AgeGroupStrokePoints:
                  AgeGroupStrokePoints[swimteams] = AgeGroupStrokePoints[swimteams] + ScoringScheme[swimmerID]
              else:
                  AgeGroupStrokePoints[swimteams] = ScoringScheme[swimmerID]
            # if SH doesnt have anyone in the 0-19 index, still create an entry of {"SH":0}. this avoids errors later
            else:
              if swimteams in AgeGroupPoints:
                  AgeGroupPoints[swimteams] = AgeGroupPoints[swimteams] + 0
              else:
                  AgeGroupPoints[swimteams] = 0
              if  swimteams in AgeGroupStrokePoints:
                  AgeGroupStrokePoints[swimteams] = AgeGroupStrokePoints[swimteams] + 0
              else:
                  AgeGroupStrokePoints[swimteams] = 0  
    
        # # SH
#         # if the key "SH" is in the dictionary, and the index is less than 20 (index 0-19 score) 
#         if "SH" in swimmers and swimmerID < 20:
#             eventresults.append((str(swimmerID+1) + " " + str(swimmers) + " Points:" + str(ScoringScheme[swimmerID]) + "\n"))
#             if "SH" in AgeGroupPoints:
#                 AgeGroupPoints["SH"] = AgeGroupPoints["SH"] + ScoringScheme[swimmerID]
#             else:
#                  AgeGroupPoints["SH"] = ScoringScheme[swimmerID]
#             if "SH" in AgeGroupStrokePoints:
#                 AgeGroupStrokePoints["SH"] = AgeGroupStrokePoints["SH"] + ScoringScheme[swimmerID]
#             else:
#                 AgeGroupStrokePoints["SH"] = ScoringScheme[swimmerID]
#         # if SH doesnt have anyone in the 0-19 index, still create an entry of {"SH":0}. this avoids errors later
#         else:
#             if "SH" in AgeGroupPoints:
#                 AgeGroupPoints["SH"] = AgeGroupPoints["SH"] + 0
#             else:
#                 AgeGroupPoints["SH"] = 0
#             if  "SH" in AgeGroupStrokePoints:
#                 AgeGroupStrokePoints["SH"] = AgeGroupStrokePoints["SH"] + 0
#             else:
#                 AgeGroupStrokePoints["SH"] = 0
#         # OCC
#         if "OCC" in swimmers and swimmerID < 20:
#             eventresults.append((str(swimmerID+1) + " " + str(swimmers) + " Points:" + str(ScoringScheme[swimmerID]) + "\n"))
#             if "OCC" in AgeGroupPoints:
#                 AgeGroupPoints["OCC"] = AgeGroupPoints["OCC"] + ScoringScheme[swimmerID]
#             else:
#                  AgeGroupPoints["OCC"] = ScoringScheme[swimmerID]
#             if "OCC" in AgeGroupStrokePoints:
#                 AgeGroupStrokePoints["OCC"] = AgeGroupStrokePoints["OCC"] + ScoringScheme[swimmerID]
#             else:
#                 AgeGroupStrokePoints["OCC"] = ScoringScheme[swimmerID]
#         else:
#             if "OCC" in AgeGroupPoints:
#                 AgeGroupPoints["OCC"] = AgeGroupPoints["OCC"] + 0
#             else:
#                 AgeGroupPoints["OCC"] = 0
#             if  "OCC" in AgeGroupStrokePoints:
#                 AgeGroupStrokePoints["OCC"] = AgeGroupStrokePoints["OCC"] + 0
#             else:
#                 AgeGroupStrokePoints["OCC"] = 0
#         # PARK
#         if "PARK" in swimmers and swimmerID < 20:
#             eventresults.append((str(swimmerID+1) + " " + str(swimmers) + " Points:" + str(ScoringScheme[swimmerID]) + "\n"))
#             if "PARK" in AgeGroupPoints:
#                 AgeGroupPoints["PARK"] = AgeGroupPoints["PARK"] + ScoringScheme[swimmerID]
#             else:
#                  AgeGroupPoints["PARK"] = ScoringScheme[swimmerID]
#             if "PARK" in AgeGroupStrokePoints:
#                 AgeGroupStrokePoints["PARK"] = AgeGroupStrokePoints["PARK"] + ScoringScheme[swimmerID]
#             else:
#                 AgeGroupStrokePoints["PARK"] = ScoringScheme[swimmerID]
#         else:
#             if "PARK" in AgeGroupPoints:
#                 AgeGroupPoints["PARK"] = AgeGroupPoints["PARK"] + 0
#             else:
#                 AgeGroupPoints["PARK"] = 0
#             if  "PARK" in AgeGroupStrokePoints:
#                 AgeGroupStrokePoints["PARK"] = AgeGroupStrokePoints["PARK"] + 0
#             else:
#                 AgeGroupStrokePoints["PARK"] = 0
#         # MEAD
#         if "MEAD" in swimmers and swimmerID < 20:
#             eventresults.append((str(swimmerID+1) + " " + str(swimmers) + " Points:" + str(ScoringScheme[swimmerID]) + "\n"))
#             if "MEAD" in AgeGroupPoints:
#                 AgeGroupPoints["MEAD"] = AgeGroupPoints["MEAD"] + ScoringScheme[swimmerID]
#             else:
#                  AgeGroupPoints["MEAD"] = ScoringScheme[swimmerID]
#             if "MEAD" in AgeGroupStrokePoints:
#                 AgeGroupStrokePoints["MEAD"] = AgeGroupStrokePoints["MEAD"] + ScoringScheme[swimmerID]
#             else:
#                 AgeGroupStrokePoints["MEAD"] = ScoringScheme[swimmerID]
#         else:
#             if "MEAD" in AgeGroupPoints:
#                 AgeGroupPoints["MEAD"] = AgeGroupPoints["MEAD"] + 0
#             else:
#                 AgeGroupPoints["MEAD"] = 0
#             if  "MEAD" in AgeGroupStrokePoints:
#                 AgeGroupStrokePoints["MEAD"] = AgeGroupStrokePoints["MEAD"] + 0
#             else:
#                 AgeGroupStrokePoints["MEAD"] = 0
#         # MVP
#         if "MVP" in swimmers and swimmerID < 20:
#             eventresults.append((str(swimmerID+1) + " " + str(swimmers) + " Points:" + str(ScoringScheme[swimmerID]) + "\n"))
#             if "MVP" in AgeGroupPoints:
#                 AgeGroupPoints["MVP"] = AgeGroupPoints["MVP"] + ScoringScheme[swimmerID]
#             else:
#                  AgeGroupPoints["MVP"] = ScoringScheme[swimmerID]
#             if "MVP" in AgeGroupStrokePoints:
#                 AgeGroupStrokePoints["MVP"] = AgeGroupStrokePoints["MVP"] + ScoringScheme[swimmerID]
#             else:
#                 AgeGroupStrokePoints["MVP"] = ScoringScheme[swimmerID]
#         else:
#             if "MVP" in AgeGroupPoints:
#                 AgeGroupPoints["MVP"] = AgeGroupPoints["MVP"] + 0
#             else:
#                 AgeGroupPoints["MVP"] = 0
#             if  "MVP" in AgeGroupStrokePoints:
#                 AgeGroupStrokePoints["MVP"] = AgeGroupStrokePoints["MVP"] + 0
#             else:
#                 AgeGroupStrokePoints["MVP"] = 0
#         # MIRA
#         if "MIRA" in swimmers and swimmerID < 20:
#             eventresults.append((str(swimmerID+1) + " " + str(swimmers) + " Points:" + str(ScoringScheme[swimmerID]) + "\n"))
#             if "MIRA" in AgeGroupPoints:
#                 AgeGroupPoints["MIRA"] = AgeGroupPoints["MIRA"] + ScoringScheme[swimmerID]
#             else:
#                  AgeGroupPoints["MIRA"] = ScoringScheme[swimmerID]
#             if "MIRA" in AgeGroupStrokePoints:
#                 AgeGroupStrokePoints["MIRA"] = AgeGroupStrokePoints["MIRA"] + ScoringScheme[swimmerID]
#             else:
#                 AgeGroupStrokePoints["MIRA"] = ScoringScheme[swimmerID]
#         else:
#             if "MIRA" in AgeGroupPoints:
#                 AgeGroupPoints["MIRA"] = AgeGroupPoints["MIRA"] + 0
#             else:
#                 AgeGroupPoints["MIRA"] = 0
#             if  "MIRA" in AgeGroupStrokePoints:
#                 AgeGroupStrokePoints["MIRA"] = AgeGroupStrokePoints["MIRA"] + 0
#             else:
#                 AgeGroupStrokePoints["MIRA"] = 0
#         # MCC
#         if "MCC" in swimmers and swimmerID < 20:
#             eventresults.append((str(swimmerID+1) + " " + str(swimmers) + " Points:" + str(ScoringScheme[swimmerID]) + "\n"))
#             if "MCC" in AgeGroupPoints:
#                 AgeGroupPoints["MCC"] = AgeGroupPoints["MCC"] + ScoringScheme[swimmerID]
#             else:
#                  AgeGroupPoints["MCC"] = ScoringScheme[swimmerID]
#             if "MCC" in AgeGroupStrokePoints:
#                 AgeGroupStrokePoints["MCC"] = AgeGroupStrokePoints["MCC"] + ScoringScheme[swimmerID]
#             else:
#                 AgeGroupStrokePoints["MCC"] = ScoringScheme[swimmerID]
#         else:
#             if "MCC" in AgeGroupPoints:
#                 AgeGroupPoints["MCC"] = AgeGroupPoints["MCC"] + 0
#             else:
#                 AgeGroupPoints["MCC"] = 0
#             if  "MCC" in AgeGroupStrokePoints:
#                 AgeGroupStrokePoints["MCC"] = AgeGroupStrokePoints["MCC"] + 0
#             else:
#                 AgeGroupStrokePoints["MCC"] = 0
#         # MRSC
#         if "MRSC" in swimmers and swimmerID < 20:
#             eventresults.append((str(swimmerID+1) + " " + str(swimmers) + " Points:" + str(ScoringScheme[swimmerID]) + "\n"))
#             if "MRSC" in AgeGroupPoints:
#                 AgeGroupPoints["MRSC"] = AgeGroupPoints["MRSC"] + ScoringScheme[swimmerID]
#             else:
#                  AgeGroupPoints["MRSC"] = ScoringScheme[swimmerID]
#             if "MRSC" in AgeGroupStrokePoints:
#                 AgeGroupStrokePoints["MRSC"] = AgeGroupStrokePoints["MRSC"] + ScoringScheme[swimmerID]
#             else:
#                 AgeGroupStrokePoints["MRSC"] = ScoringScheme[swimmerID]
#         else:
#             if "MRSC" in AgeGroupPoints:
#                 AgeGroupPoints["MRSC"] = AgeGroupPoints["MRSC"] + 0
#             else:
#                 AgeGroupPoints["MRSC"] = 0
#             if  "MRSC" in AgeGroupStrokePoints:
#                 AgeGroupStrokePoints["MRSC"] = AgeGroupStrokePoints["MRSC"] + 0
#             else:
#                 AgeGroupStrokePoints["MRSC"] = 0
#         # CCC
#         if "CCC" in swimmers and swimmerID < 20:
#             eventresults.append((str(swimmerID+1) + " " + str(swimmers) + " Points:" + str(ScoringScheme[swimmerID]) + "\n"))
#             if "CCC" in AgeGroupPoints:
#                 AgeGroupPoints["CCC"] = AgeGroupPoints["CCC"] + ScoringScheme[swimmerID]
#             else:
#                  AgeGroupPoints["CCC"] = ScoringScheme[swimmerID]
#             if "CCC" in AgeGroupStrokePoints:
#                 AgeGroupStrokePoints["CCC"] = AgeGroupStrokePoints["CCC"] + ScoringScheme[swimmerID]
#             else:
#                 AgeGroupStrokePoints["CCC"] = ScoringScheme[swimmerID]
#         else:
#             if "CCC" in AgeGroupPoints:
#                 AgeGroupPoints["CCC"] = AgeGroupPoints["CCC"] + 0
#             else:
#                 AgeGroupPoints["CCC"] = 0
#             if  "CCC" in AgeGroupStrokePoints:
#                 AgeGroupStrokePoints["CCC"] = AgeGroupStrokePoints["CCC"] + 0
#             else:
#                 AgeGroupStrokePoints["CCC"] = 0
    return eventresults
    
#









def OrderedScores(AgeGroupPoints):
    # this turns the AgeGroupPoints into an orderd tuple. Using this inside the ScoreEvent() 
    # doesnt work because the ordered tuples cant be continiously added to like the key can in a dictionary. 
    # thus they remain unordered dictionaries in most of the program
    
    OrderedScores = sorted(AgeGroupPoints.items(), key=lambda x: x[1], reverse = True)
    return OrderedScores


#






def AddTwoDictionaries(PointsOne,PointsTwo):
    # use this to total up a teams fly points (ie add their 6ugirls fly, 6u boys fly, 78girls fly etc)
    
    TotalPoints = dict(PointsOne.items() + PointsTwo.items())
    for keys in TotalPoints:
        TotalPoints[keys] = PointsOne[keys] + PointsTwo[keys]
    return TotalPoints

#

def TotalPoints(SixUnderGirls,SixUnderBoys,SevenEightGirls,SevenEightBoys,
NineTenGirls,NineTenBoys,ElevenTwelveGirls,ElevenTwelveBoys,ThirteenFourteenGirls,ThirteenFourteenBoys,FifteenEighteenGirls,FifteenEighteenBoys):

    
    SixUnder = AddTwoDictionaries(SixUnderGirls,SixUnderBoys)
    
    
    SevenEight = AddTwoDictionaries(SevenEightGirls,SevenEightBoys)
    
  
    NineTen = AddTwoDictionaries(NineTenGirls,NineTenBoys)
    
   
    ElevenTwelve = AddTwoDictionaries(ElevenTwelveGirls,ElevenTwelveBoys)
    
    
    ThirteenFourteen = AddTwoDictionaries(ThirteenFourteenGirls,ThirteenFourteenBoys)
    
   
    FifteenEighteen = AddTwoDictionaries(FifteenEighteenGirls,FifteenEighteenBoys)
    
   
    EightUnder = AddTwoDictionaries(SixUnder,SevenEight)
    
    
    NineTwelve = AddTwoDictionaries(NineTen,ElevenTwelve)
    
    ThirteenUp = AddTwoDictionaries(ThirteenFourteen,FifteenEighteen)
    
    TotalPointCount = AddTwoDictionaries(AddTwoDictionaries(EightUnder,NineTwelve),ThirteenUp)

    return TotalPointCount



