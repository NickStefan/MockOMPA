#!/usr/bin/python

# MockOMPA
# Uses: 
# <> fully quantified knowlegde of team strengths and weaknesses
# <> program runnable at any time of the season, good for tracking team improvemts
# <> just for fun, the total scores can be like the BCS of OMPA swimming
# <> can run the meet with certain teams removed
# <> can remove all but two teams to simulate a dualmeet
# <> can toggle dual meet scoring or ompa scoring
# code written and designed by Nick Stefan


# the flow of data in this program is as such:
# ompascrapymanager.py is run at the command line separate from this program
# the .json files from ompascrapymanager.py are fed into LoadScrapyData()
# LoadScrappyData() -> ReOrderStrokes() -> SortTeamSwimmers() -> PickEvents() -> FillEvents()
# variables loaded from FillEvents() are then evaluated with ScoreEvent()
# ScoreEvent() also prints out event results (ie 1st place swimmer, 2nd place swimmer etc)

# various points dictionaries stated in ompapresetvariables module are then added and totaled
# in various ways to give information such as total team points, team fly points, team 6/u girls points etc
# AddTwoDictionaries() helps with the totaling of these different dictionaries
# OrderedScores() is a formating tool for printing, but really isnt used to affect program variables


import ompapresetvariables as ov
import ompafunctions as ofunc

# more information about each function can be read in the ompafunctions module.

# load scrapy data
# six under girls
SixUnderGirlsFreestyle = ofunc.LoadScrapyData("sixundergirlsfree.json")
SixUnderGirlsBreastroke = ofunc.LoadScrapyData("sixundergirlsbreast.json")
SixUnderGirlsBackstroke = ofunc.LoadScrapyData("sixundergirlsback.json")
SixUnderGirlsButterfly = ofunc.LoadScrapyData("sixundergirlsfly.json")
SixUnderGirlsIM = [[],[],[],[]]

# six under boys
SixUnderBoysFreestyle = ofunc.LoadScrapyData("sixunderboysfree.json")
SixUnderBoysBreastroke = ofunc.LoadScrapyData("sixunderboysbreast.json")
SixUnderBoysBackstroke = ofunc.LoadScrapyData("sixunderboysback.json")
SixUnderBoysButterfly = ofunc.LoadScrapyData("sixunderboysfly.json")
SixUnderBoysIM = [[],[],[],[]]

# seven eight girls
SevenEightGirlsFreestyle = ofunc.LoadScrapyData("seveneightgirlsfree.json")
SevenEightGirlsBreastroke = ofunc.LoadScrapyData("seveneightgirlsbreast.json")
SevenEightGirlsBackstroke = ofunc.LoadScrapyData("seveneightgirlsback.json")
SevenEightGirlsButterfly = ofunc.LoadScrapyData("seveneightgirlsfly.json")
SevenEightGirlsIM = ofunc.LoadScrapyData("seveneightgirlsim.json")

# seven eight boys
SevenEightBoysFreestyle = ofunc.LoadScrapyData("seveneightboysfree.json")
SevenEightBoysBreastroke = ofunc.LoadScrapyData("seveneightboysbreast.json")
SevenEightBoysBackstroke = ofunc.LoadScrapyData("seveneightboysback.json")
SevenEightBoysButterfly = ofunc.LoadScrapyData("seveneightboysfly.json")
SevenEightBoysIM = ofunc.LoadScrapyData("seveneightboysim.json")

# nine ten girls
NineTenGirlsFreestyle = ofunc.LoadScrapyData("ninetengirlsfree.json")
NineTenGirlsBreastroke = ofunc.LoadScrapyData("ninetengirlsbreast.json")
NineTenGirlsBackstroke = ofunc.LoadScrapyData("ninetengirlsback.json")
NineTenGirlsButterfly = ofunc.LoadScrapyData("ninetengirlsfly.json")
NineTenGirlsIM = ofunc.LoadScrapyData("ninetengirlsim.json")

# nine ten boys
NineTenBoysFreestyle = ofunc.LoadScrapyData("ninetenboysfree.json")
NineTenBoysBreastroke = ofunc.LoadScrapyData("ninetenboysbreast.json")
NineTenBoysBackstroke = ofunc.LoadScrapyData("ninetenboysback.json")
NineTenBoysButterfly = ofunc.LoadScrapyData("ninetenboysfly.json")
NineTenBoysIM = ofunc.LoadScrapyData("ninetenboysim.json")

# eleven twelve girls
ElevenTwelveGirlsFreestyle = ofunc.LoadScrapyData("eleventwelvegirlsfree.json")
ElevenTwelveGirlsBreastroke = ofunc.LoadScrapyData("eleventwelvegirlsbreast.json")
ElevenTwelveGirlsBackstroke = ofunc.LoadScrapyData("eleventwelvegirlsback.json")
ElevenTwelveGirlsButterfly = ofunc.LoadScrapyData("eleventwelvegirlsfly.json")
ElevenTwelveGirlsIM = ofunc.LoadScrapyData("eleventwelvegirlsim.json")

# eleven twelve boys
ElevenTwelveBoysFreestyle = ofunc.LoadScrapyData("eleventwelveboysfree.json")
ElevenTwelveBoysBreastroke = ofunc.LoadScrapyData("eleventwelveboysbreast.json")
ElevenTwelveBoysBackstroke = ofunc.LoadScrapyData("eleventwelveboysback.json")
ElevenTwelveBoysButterfly = ofunc.LoadScrapyData("eleventwelveboysfly.json")
ElevenTwelveBoysIM = ofunc.LoadScrapyData("eleventwelveboysim.json")

# thirteen fourteen girls
ThirteenFourteenGirlsFreestyle = ofunc.LoadScrapyData("thirteenfourteengirlsfree.json")
ThirteenFourteenGirlsBreastroke = ofunc.LoadScrapyData("thirteenfourteengirlsbreast.json")
ThirteenFourteenGirlsBackstroke = ofunc.LoadScrapyData("thirteenfourteengirlsback.json")
ThirteenFourteenGirlsButterfly = ofunc.LoadScrapyData("thirteenfourteengirlsfly.json")
ThirteenFourteenGirlsIM = ofunc.LoadScrapyData("thirteenfourteengirlsim.json")

# thirteen fourteen boys
ThirteenFourteenBoysFreestyle = ofunc.LoadScrapyData("thirteenfourteenboysfree.json")
ThirteenFourteenBoysBreastroke = ofunc.LoadScrapyData("thirteenfourteenboysbreast.json")
ThirteenFourteenBoysBackstroke = ofunc.LoadScrapyData("thirteenfourteenboysback.json")
ThirteenFourteenBoysButterfly = ofunc.LoadScrapyData("thirteenfourteenboysfly.json")
ThirteenFourteenBoysIM = ofunc.LoadScrapyData("thirteenfourteenboysim.json")

# fifteen eighteen girls
FifteenEighteenGirlsFreestyle = ofunc.LoadScrapyData("fifteeneighteengirlsfree.json")
FifteenEighteenGirlsBreastroke = ofunc.LoadScrapyData("fifteeneighteengirlsbreast.json")
FifteenEighteenGirlsBackstroke = ofunc.LoadScrapyData("fifteeneighteengirlsback.json")
FifteenEighteenGirlsButterfly = ofunc.LoadScrapyData("fifteeneighteengirlsfly.json")
FifteenEighteenGirlsIM = ofunc.LoadScrapyData("fifteeneighteengirlsim.json")

# fifteen eighteen boys
FifteenEighteenBoysFreestyle = ofunc.LoadScrapyData("fifteeneighteenboysfree.json")
FifteenEighteenBoysBreastroke = ofunc.LoadScrapyData("fifteeneighteenboysbreast.json")
FifteenEighteenBoysBackstroke = ofunc.LoadScrapyData("fifteeneighteenboysback.json")
FifteenEighteenBoysButterfly = ofunc.LoadScrapyData("fifteeneighteenboysfly.json")
FifteenEighteenBoysIM = ofunc.LoadScrapyData("fifteeneighteenboysim.json")

# use this to check LoadScrapyData
# print "========================"
# print "6/u girls Free Scrapy"
# print "========================"
# print "Name"
# print SixUnderGirlsFreestyle[0]
# print "========================"
# print "Age"
# print SixUnderGirlsFreestyle[1]
# print "========================"
# print "Team"
# print SixUnderGirlsFreestyle[2]
# print "========================"
# print "Time"
# print SixUnderGirlsFreestyle[3]
# print "========================"



# re order strokes
# takes in each stroke and resorts it according to the freestyle name index
# it also checks to see if there are top 50 kids in an event who aren't in freestyle 
# so that all of their swims can be indexed to their freestyle name like everyone else
# it then makes sure that everyone has a dummy time for any events they're missing

SixUnderGirls = ofunc.ReOrderStrokes(SixUnderGirlsFreestyle,SixUnderGirlsBreastroke,SixUnderGirlsBackstroke,SixUnderGirlsButterfly,SixUnderGirlsIM)
SixUnderBoys = ofunc.ReOrderStrokes(SixUnderBoysFreestyle,SixUnderBoysBreastroke,SixUnderBoysBackstroke,SixUnderBoysButterfly,SixUnderBoysIM)
SevenEightBoys = ofunc.ReOrderStrokes(SevenEightBoysFreestyle,SevenEightBoysBreastroke,SevenEightBoysBackstroke,SevenEightBoysButterfly,SevenEightBoysIM)
SevenEightGirls = ofunc.ReOrderStrokes(SevenEightGirlsFreestyle,SevenEightGirlsBreastroke,SevenEightGirlsBackstroke,SevenEightGirlsButterfly,SevenEightGirlsIM)
NineTenGirls = ofunc.ReOrderStrokes(NineTenGirlsFreestyle,NineTenGirlsBreastroke,NineTenGirlsBackstroke,NineTenGirlsButterfly,NineTenGirlsIM)
NineTenBoys = ofunc.ReOrderStrokes(NineTenBoysFreestyle,NineTenBoysBreastroke,NineTenBoysBackstroke,NineTenBoysButterfly,NineTenBoysIM)
ElevenTwelveGirls = ofunc.ReOrderStrokes(ElevenTwelveGirlsFreestyle,ElevenTwelveGirlsBreastroke,ElevenTwelveGirlsBackstroke,ElevenTwelveGirlsButterfly,ElevenTwelveGirlsIM)
ElevenTwelveBoys = ofunc.ReOrderStrokes(ElevenTwelveBoysFreestyle,ElevenTwelveBoysBreastroke,ElevenTwelveBoysBackstroke,ElevenTwelveBoysButterfly,ElevenTwelveBoysIM)
ThirteenFourteenGirls = ofunc.ReOrderStrokes(ThirteenFourteenGirlsFreestyle,ThirteenFourteenGirlsBreastroke,ThirteenFourteenGirlsBackstroke,ThirteenFourteenGirlsButterfly,ThirteenFourteenGirlsIM)
ThirteenFourteenBoys = ofunc.ReOrderStrokes(ThirteenFourteenBoysFreestyle,ThirteenFourteenBoysBreastroke,ThirteenFourteenBoysBackstroke,ThirteenFourteenBoysButterfly,ThirteenFourteenBoysIM)
FifteenEighteenGirls = ofunc.ReOrderStrokes(FifteenEighteenGirlsFreestyle,FifteenEighteenGirlsBreastroke,FifteenEighteenGirlsBackstroke,FifteenEighteenGirlsButterfly,FifteenEighteenGirlsIM)
FifteenEighteenBoys = ofunc.ReOrderStrokes(FifteenEighteenBoysFreestyle,FifteenEighteenBoysBreastroke,FifteenEighteenBoysBackstroke,FifteenEighteenBoysButterfly,FifteenEighteenBoysIM)

# use this to check ReOrderStrokes(), that each list within the SixUnderGirls is contains correct info in correct order
# print "========================"
# print "6 and Under Girls"
# print "Re-Ordered Scrapy data"
# print "========================"
# print "names"
# print str(SixUnderGirls[0])
# print "========================"
# print "team"
# print str(SixUnderGirls[1])
# print "========================"
# print "free"
# print str(SixUnderGirls[2])
# print "========================"
# print "breast"
# print str(SixUnderGirls[3])
# print "========================"
# print "back"
# print str(SixUnderGirls[4])
# print "========================"
# print "fly"
# print str(SixUnderGirls[5])
# print "========================"
# print "im"
# print str(SixUnderGirls[6])
# print "========================"




# sort team swimmers
# Load the swimmers Free, Breast, Back, Fly, IM times into the correct team swimmer list (a list of 1 dictionary per swimmer)

TeamSixUnderGirls = ofunc.SortTeamSwimmers(SixUnderGirls,ov.SwimTeamList)
TeamSixUnderBoys = ofunc.SortTeamSwimmers(SixUnderBoys,ov.SwimTeamList)
TeamSevenEightGirls = ofunc.SortTeamSwimmers(SevenEightGirls,ov.SwimTeamList)
TeamSevenEightBoys = ofunc.SortTeamSwimmers(SevenEightBoys,ov.SwimTeamList)
TeamNineTenGirls = ofunc.SortTeamSwimmers(NineTenGirls,ov.SwimTeamList)
TeamNineTenBoys = ofunc.SortTeamSwimmers(NineTenBoys,ov.SwimTeamList)
TeamElevenTwelveGirls = ofunc.SortTeamSwimmers(ElevenTwelveGirls,ov.SwimTeamList)
TeamElevenTwelveBoys = ofunc.SortTeamSwimmers(ElevenTwelveBoys,ov.SwimTeamList)
TeamThirteenFourteenGirls = ofunc.SortTeamSwimmers(ThirteenFourteenGirls,ov.SwimTeamList)
TeamThirteenFourteenBoys = ofunc.SortTeamSwimmers(ThirteenFourteenBoys,ov.SwimTeamList)
TeamFifteenEighteenGirls = ofunc.SortTeamSwimmers(FifteenEighteenGirls,ov.SwimTeamList)
TeamFifteenEighteenBoys = ofunc.SortTeamSwimmers(FifteenEighteenBoys,ov.SwimTeamList)


# Use this to check SortTeamSwimmers(), that each team list within TeamSixUnderGirls is a list of dictionaries, 
# each dictionary with one swimmer's times

# print "========================"
# print "6/under swimmer lists"
# print "========================"
# print "SH List"
# print TeamSixUnderGirls[0]
# print "========================"
# print "OCC List"
# print TeamSixUnderGirls[1]
# print "========================"
# print "PARK List"
# print TeamSixUnderGirls[2]
# print "========================"
# print "MEAD List"
# print TeamSixUnderGirls[3]
# print "========================"
# print "MVP List"
# print TeamSixUnderGirls[4]
# print "========================"
# print "MIRA List"
# print TeamSixUnderGirls[5]
# print "========================"
# print "MCC List"
# print TeamSixUnderGirls[6]
# print "========================"
# print "MRSC List"
# print TeamSixUnderGirls[7]
# print "========================"
# print "CCC List"
# print TeamSixUnderGirls[8]
# print "========================"

# pick the relays happens before pick events, because we want all available time to pick the
# best relays. if we wait until after pick events, then some freestyle times will be covered up
# by the individual event selection process.

SixUnderGirlsFreeRelay = ofunc.FillFreeRelay(TeamSixUnderGirls,ov.SwimTeamList)
SixUnderBoysFreeRelay = ofunc.FillFreeRelay(TeamSixUnderBoys,ov.SwimTeamList)

SevenEightGirlsFreeRelay = ofunc.FillFreeRelay(TeamSevenEightGirls,ov.SwimTeamList)
SevenEightBoysFreeRelay = ofunc.FillFreeRelay(TeamSevenEightBoys,ov.SwimTeamList)

NineTenGirlsFreeRelay = ofunc.FillFreeRelay(TeamNineTenGirls,ov.SwimTeamList)
NineTenBoysFreeRelay = ofunc.FillFreeRelay(TeamNineTenBoys,ov.SwimTeamList)

ElevenTwelveGirlsFreeRelay = ofunc.FillFreeRelay(TeamElevenTwelveGirls,ov.SwimTeamList)
ElevenTwelveBoysFreeRelay = ofunc.FillFreeRelay(TeamElevenTwelveBoys,ov.SwimTeamList)

ThirteenFourteenGirlsFreeRelay = ofunc.FillFreeRelay(TeamThirteenFourteenGirls,ov.SwimTeamList)
ThirteenFourteenBoysFreeRelay = ofunc.FillFreeRelay(TeamThirteenFourteenBoys,ov.SwimTeamList)

FifteenEighteenGirlsFreeRelay = ofunc.FillFreeRelay(TeamFifteenEighteenGirls,ov.SwimTeamList)
FifteenEighteenBoysFreeRelay = ofunc.FillFreeRelay(TeamFifteenEighteenBoys,ov.SwimTeamList)



# pick events
# We will enter every swimmer into every event, but "simulate" only swimming the OMPA allowed number of events
# by changing their "worst" strokes into 1000 seconds (ie last place and no points for those events)
# we will select "worst" strokes by dividing each stroke by the county time. the largest numbers are "worst".
# the "division" process only permanently effects the bad strokes.
# because six and under are only able to swim 2 events, IM is automatically made their "fastest" stroke,
# that way their actual two worst strokes are turned into 1000 seconds. then we make sure not to score
# 6 under IM.

TeamSixUnderGirls = ofunc.PickEvents(TeamSixUnderGirls,ov.SixUnderGirlsCounty)
TeamSixUnderBoys = ofunc.PickEvents(TeamSixUnderBoys,ov.SixUnderBoysCounty)
TeamSevenEightGirls = ofunc.PickEvents(TeamSevenEightGirls,ov.SevenEightGirlsCounty)
TeamSevenEightBoys = ofunc.PickEvents(TeamSevenEightBoys,ov.SevenEightBoysCounty)
TeamNineTenGirls = ofunc.PickEvents(TeamNineTenGirls,ov.NineTenGirlsCounty)
TeamNineTenBoys = ofunc.PickEvents(TeamNineTenBoys,ov.NineTenBoysCounty)
TeamElevenTwelveGirls = ofunc.PickEvents(TeamElevenTwelveGirls,ov.ElevenTwelveGirlsCounty)
TeamElevenTwelveBoys = ofunc.PickEvents(TeamElevenTwelveBoys,ov.ElevenTwelveBoysCounty)
TeamThirteenFourteenGirls = ofunc.PickEvents(TeamThirteenFourteenGirls,ov.ThirteenFourteenGirlsCounty)
TeamThirteenFourteenBoys = ofunc.PickEvents(TeamThirteenFourteenBoys,ov.ThirteenFourteenBoysCounty)
TeamFifteenEighteenGirls = ofunc.PickEvents(TeamFifteenEighteenGirls,ov.FifteenEighteenBoysCounty)
TeamFifteenEighteenBoys = ofunc.PickEvents(TeamFifteenEighteenBoys,ov.FifteenEighteenBoysCounty)


# Use this to check PickEvents(), that each team list within TeamSixUnderGirls is a list of dictionaries,
# each dictionary with one swimmers time's and that their two worst events are 1000 seconds
# print "========================"
# print "6/under Entries"
# print "========================"
# print "SH EntriesEntries"
# print TeamSixUnderGirls[0]
# print "========================"
# print "OCC Entries"
# print TeamSixUnderGirls[1]
# print "========================"
# print "PARK Entries"
# print TeamSixUnderGirls[2]
# print "========================"
# print "MEAD Entries"
# print TeamSixUnderGirls[3]
# print "========================"
# print "MVP Entries"
# print TeamSixUnderGirls[4]
# print "========================"
# print "MIRA Entries"
# print TeamSixUnderGirls[5]
# print "========================"
# print "MCC Entries"
# print TeamSixUnderGirls[6]
# print "========================"
# print "MRSC Entries"
# print TeamSixUnderGirls[7]
# print "========================"
# print "CCC Entries"
# print TeamSixUnderGirls[8]
# print "========================"



# This takes the team lists of swimmer dictionaries and actually enters them into every event
# because we changed everyone's worst strokes into 1000 seconds with PickEvents(), it properly simulates only
# swimming your best events.

SixUnderGirlsEvents = ofunc.FillEvent(TeamSixUnderGirls,ov.SwimTeamList)
SixUnderBoysEvents = ofunc.FillEvent(TeamSixUnderBoys,ov.SwimTeamList)
SevenEightGirlsEvents = ofunc.FillEvent(TeamSevenEightGirls,ov.SwimTeamList)
SevenEightBoysEvents = ofunc.FillEvent(TeamSevenEightBoys,ov.SwimTeamList)
NineTenGirlsEvents = ofunc.FillEvent(TeamNineTenGirls,ov.SwimTeamList)
NineTenBoysEvents = ofunc.FillEvent(TeamNineTenBoys,ov.SwimTeamList)
ElevenTwelveGirlsEvents = ofunc.FillEvent(TeamElevenTwelveGirls,ov.SwimTeamList)
ElevenTwelveBoysEvents = ofunc.FillEvent(TeamElevenTwelveBoys,ov.SwimTeamList)
ThirteenFourteenGirlsEvents = ofunc.FillEvent(TeamThirteenFourteenGirls,ov.SwimTeamList)
ThirteenFourteenBoysEvents = ofunc.FillEvent(TeamThirteenFourteenBoys,ov.SwimTeamList)
FifteenEighteenGirlsEvents = ofunc.FillEvent(TeamFifteenEighteenGirls,ov.SwimTeamList)
FifteenEighteenBoysEvents = ofunc.FillEvent(TeamFifteenEighteenBoys,ov.SwimTeamList)



# scoring the meet
# the function ScoreEvent() will load a score into an a global variable age group scoring dictionary as a secondary action.
# it will return (and load a variable) as a list of the event results (1st place swimmer, 2nd place swimmer etc)
# that can be written by looping through the list with a f.write

SixUnderGirls_Free = ofunc.ScoreEvent(SixUnderGirlsEvents[0], ov.SixUnderGirls_Points, ov.SixUnderGirls_Free_Points, ov.ScoringScheme1, ov.SwimTeamList)
SixUnderGirls_Breast = ofunc.ScoreEvent(SixUnderGirlsEvents[1], ov.SixUnderGirls_Points, ov.SixUnderGirls_Breast_Points, ov.ScoringScheme1, ov.SwimTeamList)
SixUnderGirls_Back = ofunc.ScoreEvent(SixUnderGirlsEvents[2], ov.SixUnderGirls_Points, ov.SixUnderGirls_Back_Points, ov.ScoringScheme1, ov.SwimTeamList)
SixUnderGirls_Fly = ofunc.ScoreEvent(SixUnderGirlsEvents[3], ov.SixUnderGirls_Points, ov.SixUnderGirls_Fly_Points, ov.ScoringScheme1, ov.SwimTeamList)

SixUnderBoys_Free = ofunc.ScoreEvent(SixUnderBoysEvents[0], ov.SixUnderBoys_Points, ov.SixUnderBoys_Free_Points, ov.ScoringScheme1, ov.SwimTeamList)
SixUnderBoys_Breast = ofunc.ScoreEvent(SixUnderBoysEvents[1], ov.SixUnderBoys_Points, ov.SixUnderBoys_Breast_Points, ov.ScoringScheme1, ov.SwimTeamList)
SixUnderBoys_Back = ofunc.ScoreEvent(SixUnderBoysEvents[2], ov.SixUnderBoys_Points, ov.SixUnderBoys_Back_Points, ov.ScoringScheme1, ov.SwimTeamList)
SixUnderBoys_Fly = ofunc.ScoreEvent(SixUnderBoysEvents[3], ov.SixUnderBoys_Points, ov.SixUnderBoys_Fly_Points, ov.ScoringScheme1, ov.SwimTeamList)

SevenEightGirls_Free = ofunc.ScoreEvent(SevenEightGirlsEvents[0], ov.SevenEightGirls_Points, ov.SevenEightGirls_Free_Points, ov.ScoringScheme1, ov.SwimTeamList)
SevenEightGirls_Breast = ofunc.ScoreEvent(SevenEightGirlsEvents[1], ov.SevenEightGirls_Points, ov.SevenEightGirls_Breast_Points, ov.ScoringScheme1, ov.SwimTeamList)
SevenEightGirls_Back = ofunc.ScoreEvent(SevenEightGirlsEvents[2], ov.SevenEightGirls_Points, ov.SevenEightGirls_Back_Points, ov.ScoringScheme1, ov.SwimTeamList)
SevenEightGirls_Fly = ofunc.ScoreEvent(SevenEightGirlsEvents[3], ov.SevenEightGirls_Points, ov.SevenEightGirls_Fly_Points, ov.ScoringScheme1, ov.SwimTeamList)
SevenEightGirls_IM = ofunc.ScoreEvent(SevenEightGirlsEvents[4], ov.SevenEightGirls_Points, ov.SevenEightGirls_IM_Points, ov.ScoringScheme1, ov.SwimTeamList)

SevenEightBoys_Free = ofunc.ScoreEvent(SevenEightBoysEvents[0], ov.SevenEightBoys_Points, ov.SevenEightBoys_Free_Points, ov.ScoringScheme1, ov.SwimTeamList)
SevenEightBoys_Breast = ofunc.ScoreEvent(SevenEightBoysEvents[1], ov.SevenEightBoys_Points, ov.SevenEightBoys_Breast_Points, ov.ScoringScheme1, ov.SwimTeamList)
SevenEightBoys_Back = ofunc.ScoreEvent(SevenEightBoysEvents[2], ov.SevenEightBoys_Points, ov.SevenEightBoys_Back_Points, ov.ScoringScheme1, ov.SwimTeamList)
SevenEightBoys_Fly = ofunc.ScoreEvent(SevenEightBoysEvents[3], ov.SevenEightBoys_Points, ov.SevenEightBoys_Fly_Points, ov.ScoringScheme1, ov.SwimTeamList)
SevenEightBoys_IM = ofunc.ScoreEvent(SevenEightBoysEvents[4], ov.SevenEightBoys_Points, ov.SevenEightBoys_IM_Points, ov.ScoringScheme1, ov.SwimTeamList)

NineTenGirls_Free = ofunc.ScoreEvent(NineTenGirlsEvents[0], ov.NineTenGirls_Points, ov.NineTenGirls_Free_Points, ov.ScoringScheme1, ov.SwimTeamList)
NineTenGirls_Breast = ofunc.ScoreEvent(NineTenGirlsEvents[1], ov.NineTenGirls_Points, ov.NineTenGirls_Breast_Points, ov.ScoringScheme1, ov.SwimTeamList)
NineTenGirls_Back = ofunc.ScoreEvent(NineTenGirlsEvents[2], ov.NineTenGirls_Points, ov.NineTenGirls_Back_Points, ov.ScoringScheme1, ov.SwimTeamList)
NineTenGirls_Fly = ofunc.ScoreEvent(NineTenGirlsEvents[3], ov.NineTenGirls_Points, ov.NineTenGirls_Fly_Points, ov.ScoringScheme1, ov.SwimTeamList)
NineTenGirls_IM = ofunc.ScoreEvent(NineTenGirlsEvents[4], ov.NineTenGirls_Points, ov.NineTenGirls_IM_Points, ov.ScoringScheme1, ov.SwimTeamList)

NineTenBoys_Free = ofunc.ScoreEvent(NineTenBoysEvents[0], ov.NineTenBoys_Points, ov.NineTenBoys_Free_Points, ov.ScoringScheme1, ov.SwimTeamList)
NineTenBoys_Breast = ofunc.ScoreEvent(NineTenBoysEvents[1], ov.NineTenBoys_Points, ov.NineTenBoys_Breast_Points, ov.ScoringScheme1, ov.SwimTeamList)
NineTenBoys_Back = ofunc.ScoreEvent(NineTenBoysEvents[2], ov.NineTenBoys_Points, ov.NineTenBoys_Back_Points, ov.ScoringScheme1, ov.SwimTeamList)
NineTenBoys_Fly = ofunc.ScoreEvent(NineTenBoysEvents[3], ov.NineTenBoys_Points, ov.NineTenBoys_Fly_Points, ov.ScoringScheme1, ov.SwimTeamList)
NineTenBoys_IM = ofunc.ScoreEvent(NineTenBoysEvents[4], ov.NineTenBoys_Points, ov.NineTenBoys_IM_Points, ov.ScoringScheme1, ov.SwimTeamList)

ElevenTwelveGirls_Free = ofunc.ScoreEvent(ElevenTwelveGirlsEvents[0], ov.ElevenTwelveGirls_Points, ov.ElevenTwelveGirls_Free_Points, ov.ScoringScheme1, ov.SwimTeamList)
ElevenTwelveGirls_Breast = ofunc.ScoreEvent(ElevenTwelveGirlsEvents[1], ov.ElevenTwelveGirls_Points, ov.ElevenTwelveGirls_Breast_Points, ov.ScoringScheme1, ov.SwimTeamList)
ElevenTwelveGirls_Back = ofunc.ScoreEvent(ElevenTwelveGirlsEvents[2], ov.ElevenTwelveGirls_Points, ov.ElevenTwelveGirls_Back_Points, ov.ScoringScheme1, ov.SwimTeamList)
ElevenTwelveGirls_Fly = ofunc.ScoreEvent(ElevenTwelveGirlsEvents[3], ov.ElevenTwelveGirls_Points, ov.ElevenTwelveGirls_Fly_Points, ov.ScoringScheme1, ov.SwimTeamList)
ElevenTwelveGirls_IM = ofunc.ScoreEvent(ElevenTwelveGirlsEvents[4], ov.ElevenTwelveGirls_Points, ov.ElevenTwelveGirls_IM_Points, ov.ScoringScheme1, ov.SwimTeamList)

ElevenTwelveBoys_Free = ofunc.ScoreEvent(ElevenTwelveBoysEvents[0], ov.ElevenTwelveBoys_Points, ov.ElevenTwelveBoys_Free_Points, ov.ScoringScheme1, ov.SwimTeamList)
ElevenTwelveBoys_Breast = ofunc.ScoreEvent(ElevenTwelveBoysEvents[1], ov.ElevenTwelveBoys_Points, ov.ElevenTwelveBoys_Breast_Points, ov.ScoringScheme1, ov.SwimTeamList)
ElevenTwelveBoys_Back = ofunc.ScoreEvent(ElevenTwelveBoysEvents[2], ov.ElevenTwelveBoys_Points, ov.ElevenTwelveBoys_Back_Points, ov.ScoringScheme1, ov.SwimTeamList)
ElevenTwelveBoys_Fly = ofunc.ScoreEvent(ElevenTwelveBoysEvents[3], ov.ElevenTwelveBoys_Points, ov.ElevenTwelveBoys_Fly_Points, ov.ScoringScheme1, ov.SwimTeamList)
ElevenTwelveBoys_IM = ofunc.ScoreEvent(ElevenTwelveBoysEvents[4], ov.ElevenTwelveBoys_Points, ov.ElevenTwelveBoys_IM_Points, ov.ScoringScheme1, ov.SwimTeamList)

ThirteenFourteenGirls_Free = ofunc.ScoreEvent(ThirteenFourteenGirlsEvents[0], ov.ThirteenFourteenGirls_Points, ov.ThirteenFourteenGirls_Free_Points, ov.ScoringScheme1, ov.SwimTeamList)
ThirteenFourteenGirls_Breast = ofunc.ScoreEvent(ThirteenFourteenGirlsEvents[1], ov.ThirteenFourteenGirls_Points, ov.ThirteenFourteenGirls_Breast_Points, ov.ScoringScheme1, ov.SwimTeamList)
ThirteenFourteenGirls_Back = ofunc.ScoreEvent(ThirteenFourteenGirlsEvents[2], ov.ThirteenFourteenGirls_Points, ov.ThirteenFourteenGirls_Back_Points, ov.ScoringScheme1, ov.SwimTeamList)
ThirteenFourteenGirls_Fly = ofunc.ScoreEvent(ThirteenFourteenGirlsEvents[3], ov.ThirteenFourteenGirls_Points, ov.ThirteenFourteenGirls_Fly_Points, ov.ScoringScheme1, ov.SwimTeamList)
ThirteenFourteenGirls_IM = ofunc.ScoreEvent(ThirteenFourteenGirlsEvents[4], ov.ThirteenFourteenGirls_Points, ov.ThirteenFourteenGirls_IM_Points, ov.ScoringScheme1, ov.SwimTeamList)

ThirteenFourteenBoys_Free = ofunc.ScoreEvent(ThirteenFourteenBoysEvents[0], ov.ThirteenFourteenBoys_Points, ov.ThirteenFourteenBoys_Free_Points, ov.ScoringScheme1, ov.SwimTeamList)
ThirteenFourteenBoys_Breast = ofunc.ScoreEvent(ThirteenFourteenBoysEvents[1], ov.ThirteenFourteenBoys_Points, ov.ThirteenFourteenBoys_Breast_Points, ov.ScoringScheme1, ov.SwimTeamList)
ThirteenFourteenBoys_Back = ofunc.ScoreEvent(ThirteenFourteenBoysEvents[2], ov.ThirteenFourteenBoys_Points, ov.ThirteenFourteenBoys_Back_Points, ov.ScoringScheme1, ov.SwimTeamList)
ThirteenFourteenBoys_Fly = ofunc.ScoreEvent(ThirteenFourteenBoysEvents[3], ov.ThirteenFourteenBoys_Points, ov.ThirteenFourteenBoys_Fly_Points, ov.ScoringScheme1, ov.SwimTeamList)
ThirteenFourteenBoys_IM = ofunc.ScoreEvent(ThirteenFourteenBoysEvents[4], ov.ThirteenFourteenBoys_Points, ov.ThirteenFourteenBoys_IM_Points, ov.ScoringScheme1, ov.SwimTeamList)

FifteenEighteenGirls_Free = ofunc.ScoreEvent(FifteenEighteenGirlsEvents[0], ov.FifteenEighteenGirls_Points, ov.FifteenEighteenGirls_Free_Points, ov.ScoringScheme1, ov.SwimTeamList)
FifteenEighteenGirls_Breast = ofunc.ScoreEvent(FifteenEighteenGirlsEvents[1], ov.FifteenEighteenGirls_Points, ov.FifteenEighteenGirls_Breast_Points, ov.ScoringScheme1, ov.SwimTeamList)
FifteenEighteenGirls_Back = ofunc.ScoreEvent(FifteenEighteenGirlsEvents[2], ov.FifteenEighteenGirls_Points, ov.FifteenEighteenGirls_Back_Points, ov.ScoringScheme1, ov.SwimTeamList)
FifteenEighteenGirls_Fly = ofunc.ScoreEvent(FifteenEighteenGirlsEvents[3], ov.FifteenEighteenGirls_Points, ov.FifteenEighteenGirls_Fly_Points, ov.ScoringScheme1, ov.SwimTeamList)
FifteenEighteenGirls_IM = ofunc.ScoreEvent(FifteenEighteenGirlsEvents[4], ov.FifteenEighteenGirls_Points, ov.FifteenEighteenGirls_IM_Points, ov.ScoringScheme1, ov.SwimTeamList)

FifteenEighteenBoys_Free = ofunc.ScoreEvent(FifteenEighteenBoysEvents[0], ov.FifteenEighteenBoys_Points, ov.FifteenEighteenBoys_Free_Points, ov.ScoringScheme1, ov.SwimTeamList)
FifteenEighteenBoys_Breast = ofunc.ScoreEvent(FifteenEighteenBoysEvents[1], ov.FifteenEighteenBoys_Points, ov.FifteenEighteenBoys_Breast_Points, ov.ScoringScheme1, ov.SwimTeamList)
FifteenEighteenBoys_Back = ofunc.ScoreEvent(FifteenEighteenBoysEvents[2], ov.FifteenEighteenBoys_Points, ov.FifteenEighteenBoys_Back_Points, ov.ScoringScheme1, ov.SwimTeamList)
FifteenEighteenBoys_Fly = ofunc.ScoreEvent(FifteenEighteenBoysEvents[3], ov.FifteenEighteenBoys_Points, ov.FifteenEighteenBoys_Fly_Points, ov.ScoringScheme1, ov.SwimTeamList)
FifteenEighteenBoys_IM = ofunc.ScoreEvent(FifteenEighteenBoysEvents[4], ov.FifteenEighteenBoys_Points, ov.FifteenEighteenBoys_IM_Points, ov.ScoringScheme1, ov.SwimTeamList)

SixUnderGirls_FreeRelay = ofunc.ScoreEvent(SixUnderGirlsFreeRelay, ov.SixUnderGirls_Points, ov.SixUnderGirls_FreeRelay_Points, ov.ScoringScheme2, ov.SwimTeamList)
SixUnderBoys_FreeRelay = ofunc.ScoreEvent(SixUnderBoysFreeRelay, ov.SixUnderBoys_Points, ov.SixUnderBoys_FreeRelay_Points, ov.ScoringScheme2, ov.SwimTeamList)
SevenEightGirls_FreeRelay = ofunc.ScoreEvent(SevenEightGirlsFreeRelay, ov.SevenEightGirls_Points, ov.SevenEightGirls_FreeRelay_Points, ov.ScoringScheme2, ov.SwimTeamList)
SevenEightBoys_FreeRelay = ofunc.ScoreEvent(SevenEightBoysFreeRelay, ov.SevenEightBoys_Points, ov.SevenEightBoys_FreeRelay_Points, ov.ScoringScheme2, ov.SwimTeamList)
NineTenGirls_FreeRelay = ofunc.ScoreEvent(NineTenGirlsFreeRelay, ov.NineTenGirls_Points, ov.NineTenGirls_FreeRelay_Points, ov.ScoringScheme2, ov.SwimTeamList)
NineTenBoys_FreeRelay = ofunc.ScoreEvent(NineTenBoysFreeRelay, ov.NineTenBoys_Points, ov.NineTenBoys_FreeRelay_Points, ov.ScoringScheme2, ov.SwimTeamList)
ElevenTwelveGirls_FreeRelay = ofunc.ScoreEvent(ElevenTwelveGirlsFreeRelay, ov.ElevenTwelveGirls_Points, ov.ElevenTwelveGirls_FreeRelay_Points, ov.ScoringScheme2, ov.SwimTeamList)
ElevenTwelveBoys_FreeRelay = ofunc.ScoreEvent(ElevenTwelveBoysFreeRelay, ov.ElevenTwelveBoys_Points, ov.ElevenTwelveBoys_FreeRelay_Points, ov.ScoringScheme2, ov.SwimTeamList)
ThirteenFourteenGirls_FreeRelay = ofunc.ScoreEvent(ThirteenFourteenGirlsFreeRelay, ov.ThirteenFourteenGirls_Points, ov.ThirteenFourteenGirls_FreeRelay_Points, ov.ScoringScheme2, ov.SwimTeamList)
ThirteenFourteenBoys_FreeRelay = ofunc.ScoreEvent(ThirteenFourteenBoysFreeRelay, ov.ThirteenFourteenBoys_Points, ov.ThirteenFourteenBoys_FreeRelay_Points, ov.ScoringScheme2, ov.SwimTeamList)
FifteenEighteenGirls_FreeRelay = ofunc.ScoreEvent(FifteenEighteenGirlsFreeRelay, ov.FifteenEighteenGirls_Points, ov.FifteenEighteenGirls_FreeRelay_Points, ov.ScoringScheme2, ov.SwimTeamList)
FifteenEighteenBoys_FreeRelay = ofunc.ScoreEvent(FifteenEighteenBoysFreeRelay, ov.FifteenEighteenBoys_Points, ov.FifteenEighteenBoys_FreeRelay_Points, ov.ScoringScheme2, ov.SwimTeamList)

# writing to output file
# the function ScoreEvent() will load a score into an a global variable age group scoring dictionary as a secondary action.
# it will return (and load a variable) as a list of the event results (1st place swimmer, 2nd place swimmer etc)
# that can be written by looping through the list with a f.write

# asks the user to define the name of the output text file (use does not need to include the extension)
file = ofunc.CreateOutPutFile()
filename = file
f = open(filename, "a")

f.write("========================================================================\n")
f.write("========================       MOCK OMPA        ========================\n")
f.write("========================================================================\n")
################
# Six under girls
################
f.write("\n")
f.write("========================\n")
f.write("6/Under Girls Free:\n")
f.write("========================\n")
for things in SixUnderGirls_Free:
    f.write(things)
f.write("\n")
f.write("6/Under Girls Free Points: \n")
f.write(str(ofunc.OrderedScores(ov.SixUnderGirls_Free_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("6/Under Girls Breast:\n")
f.write("========================\n")
for things in SixUnderGirls_Breast:
    f.write(things)
f.write("\n")
f.write("6/Under Girls Breast Points: \n")
f.write(str(ofunc.OrderedScores(ov.SixUnderGirls_Breast_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("6/Under Girls Back:\n")
f.write("========================\n")
for things in SixUnderGirls_Back:
    f.write(things)
f.write("\n")
f.write("6/Under Girls Back Points: \n")
f.write(str(ofunc.OrderedScores(ov.SixUnderGirls_Back_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("6/Under Girls Fly:\n")
f.write("========================\n")
for things in SixUnderGirls_Fly:
    f.write(things)
f.write("\n")
f.write("6/Under Girls Fly Points: \n")
f.write(str(ofunc.OrderedScores(ov.SixUnderGirls_Fly_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("6/Under Girls Free Relay:\n")
f.write("========================\n")
for things in SixUnderGirls_FreeRelay:
    f.write(things)
f.write("\n")
f.write("6/Under Girls Free Relay Points: \n")
f.write(str(ofunc.OrderedScores(ov.SixUnderGirls_FreeRelay_Points))+"\n")
f.write("\n")
################
# six under boys
################
f.write("========================\n")
f.write("6/Under Boys Free:\n")
f.write("========================\n")
for things in SixUnderBoys_Free:
    f.write(things)
f.write("\n")
f.write("6/Under Boys Free Points: \n")
f.write(str(ofunc.OrderedScores(ov.SixUnderBoys_Free_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("6/Under BoysBoys Breast:\n")
f.write("========================\n")
for things in SixUnderBoys_Breast:
    f.write(things)
f.write("\n")
f.write("6/Under Boys Breast Points: \n")
f.write(str(ofunc.OrderedScores(ov.SixUnderBoys_Breast_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("6/Under Boys Back:\n")
f.write("========================\n")
for things in SixUnderBoys_Back:
    f.write(things)
f.write("\n")
f.write("6/Under Boys Back Points: \n")
f.write(str(ofunc.OrderedScores(ov.SixUnderBoys_Back_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("6/Under Boys Fly:\n")
f.write("========================\n")
for things in SixUnderBoys_Fly:
    f.write(things)
f.write("\n")
f.write("6/Under Boys Fly Points: \n")
f.write(str(ofunc.OrderedScores(ov.SixUnderBoys_Fly_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("6/Under Boys Free Relay:\n")
f.write("========================\n")
for things in SixUnderBoys_FreeRelay:
    f.write(things)
f.write("\n")
f.write("6/Under Boys Free Relay Points: \n")
f.write(str(ofunc.OrderedScores(ov.SixUnderBoys_FreeRelay_Points))+"\n")
f.write("\n")
###############

################
# seven eight girls
################
f.write("========================\n")
f.write("7/8 Girls Free:\n")
f.write("========================\n")
for things in SevenEightGirls_Free:
    f.write(things)
f.write("\n")
f.write("7/8 Girls Free Points: \n")
f.write(str(ofunc.OrderedScores(ov.SevenEightGirls_Free_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("7/8 Girls Breast:\n")
f.write("========================\n")
for things in SevenEightGirls_Breast:
    f.write(things)
f.write("\n")
f.write("7/8 Girls Breast Points: \n")
f.write(str(ofunc.OrderedScores(ov.SevenEightGirls_Breast_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("7/8 Girls Back:\n")
f.write("========================\n")
for things in SevenEightGirls_Back:
    f.write(things)
f.write("\n")
f.write("7/8 Girls Back Points: \n")
f.write(str(ofunc.OrderedScores(ov.SevenEightGirls_Back_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("7/8 Girls Fly:\n")
f.write("========================\n")
for things in SevenEightGirls_Fly:
    f.write(things)
f.write("\n")
f.write("7/8 Girls Fly Points: \n")
f.write(str(ofunc.OrderedScores(ov.SevenEightGirls_Fly_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("7/8 Girls IM:\n")
f.write("========================\n")
for things in SevenEightGirls_IM:
    f.write(things)
f.write("\n")
f.write("7/8 Girls IM Points: \n")
f.write(str(ofunc.OrderedScores(ov.SevenEightGirls_IM_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("7/8 Girls Free Relay:\n")
f.write("========================\n")
for things in SevenEightGirls_FreeRelay:
    f.write(things)
f.write("\n")
f.write("7/8 Girls Free Relay Points: \n")
f.write(str(ofunc.OrderedScores(ov.SevenEightGirls_FreeRelay_Points))+"\n")
f.write("\n")
################
# seven eight boys
################
f.write("========================\n")
f.write("7/8 Boys Free:\n")
f.write("========================\n")
for things in SevenEightBoys_Free:
    f.write(things)
f.write("\n")
f.write("7/8 Boys Free Points: \n")
f.write(str(ofunc.OrderedScores(ov.SevenEightBoys_Free_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("7/8 Boys Breast:\n")
f.write("========================\n")
for things in SevenEightBoys_Breast:
    f.write(things)
f.write("\n")
f.write("7/8 Boys Breast Points: \n")
f.write(str(ofunc.OrderedScores(ov.SevenEightBoys_Breast_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("7/8 Boys Back:\n")
f.write("========================\n")
for things in SevenEightBoys_Back:
    f.write(things)
f.write("\n")
f.write("7/8 Boys Back Points: \n")
f.write(str(ofunc.OrderedScores(ov.SevenEightBoys_Back_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("7/8 Boys Fly:\n")
f.write("========================\n")
for things in SevenEightBoys_Fly:
    f.write(things)
f.write("\n")
f.write("7/8 Boys Fly Points: \n")
f.write(str(ofunc.OrderedScores(ov.SevenEightBoys_Fly_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("7/8 Boys IM:\n")
f.write("========================\n")
for things in SevenEightBoys_IM:
    f.write(things)
f.write("\n")
f.write("7/8 Boys IM Points: \n")
f.write(str(ofunc.OrderedScores(ov.SevenEightBoys_IM_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("7/8 Boys Free Relay:\n")
f.write("========================\n")
for things in SevenEightBoys_FreeRelay:
    f.write(things)
f.write("\n")
f.write("7/8 Boys Free Relay Points: \n")
f.write(str(ofunc.OrderedScores(ov.SevenEightBoys_FreeRelay_Points))+"\n")
f.write("\n")
###############

################
# nine ten girls
################
f.write("========================\n")
f.write("9/10 Girls Free:\n")
f.write("========================\n")
for things in NineTenGirls_Free:
    f.write(things)
f.write("\n")
f.write("9/10 Girls Free Points: \n")
f.write(str(ofunc.OrderedScores(ov.NineTenGirls_Free_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("9/10 Girls Breast:\n")
f.write("========================\n")
for things in NineTenGirls_Breast:
    f.write(things)
f.write("\n")
f.write("9/10 Girls Breast Points: \n")
f.write(str(ofunc.OrderedScores(ov.NineTenGirls_Breast_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("9/10 Girls Back:\n")
f.write("========================\n")
for things in NineTenGirls_Back:
    f.write(things)
f.write("\n")
f.write("9/10 Girls Back Points: \n")
f.write(str(ofunc.OrderedScores(ov.NineTenGirls_Back_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("9/10 Girls Fly:\n")
f.write("========================\n")
for things in NineTenGirls_Fly:
    f.write(things)
f.write("\n")
f.write("9/10 Girls Fly Points: \n")
f.write(str(ofunc.OrderedScores(ov.NineTenGirls_Fly_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("9/10 Girls IM:\n")
f.write("========================\n")
for things in NineTenGirls_IM:
    f.write(things)
f.write("\n")
f.write("9/10 Girls IM Points: \n")
f.write(str(ofunc.OrderedScores(ov.NineTenGirls_IM_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("9/10 Girls Free Relay:\n")
f.write("========================\n")
for things in NineTenGirls_FreeRelay:
    f.write(things)
f.write("\n")
f.write("9/10 Girls Free Relay Points: \n")
f.write(str(ofunc.OrderedScores(ov.NineTenGirls_FreeRelay_Points))+"\n")
f.write("\n")
################
# nine ten boys
################
f.write("========================\n")
f.write("9/10 Boys Free:\n")
f.write("========================\n")
for things in NineTenBoys_Free:
    f.write(things)
f.write("\n")
f.write("9/10 Boys Free Points: \n")
f.write(str(ofunc.OrderedScores(ov.NineTenBoys_Free_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("9/10 Boys Breast:\n")
f.write("========================\n")
for things in NineTenBoys_Breast:
    f.write(things)
f.write("\n")
f.write("9/10 Boys Breast Points: \n")
f.write(str(ofunc.OrderedScores(ov.NineTenBoys_Breast_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("9/10 Boys Back:\n")
f.write("========================\n")
for things in NineTenBoys_Back:
    f.write(things)
f.write("\n")
f.write("9/10 Boys Back Points: \n")
f.write(str(ofunc.OrderedScores(ov.NineTenBoys_Back_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("9/10 Boys Fly:\n")
f.write("========================\n")
for things in NineTenBoys_Fly:
    f.write(things)
f.write("\n")
f.write("9/10 Boys Fly Points: \n")
f.write(str(ofunc.OrderedScores(ov.NineTenBoys_Fly_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("9/10 Boys IM:\n")
f.write("========================\n")
for things in NineTenBoys_IM:
    f.write(things)
f.write("\n")
f.write("9/10 Boys IM Points: \n")
f.write(str(ofunc.OrderedScores(ov.NineTenBoys_IM_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("9/10 Boys Free Relay:\n")
f.write("========================\n")
for things in NineTenBoys_FreeRelay:
    f.write(things)
f.write("\n")
f.write("9/10 Boys Free Relay Points: \n")
f.write(str(ofunc.OrderedScores(ov.NineTenBoys_FreeRelay_Points))+"\n")
f.write("\n")
################

################
# eleven twelve girls
################
f.write("========================\n")
f.write("11/12 Girls Free:\n")
f.write("========================\n")
for things in ElevenTwelveGirls_Free:
    f.write(things)
f.write("\n")
f.write("11/12 Girls Free Points: \n")
f.write(str(ofunc.OrderedScores(ov.ElevenTwelveGirls_Free_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("11/12 Girls Breast:\n")
f.write("========================\n")
for things in ElevenTwelveGirls_Breast:
    f.write(things)
f.write("\n")
f.write("11/12 Girls Breast Points: \n")
f.write(str(ofunc.OrderedScores(ov.ElevenTwelveGirls_Breast_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("11/12 Girls Back:\n")
f.write("========================\n")
for things in ElevenTwelveGirls_Back:
    f.write(things)
f.write("\n")
f.write("11/12 Girls Back Points: \n")
f.write(str(ofunc.OrderedScores(ov.ElevenTwelveGirls_Back_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("11/12 Girls Fly:\n")
f.write("========================\n")
for things in ElevenTwelveGirls_Fly:
    f.write(things)
f.write("\n")
f.write("11/12 Girls Fly Points: \n")
f.write(str(ofunc.OrderedScores(ov.ElevenTwelveGirls_Fly_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("11/12 Girls IM:\n")
f.write("========================\n")
for things in ElevenTwelveGirls_IM:
    f.write(things)
f.write("\n")
f.write("11/12 Girls IM Points: \n")
f.write(str(ofunc.OrderedScores(ov.ElevenTwelveGirls_IM_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("11/12 Girls Free Relay:\n")
f.write("========================\n")
for things in ElevenTwelveGirls_FreeRelay:
    f.write(things)
f.write("\n")
f.write("11/12 Girls Free Relay Points: \n")
f.write(str(ofunc.OrderedScores(ov.ElevenTwelveGirls_FreeRelay_Points))+"\n")
f.write("\n")
################
# eleven twelve boys
################
f.write("========================\n")
f.write("11/12 Boys Free:\n")
f.write("========================\n")
for things in ElevenTwelveBoys_Free:
    f.write(things)
f.write("\n")
f.write("11/12 Boys Free Points: \n")
f.write(str(ofunc.OrderedScores(ov.ElevenTwelveBoys_Free_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("11/12 Boys Breast:\n")
f.write("========================\n")
for things in ElevenTwelveBoys_Breast:
    f.write(things)
f.write("\n")
f.write("11/12 Boys Breast Points: \n")
f.write(str(ofunc.OrderedScores(ov.ElevenTwelveBoys_Breast_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("11/12 Boys Back:\n")
f.write("========================\n")
for things in ElevenTwelveBoys_Back:
    f.write(things)
f.write("\n")
f.write("11/12 Boys Back Points: \n")
f.write(str(ofunc.OrderedScores(ov.ElevenTwelveBoys_Back_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("11/12 Boys Fly:\n")
f.write("========================\n")
for things in ElevenTwelveBoys_Fly:
    f.write(things)
f.write("\n")
f.write("11/12 Boys Fly Points: \n")
f.write(str(ofunc.OrderedScores(ov.ElevenTwelveBoys_Fly_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("11/12 Boys IM:\n")
f.write("========================\n")
for things in ElevenTwelveBoys_IM:
    f.write(things)
f.write("\n")
f.write("11/12 Boys IM Points: \n")
f.write(str(ofunc.OrderedScores(ov.ElevenTwelveBoys_IM_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("11/12 Boys Free Relay:\n")
f.write("========================\n")
for things in ElevenTwelveBoys_FreeRelay:
    f.write(things)
f.write("\n")
f.write("11/12 Boys Free Relay Points: \n")
f.write(str(ofunc.OrderedScores(ov.ElevenTwelveBoys_FreeRelay_Points))+"\n")
f.write("\n")
################

################
# thirteenfourteen girls
################
f.write("========================\n")
f.write("13/14 Girls Free:\n")
f.write("========================\n")
for things in ThirteenFourteenGirls_Free:
    f.write(things)
f.write("\n")
f.write("13/14 Girls Free Points: \n")
f.write(str(ofunc.OrderedScores(ov.ThirteenFourteenGirls_Free_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("13/14 Girls Breast:\n")
f.write("========================\n")
for things in ThirteenFourteenGirls_Breast:
    f.write(things)
f.write("\n")
f.write("13/14 Girls Breast Points: \n")
f.write(str(ofunc.OrderedScores(ov.ThirteenFourteenGirls_Breast_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("13/14 Girls Back:\n")
f.write("========================\n")
for things in ThirteenFourteenGirls_Back:
    f.write(things)
f.write("\n")
f.write("13/14 Girls Back Points: \n")
f.write(str(ofunc.OrderedScores(ov.ThirteenFourteenGirls_Back_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("13/14 Girls Fly:\n")
f.write("========================\n")
for things in ThirteenFourteenGirls_Fly:
    f.write(things)
f.write("\n")
f.write("13/14 Girls Fly Points: \n")
f.write(str(ofunc.OrderedScores(ov.ThirteenFourteenGirls_Fly_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("13/14 Girls IM:\n")
f.write("========================\n")
for things in ThirteenFourteenGirls_IM:
    f.write(things)
f.write("\n")
f.write("13/14 Girls IM Points: \n")
f.write(str(ofunc.OrderedScores(ov.ThirteenFourteenGirls_IM_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("13/14 Girls Free Relay:\n")
f.write("========================\n")
for things in ThirteenFourteenGirls_FreeRelay:
    f.write(things)
f.write("\n")
f.write("13/14 Girls Free Relay Points: \n")
f.write(str(ofunc.OrderedScores(ov.ThirteenFourteenGirls_FreeRelay_Points))+"\n")
f.write("\n")
################
# thirteenfourteen boys
################
f.write("========================\n")
f.write("13/14 Boys Free:\n")
f.write("========================\n")
for things in ThirteenFourteenBoys_Free:
    f.write(things)
f.write("\n")
f.write("13/14 Boys Free Points: \n")
f.write(str(ofunc.OrderedScores(ov.ThirteenFourteenBoys_Free_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("13/14 Boys Breast:\n")
f.write("========================\n")
for things in ThirteenFourteenBoys_Breast:
    f.write(things)
f.write("\n")
f.write("13/14 Boys Breast Points: \n")
f.write(str(ofunc.OrderedScores(ov.ThirteenFourteenBoys_Breast_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("13/14 Boys Back:\n")
f.write("========================\n")
for things in ThirteenFourteenBoys_Back:
    f.write(things)
f.write("\n")
f.write("13/14 Boys Back Points: \n")
f.write(str(ofunc.OrderedScores(ov.ThirteenFourteenBoys_Back_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("13/14 Boys Fly:\n")
f.write("========================\n")
for things in ThirteenFourteenBoys_Fly:
    f.write(things)
f.write("\n")
f.write("13/14 Boys Fly Points: \n")
f.write(str(ofunc.OrderedScores(ov.ThirteenFourteenBoys_Fly_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("13/14 Boys IM:\n")
f.write("========================\n")
for things in ThirteenFourteenBoys_IM:
    f.write(things)
f.write("\n")
f.write("13/14 Boys IM Points: \n")
f.write(str(ofunc.OrderedScores(ov.ThirteenFourteenBoys_IM_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("13/14 Boys Free Relay:\n")
f.write("========================\n")
for things in ThirteenFourteenBoys_FreeRelay:
    f.write(things)
f.write("\n")
f.write("13/14 Boys Free Relay Points: \n")
f.write(str(ofunc.OrderedScores(ov.ThirteenFourteenBoys_FreeRelay_Points))+"\n")
f.write("\n")
################

################
# fifteeneighteen girls
################
f.write("========================\n")
f.write("15/18 Girls Free:\n")
f.write("========================\n")
for things in FifteenEighteenGirls_Free:
    f.write(things)
f.write("\n")
f.write("15/18 Girls Free Points: \n")
f.write(str(ofunc.OrderedScores(ov.FifteenEighteenGirls_Free_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("15/18 Girls Breast:\n")
f.write("========================\n")
for things in FifteenEighteenGirls_Breast:
    f.write(things)
f.write("\n")
f.write("15/18 Girls Breast Points: \n")
f.write(str(ofunc.OrderedScores(ov.FifteenEighteenGirls_Breast_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("15/18 Girls Back:\n")
f.write("========================\n")
for things in FifteenEighteenGirls_Back:
    f.write(things)
f.write("\n")
f.write("15/18 Girls Back Points: \n")
f.write(str(ofunc.OrderedScores(ov.FifteenEighteenGirls_Back_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("15/18 Girls Fly:\n")
f.write("========================\n")
for things in FifteenEighteenGirls_Fly:
    f.write(things)
f.write("\n")
f.write("15/18 Girls Fly Points: \n")
f.write(str(ofunc.OrderedScores(ov.FifteenEighteenGirls_Fly_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("15/18 Girls IM:\n")
f.write("========================\n")
for things in FifteenEighteenGirls_IM:
    f.write(things)
f.write("\n")
f.write("15/18 Girls IM Points: \n")
f.write(str(ofunc.OrderedScores(ov.FifteenEighteenGirls_IM_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("15/18 Girls Free Relay:\n")
f.write("========================\n")
for things in FifteenEighteenGirls_FreeRelay:
    f.write(things)
f.write("\n")
f.write("15/18 Girls Free Relay Points: \n")
f.write(str(ofunc.OrderedScores(ov.FifteenEighteenGirls_FreeRelay_Points))+"\n")
f.write("\n")
################
# fifteeneighteen boys
################
f.write("========================\n")
f.write("15/18 Boys Free:\n")
f.write("========================\n")
for things in FifteenEighteenBoys_Free:
    f.write(things)
f.write("\n")
f.write("15/18 Boys Free Points: \n")
f.write(str(ofunc.OrderedScores(ov.FifteenEighteenBoys_Free_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("15/18 Boys Breast:\n")
f.write("========================\n")
for things in FifteenEighteenBoys_Breast:
    f.write(things)
f.write("\n")
f.write("15/18 Boys Breast Points: \n")
f.write(str(ofunc.OrderedScores(ov.FifteenEighteenBoys_Breast_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("15/18 Boys Back:\n")
f.write("========================\n")
for things in FifteenEighteenBoys_Back:
    f.write(things)
f.write("\n")
f.write("15/18 Boys Back Points: \n")
f.write(str(ofunc.OrderedScores(ov.FifteenEighteenBoys_Back_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("15/18 Boys Fly:\n")
f.write("========================\n")
for things in FifteenEighteenBoys_Fly:
    f.write(things)
f.write("\n")
f.write("15/18 Boys Fly Points: \n")
f.write(str(ofunc.OrderedScores(ov.FifteenEighteenBoys_Fly_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("15/18 Boys IM:\n")
f.write("========================\n")
for things in FifteenEighteenBoys_IM:
    f.write(things)
f.write("\n")
f.write("15/18 Boys IM Points: \n")
f.write(str(ofunc.OrderedScores(ov.FifteenEighteenBoys_IM_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("15/18 Boys Free Relay:\n")
f.write("========================\n")
for things in FifteenEighteenBoys_FreeRelay:
    f.write(things)
f.write("\n")
f.write("15/18 Boys Free Relay Points: \n")
f.write(str(ofunc.OrderedScores(ov.FifteenEighteenBoys_FreeRelay_Points))+"\n")
f.write("\n")

print "finished"

# create futureompascrapymanager, future functions, and futureMockOMPA

# scoring report
# we can generate total team scores, team stroke scores, age group totals etc, 
# by adding together the various scoring dictionaries with AddTwoDictionaries()
# The OrderedScores() function will order the scoring dictionary from most points
# to fewest, however it will change the data type from a dictionary to a tuple.
# keeping it a tuple is best for correctly adding points throughout the program,
# therefore we only use the OrderedScoring() as display function with print

###############
# scoring summary
###############
f.write("\n")
f.write("\n")
f.write("========================================================================\n")
f.write("========================    SCORING SUMMARY     ========================\n")
f.write("========================================================================\n")
f.write("\n")
f.write("================================================\n")
f.write("================   Six and Unders  =============\n")
f.write("================================================\n")
f.write("\n")
f.write("========================\n")
f.write("6/Under Girls\n")
f.write("========================\n")
f.write("\n")
f.write("6/Under Girls Free\n")
f.write(str(ofunc.OrderedScores(ov.SixUnderGirls_Free_Points))+"\n")
f.write("\n")
f.write("6/Under Girls Breast\n")
f.write(str(ofunc.OrderedScores(ov.SixUnderGirls_Breast_Points))+"\n")
f.write("\n")
f.write("6/Under Girls Back\n")
f.write(str(ofunc.OrderedScores(ov.SixUnderGirls_Back_Points))+"\n")
f.write("\n")
f.write("6/Under Girls Fly\n")
f.write(str(ofunc.OrderedScores(ov.SixUnderGirls_Back_Points))+"\n")
f.write("\n")
f.write("6/Under Girls Medley Relay\n")
#f.write(str(ofunc.OrderedScores(ov.SixUnderGirls_MedRelay_Points))+"\n")
f.write("\n")
f.write("6/Under Girls Free Relay\n")
f.write(str(ofunc.OrderedScores(ov.SixUnderGirls_FreeRelay_Points))+"\n")
f.write("\n")
f.write("6/Under Girls Total Age Group Points\n")
f.write(str(ofunc.OrderedScores(ov.SixUnderGirls_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("6/Under Boys\n")
f.write("========================\n")
f.write("\n")
f.write("6/Under Boys Free\n")
f.write(str(ofunc.OrderedScores(ov.SixUnderBoys_Free_Points))+"\n")
f.write("\n")
f.write("6/Under Boys Breast\n")
f.write(str(ofunc.OrderedScores(ov.SixUnderBoys_Breast_Points))+"\n")
f.write("\n")
f.write("6/Under Boys Back\n")
f.write(str(ofunc.OrderedScores(ov.SixUnderBoys_Back_Points))+"\n")
f.write("\n")
f.write("6/Under Boys Fly\n")
f.write(str(ofunc.OrderedScores(ov.SixUnderBoys_Back_Points))+"\n")
f.write("\n")
f.write("6/Under Boys Medley Relay\n")
#f.write(str(ofunc.OrderedScores(ov.SixUnderBoys_MedRelay_Points))+"\n")
f.write("\n")
f.write("6/Under Boys Free Relay\n")
f.write(str(ofunc.OrderedScores(ov.SixUnderBoys_FreeRelay_Points))+"\n")
f.write("\n")
f.write("6/Under Boys Total Age Group Points\n")
f.write(str(ofunc.OrderedScores(ov.SixUnderBoys_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("6/U Girls and Boys\n")
f.write("========================\n")
f.write("\n")
f.write("6/Under Girls and Boys Free\n")
f.write(str(ofunc.OrderedScores(ofunc.AddTwoDictionaries(ov.SixUnderGirls_Free_Points,ov.SixUnderBoys_Free_Points)))+"\n")
f.write("\n")
f.write("6/Under Girls and Boys Breast\n")
f.write(str(ofunc.OrderedScores(ofunc.AddTwoDictionaries(ov.SixUnderGirls_Breast_Points,ov.SixUnderBoys_Breast_Points)))+"\n")
f.write("\n")
f.write("6/Under Girls and Boys Back\n")
f.write(str(ofunc.OrderedScores(ofunc.AddTwoDictionaries(ov.SixUnderGirls_Back_Points,ov.SixUnderBoys_Back_Points)))+"\n")
f.write("\n")
f.write("6/Under Girls and Boys Fly\n")
f.write(str(ofunc.OrderedScores(ofunc.AddTwoDictionaries(ov.SixUnderGirls_Fly_Points,ov.SixUnderBoys_Fly_Points)))+"\n")
f.write("\n")
f.write("6/Under Girls and Boys Total Age Group Points + Relays\n")
f.write(str(ofunc.OrderedScores(ofunc.AddTwoDictionaries(ov.SixUnderGirls_Points,ov.SixUnderBoys_Points)))+"\n")
f.write("\n")

f.write("================================================\n")
f.write("================  Seven and Eights  ============\n")
f.write("================================================\n")
f.write("\n")
f.write("========================\n")
f.write("7/8 Girls\n")
f.write("========================\n")
f.write("\n")
f.write("7/8 Girls Free\n")
f.write(str(ofunc.OrderedScores(ov.SevenEightGirls_Free_Points))+"\n")
f.write("\n")
f.write("7/8 Girls Breast\n")
f.write(str(ofunc.OrderedScores(ov.SevenEightGirls_Breast_Points))+"\n")
f.write("\n")
f.write("7/8 Girls Back\n")
f.write(str(ofunc.OrderedScores(ov.SevenEightGirls_Back_Points))+"\n")
f.write("\n")
f.write("7/8 Girls Fly\n")
f.write(str(ofunc.OrderedScores(ov.SevenEightGirls_Back_Points))+"\n")
f.write("\n")
f.write("7/8 Girls Medley Relay\n")
#f.write(str(ofunc.OrderedScores(ov.SevenEightGirls_MedRelay_Points))+"\n")
f.write("\n")
f.write("7/8 Girls Free Relay\n")
f.write(str(ofunc.OrderedScores(ov.SevenEightGirls_FreeRelay_Points))+"\n")
f.write("\n")
f.write("7/8 Girls Total Age Group Points\n")
f.write(str(ofunc.OrderedScores(ov.SevenEightGirls_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("7/8 Boys\n")
f.write("========================\n")
f.write("\n")
f.write("7/8 Boys Free\n")
f.write(str(ofunc.OrderedScores(ov.SevenEightBoys_Free_Points))+"\n")
f.write("\n")
f.write("7/8 Boys Breast\n")
f.write(str(ofunc.OrderedScores(ov.SevenEightBoys_Breast_Points))+"\n")
f.write("\n")
f.write("7/8 Boys Back\n")
f.write(str(ofunc.OrderedScores(ov.SevenEightBoys_Back_Points))+"\n")
f.write("\n")
f.write("7/8 Boys Fly\n")
f.write(str(ofunc.OrderedScores(ov.SevenEightBoys_Back_Points))+"\n")
f.write("\n")
f.write("7/8 Boys Medley Relay\n")
#f.write(str(ofunc.OrderedScores(ov.SevenEightBoys_MedRelay_Points))+"\n")
f.write("\n")
f.write("7/8 Boys Free Relay\n")
f.write(str(ofunc.OrderedScores(ov.SevenEightBoys_FreeRelay_Points))+"\n")
f.write("\n")
f.write("7/8 Boys Total Age Group Points\n")
f.write(str(ofunc.OrderedScores(ov.SevenEightBoys_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("7/8 Girls and Boys\n")
f.write("========================\n")
f.write("\n")
f.write("7/8 Girls and Boys Free\n")
f.write(str(ofunc.OrderedScores(ofunc.AddTwoDictionaries(ov.SevenEightGirls_Free_Points,ov.SevenEightBoys_Free_Points)))+"\n")
f.write("\n")
f.write("7/8 Girls and Boys Breast\n")
f.write(str(ofunc.OrderedScores(ofunc.AddTwoDictionaries(ov.SevenEightGirls_Breast_Points,ov.SevenEightBoys_Breast_Points)))+"\n")
f.write("\n")
f.write("7/8 Girls and Boys Back\n")
f.write(str(ofunc.OrderedScores(ofunc.AddTwoDictionaries(ov.SevenEightGirls_Back_Points,ov.SevenEightBoys_Back_Points)))+"\n")
f.write("\n")
f.write("7/8 Girls and Boys Fly\n")
f.write(str(ofunc.OrderedScores(ofunc.AddTwoDictionaries(ov.SevenEightGirls_Fly_Points,ov.SevenEightBoys_Fly_Points)))+"\n")
f.write("\n")
f.write("7/8 Girls and Boys IM\n")
f.write(str(ofunc.OrderedScores(ofunc.AddTwoDictionaries(ov.SevenEightGirls_IM_Points,ov.SevenEightBoys_IM_Points)))+"\n")
f.write("\n")
f.write("7/8 Girls and Boys Total Age Group Points + Relays\n")
f.write(str(ofunc.OrderedScores(ofunc.AddTwoDictionaries(ov.SevenEightGirls_Points,ov.SevenEightBoys_Points)))+"\n")
f.write("\n")

f.write("================================================\n")
f.write("=========  8 and Under Girls and Boys  =========\n")
f.write("================================================\n")
f.write("\n")
f.write("8 and Under Girls and Boys Free\n")
EightUnderTotal_Free_Points = ofunc.AddTwoDictionaries(
ofunc.AddTwoDictionaries(ov.SixUnderGirls_Free_Points,ov.SixUnderBoys_Free_Points),
ofunc.AddTwoDictionaries(ov.SevenEightGirls_Free_Points,ov.SevenEightBoys_Free_Points))
f.write(str(ofunc.OrderedScores(EightUnderTotal_Free_Points))+"\n")
f.write("\n")
f.write("8 and Under Girls and Boys Breast\n")
EightUnderTotal_Breast_Points = ofunc.AddTwoDictionaries(
ofunc.AddTwoDictionaries(ov.SixUnderGirls_Breast_Points,ov.SixUnderBoys_Breast_Points),
ofunc.AddTwoDictionaries(ov.SevenEightGirls_Breast_Points,ov.SevenEightBoys_Breast_Points))
f.write(str(ofunc.OrderedScores(EightUnderTotal_Breast_Points))+"\n")
f.write("\n")
f.write("8 and Under Girls and Boys Back\n")
EightUnderTotal_Back_Points = ofunc.AddTwoDictionaries(
ofunc.AddTwoDictionaries(ov.SixUnderGirls_Back_Points,ov.SixUnderBoys_Back_Points),
ofunc.AddTwoDictionaries(ov.SevenEightGirls_Back_Points,ov.SevenEightBoys_Back_Points))
f.write(str(ofunc.OrderedScores(EightUnderTotal_Back_Points))+"\n")
f.write("\n")
f.write("8 and Under Girls and Boys Fly\n")
EightUnderTotal_Fly_Points = ofunc.AddTwoDictionaries(
ofunc.AddTwoDictionaries(ov.SixUnderGirls_Fly_Points,ov.SixUnderBoys_Fly_Points),
ofunc.AddTwoDictionaries(ov.SevenEightGirls_Fly_Points,ov.SevenEightBoys_Fly_Points))
f.write(str(ofunc.OrderedScores(EightUnderTotal_Fly_Points))+"\n")
f.write("\n")
f.write("8 and Under Girls and Boys IM\n")
EightUnderTotal_IM_Points = ofunc.AddTwoDictionaries(ov.SevenEightGirls_IM_Points,ov.SevenEightBoys_IM_Points)
f.write(str(ofunc.OrderedScores(EightUnderTotal_IM_Points))+"\n")
f.write("\n")
f.write("8 and Under Girls and Boys Total Age Group Points + Relays\n")
EightUnderTotal_Points = ofunc.AddTwoDictionaries(
ofunc.AddTwoDictionaries(ov.SixUnderGirls_Points,ov.SixUnderBoys_Points),
ofunc.AddTwoDictionaries(ov.SevenEightGirls_Points,ov.SevenEightBoys_Points))
f.write(str(ofunc.OrderedScores(EightUnderTotal_Points))+"\n")
f.write("\n")




f.write("================================================\n")
f.write("================   Nine and Tens   =============\n")
f.write("================================================\n")
f.write("\n")
f.write("========================\n")
f.write("9/10 Girls\n")
f.write("========================\n")
f.write("\n")
f.write("9/10 Girls Free\n")
f.write(str(ofunc.OrderedScores(ov.NineTenGirls_Free_Points))+"\n")
f.write("\n")
f.write("9/10 Girls Breast\n")
f.write(str(ofunc.OrderedScores(ov.NineTenGirls_Breast_Points))+"\n")
f.write("\n")
f.write("9/10 Girls Back\n")
f.write(str(ofunc.OrderedScores(ov.NineTenGirls_Back_Points))+"\n")
f.write("\n")
f.write("9/10 Girls Fly\n")
f.write(str(ofunc.OrderedScores(ov.NineTenGirls_Back_Points))+"\n")
f.write("\n")
f.write("9/10 Girls Medley Relay\n")
#f.write(str(ofunc.OrderedScores(ov.NineTenGirls_MedRelay_Points))+"\n")
f.write("\n")
f.write("9/10 Girls Free Relay\n")
f.write(str(ofunc.OrderedScores(ov.NineTenGirls_FreeRelay_Points))+"\n")
f.write("\n")
f.write("9/10 Girls Total Age Group Points\n")
f.write(str(ofunc.OrderedScores(ov.NineTenGirls_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("9/10 Boys\n")
f.write("========================\n")
f.write("\n")
f.write("9/10 Boys Free\n")
f.write(str(ofunc.OrderedScores(ov.NineTenBoys_Free_Points))+"\n")
f.write("\n")
f.write("9/10 Boys Breast\n")
f.write(str(ofunc.OrderedScores(ov.NineTenBoys_Breast_Points))+"\n")
f.write("\n")
f.write("9/10 Boys Back\n")
f.write(str(ofunc.OrderedScores(ov.NineTenBoys_Back_Points))+"\n")
f.write("\n")
f.write("9/10 Boys Fly\n")
f.write(str(ofunc.OrderedScores(ov.NineTenBoys_Back_Points))+"\n")
f.write("\n")
f.write("9/10 Boys Medley Relay\n")
#f.write(str(ofunc.OrderedScores(ov.NineTenBoys_MedRelay_Points))+"\n")
f.write("\n")
f.write("9/10 Boys Free Relay\n")
f.write(str(ofunc.OrderedScores(ov.NineTenBoys_FreeRelay_Points))+"\n")
f.write("\n")
f.write("9/10 Boys Total Age Group Points\n")
f.write(str(ofunc.OrderedScores(ov.NineTenBoys_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("9/10 Girls and Boys\n")
f.write("========================\n")
f.write("\n")
f.write("9/10 Girls and Boys Free\n")
f.write(str(ofunc.OrderedScores(ofunc.AddTwoDictionaries(ov.NineTenGirls_Free_Points,ov.NineTenBoys_Free_Points)))+"\n")
f.write("\n")
f.write("9/10 Girls and Boys Breast\n")
f.write(str(ofunc.OrderedScores(ofunc.AddTwoDictionaries(ov.NineTenGirls_Breast_Points,ov.NineTenBoys_Breast_Points)))+"\n")
f.write("\n")
f.write("9/10 Girls and Boys Back\n")
f.write(str(ofunc.OrderedScores(ofunc.AddTwoDictionaries(ov.NineTenGirls_Back_Points,ov.NineTenBoys_Back_Points)))+"\n")
f.write("\n")
f.write("9/10 Girls and Boys Fly\n")
f.write(str(ofunc.OrderedScores(ofunc.AddTwoDictionaries(ov.NineTenGirls_Fly_Points,ov.NineTenBoys_Fly_Points)))+"\n")
f.write("\n")
f.write("9/10 Girls and Boys IM\n")
f.write(str(ofunc.OrderedScores(ofunc.AddTwoDictionaries(ov.NineTenGirls_IM_Points,ov.NineTenBoys_IM_Points)))+"\n")
f.write("\n")
f.write("9/10 Girls and Boys Total Age Group Points + Relays\n")
f.write(str(ofunc.OrderedScores(ofunc.AddTwoDictionaries(ov.NineTenGirls_Points,ov.NineTenBoys_Points)))+"\n")
f.write("\n")




f.write("================================================\n")
f.write("===============  Eleven and Twelves  ===========\n")
f.write("================================================\n")
f.write("\n")
f.write("========================\n")
f.write("11/12 Girls\n")
f.write("========================\n")
f.write("\n")
f.write("11/12 Girls Free\n")
f.write(str(ofunc.OrderedScores(ov.ElevenTwelveGirls_Free_Points))+"\n")
f.write("\n")
f.write("11/12 Girls Breast\n")
f.write(str(ofunc.OrderedScores(ov.ElevenTwelveGirls_Breast_Points))+"\n")
f.write("\n")
f.write("11/12 Girls Back\n")
f.write(str(ofunc.OrderedScores(ov.ElevenTwelveGirls_Back_Points))+"\n")
f.write("\n")
f.write("11/12 Girls Fly\n")
f.write(str(ofunc.OrderedScores(ov.ElevenTwelveGirls_Back_Points))+"\n")
f.write("\n")
f.write("11/12 Girls Medley Relay\n")
#f.write(str(ofunc.OrderedScores(ov.ElevenTwelveGirls_MedRelay_Points))+"\n")
f.write("\n")
f.write("11/12 Girls Free Relay\n")
f.write(str(ofunc.OrderedScores(ov.ElevenTwelveGirls_FreeRelay_Points))+"\n")
f.write("\n")
f.write("11/12 Girls Total Age Group Points\n")
f.write(str(ofunc.OrderedScores(ov.ElevenTwelveGirls_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("11/12 Boys\n")
f.write("========================\n")
f.write("\n")
f.write("11/12 Boys Free\n")
f.write(str(ofunc.OrderedScores(ov.ElevenTwelveBoys_Free_Points))+"\n")
f.write("\n")
f.write("11/12 Boys Breast\n")
f.write(str(ofunc.OrderedScores(ov.ElevenTwelveBoys_Breast_Points))+"\n")
f.write("\n")
f.write("11/12 Boys Back\n")
f.write(str(ofunc.OrderedScores(ov.ElevenTwelveBoys_Back_Points))+"\n")
f.write("\n")
f.write("11/12 Boys Fly\n")
f.write(str(ofunc.OrderedScores(ov.ElevenTwelveBoys_Back_Points))+"\n")
f.write("\n")
f.write("11/12 Boys Medley Relay\n")
#f.write(str(ofunc.OrderedScores(ov.ElevenTwelveBoys_MedRelay_Points))+"\n")
f.write("\n")
f.write("11/12 Boys Free Relay\n")
f.write(str(ofunc.OrderedScores(ov.ElevenTwelveBoys_FreeRelay_Points))+"\n")
f.write("\n")
f.write("11/12 Boys Total Age Group Points\n")
f.write(str(ofunc.OrderedScores(ov.ElevenTwelveBoys_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("11/12 Girls and Boys\n")
f.write("========================\n")
f.write("\n")
f.write("11/12 Girls and Boys Free\n")
f.write(str(ofunc.OrderedScores(ofunc.AddTwoDictionaries(ov.ElevenTwelveGirls_Free_Points,ov.ElevenTwelveBoys_Free_Points)))+"\n")
f.write("\n")
f.write("11/12 Girls and Boys Breast\n")
f.write(str(ofunc.OrderedScores(ofunc.AddTwoDictionaries(ov.ElevenTwelveGirls_Breast_Points,ov.ElevenTwelveBoys_Breast_Points)))+"\n")
f.write("\n")
f.write("11/12 Girls and Boys Back\n")
f.write(str(ofunc.OrderedScores(ofunc.AddTwoDictionaries(ov.ElevenTwelveGirls_Back_Points,ov.ElevenTwelveBoys_Back_Points)))+"\n")
f.write("\n")
f.write("11/12 Girls and Boys Fly\n")
f.write(str(ofunc.OrderedScores(ofunc.AddTwoDictionaries(ov.ElevenTwelveGirls_Fly_Points,ov.ElevenTwelveBoys_Fly_Points)))+"\n")
f.write("\n")
f.write("11/12 Girls and Boys IM\n")
f.write(str(ofunc.OrderedScores(ofunc.AddTwoDictionaries(ov.ElevenTwelveGirls_IM_Points,ov.ElevenTwelveBoys_IM_Points)))+"\n")
f.write("\n")
f.write("11/12 Girls and Boys Total Age Group Points + Relays\n")
f.write(str(ofunc.OrderedScores(ofunc.AddTwoDictionaries(ov.ElevenTwelveGirls_Points,ov.ElevenTwelveBoys_Points)))+"\n")
f.write("\n")

f.write("================================================\n")
f.write("=========    9 to 12 Girls and Boys    =========\n")
f.write("================================================\n")
f.write("\n")
f.write("9 to 12 Girls and Boys Free\n")
NineTwelveTotal_Free_Points = ofunc.AddTwoDictionaries(
ofunc.AddTwoDictionaries(ov.NineTenGirls_Free_Points,ov.NineTenBoys_Free_Points),
ofunc.AddTwoDictionaries(ov.ElevenTwelveGirls_Free_Points,ov.ElevenTwelveBoys_Free_Points))
f.write(str(ofunc.OrderedScores(NineTwelveTotal_Free_Points))+"\n")
f.write("\n")
f.write("9 to 12 Girls and Boys Breast\n")
NineTwelveTotal_Breast_Points = ofunc.AddTwoDictionaries(
ofunc.AddTwoDictionaries(ov.NineTenGirls_Breast_Points,ov.NineTenBoys_Breast_Points),
ofunc.AddTwoDictionaries(ov.ElevenTwelveGirls_Breast_Points,ov.ElevenTwelveBoys_Breast_Points))
f.write(str(ofunc.OrderedScores(NineTwelveTotal_Breast_Points))+"\n")
f.write("\n")
f.write("9 to 12 Girls and Boys Back\n")
NineTwelveTotal_Back_Points = ofunc.AddTwoDictionaries(
ofunc.AddTwoDictionaries(ov.NineTenGirls_Back_Points,ov.NineTenBoys_Back_Points),
ofunc.AddTwoDictionaries(ov.ElevenTwelveGirls_Back_Points,ov.ElevenTwelveBoys_Back_Points))
f.write(str(ofunc.OrderedScores(NineTwelveTotal_Back_Points))+"\n")
f.write("\n")
f.write("9 to 12 Girls and Boys Fly\n")
NineTwelveTotal_Fly_Points = ofunc.AddTwoDictionaries(
ofunc.AddTwoDictionaries(ov.NineTenGirls_Fly_Points,ov.NineTenBoys_Fly_Points),
ofunc.AddTwoDictionaries(ov.ElevenTwelveGirls_Fly_Points,ov.ElevenTwelveBoys_Fly_Points))
f.write(str(ofunc.OrderedScores(NineTwelveTotal_Fly_Points))+"\n")
f.write("\n")
f.write("9 to 12 Girls and Boys IM\n")
NineTwelveTotal_IM_Points = ofunc.AddTwoDictionaries(
ofunc.AddTwoDictionaries(ov.NineTenGirls_IM_Points,ov.NineTenBoys_IM_Points),
ofunc.AddTwoDictionaries(ov.ElevenTwelveGirls_IM_Points,ov.ElevenTwelveBoys_IM_Points))
f.write(str(ofunc.OrderedScores(NineTwelveTotal_IM_Points))+"\n")
f.write("\n")
f.write("9 to 12 Girls and Boys Total Age Group Points + Relays\n")
NineTwelveTotal_Points = ofunc.AddTwoDictionaries(
ofunc.AddTwoDictionaries(ov.NineTenGirls_Points,ov.NineTenBoys_Points),
ofunc.AddTwoDictionaries(ov.ElevenTwelveGirls_Points,ov.ElevenTwelveBoys_Points))
f.write(str(ofunc.OrderedScores(NineTwelveTotal_Points))+"\n")
f.write("\n")



f.write("================================================\n")
f.write("=============  Thirteen and Fourteens  =========\n")
f.write("================================================\n")
f.write("\n")
f.write("========================\n")
f.write("13/14 Girls\n")
f.write("========================\n")
f.write("\n")
f.write("13/14 Girls Free\n")
f.write(str(ofunc.OrderedScores(ov.ThirteenFourteenGirls_Free_Points))+"\n")
f.write("\n")
f.write("13/14 Girls Breast\n")
f.write(str(ofunc.OrderedScores(ov.ThirteenFourteenGirls_Breast_Points))+"\n")
f.write("\n")
f.write("13/14 Girls Back\n")
f.write(str(ofunc.OrderedScores(ov.ThirteenFourteenGirls_Back_Points))+"\n")
f.write("\n")
f.write("13/14 Girls Fly\n")
f.write(str(ofunc.OrderedScores(ov.ThirteenFourteenGirls_Back_Points))+"\n")
f.write("\n")
f.write("13/14 Girls Medley Relay\n")
#f.write(str(ofunc.OrderedScores(ov.ThirteenFourteenGirls_MedRelay_Points))+"\n")
f.write("\n")
f.write("13/14 Girls Free Relay\n")
f.write(str(ofunc.OrderedScores(ov.ThirteenFourteenGirls_FreeRelay_Points))+"\n")
f.write("\n")
f.write("13/14 Girls Total Age Group Points\n")
f.write(str(ofunc.OrderedScores(ov.ThirteenFourteenGirls_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("13/14 Boys\n")
f.write("========================\n")
f.write("\n")
f.write("13/14 Boys Free\n")
f.write(str(ofunc.OrderedScores(ov.ThirteenFourteenBoys_Free_Points))+"\n")
f.write("\n")
f.write("13/14 Boys Breast\n")
f.write(str(ofunc.OrderedScores(ov.ThirteenFourteenBoys_Breast_Points))+"\n")
f.write("\n")
f.write("13/14 Boys Back\n")
f.write(str(ofunc.OrderedScores(ov.ThirteenFourteenBoys_Back_Points))+"\n")
f.write("\n")
f.write("13/14 Boys Fly\n")
f.write(str(ofunc.OrderedScores(ov.ThirteenFourteenBoys_Back_Points))+"\n")
f.write("\n")
f.write("13/14 Boys Medley Relay\n")
#f.write(str(ofunc.OrderedScores(ov.ThirteenFourteenBoys_MedRelay_Points))+"\n")
f.write("\n")
f.write("13/14 Boys Free Relay\n")
f.write(str(ofunc.OrderedScores(ov.ThirteenFourteenBoys_FreeRelay_Points))+"\n")
f.write("\n")
f.write("13/14 Boys Total Age Group Points\n")
f.write(str(ofunc.OrderedScores(ov.ThirteenFourteenBoys_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("13/14 Girls and Boys\n")
f.write("========================\n")
f.write("\n")
f.write("13/14 Girls and Boys Free\n")
f.write(str(ofunc.OrderedScores(ofunc.AddTwoDictionaries(ov.ThirteenFourteenGirls_Free_Points,ov.ThirteenFourteenBoys_Free_Points)))+"\n")
f.write("\n")
f.write("13/14 Girls and Boys Breast\n")
f.write(str(ofunc.OrderedScores(ofunc.AddTwoDictionaries(ov.ThirteenFourteenGirls_Breast_Points,ov.ThirteenFourteenBoys_Breast_Points)))+"\n")
f.write("\n")
f.write("13/14 Girls and Boys Back\n")
f.write(str(ofunc.OrderedScores(ofunc.AddTwoDictionaries(ov.ThirteenFourteenGirls_Back_Points,ov.ThirteenFourteenBoys_Back_Points)))+"\n")
f.write("\n")
f.write("13/14 Girls and Boys Fly\n")
f.write(str(ofunc.OrderedScores(ofunc.AddTwoDictionaries(ov.ThirteenFourteenGirls_Fly_Points,ov.ThirteenFourteenBoys_Fly_Points)))+"\n")
f.write("\n")
f.write("13/14 Girls and Boys IM\n")
f.write(str(ofunc.OrderedScores(ofunc.AddTwoDictionaries(ov.ThirteenFourteenGirls_IM_Points,ov.ThirteenFourteenBoys_IM_Points)))+"\n")
f.write("\n")
f.write("13/14 Girls and Boys Total Age Group Points + Relays\n")
f.write(str(ofunc.OrderedScores(ofunc.AddTwoDictionaries(ov.ThirteenFourteenGirls_Points,ov.ThirteenFourteenBoys_Points)))+"\n")
f.write("\n")



f.write("================================================\n")
f.write("=============  Fifteen and Eighteens  ==========\n")
f.write("================================================\n")
f.write("\n")
f.write("========================\n")
f.write("15/18 Girls\n")
f.write("========================\n")
f.write("\n")
f.write("15/18 Girls Free\n")
f.write(str(ofunc.OrderedScores(ov.FifteenEighteenGirls_Free_Points))+"\n")
f.write("\n")
f.write("15/18 Girls Breast\n")
f.write(str(ofunc.OrderedScores(ov.FifteenEighteenGirls_Breast_Points))+"\n")
f.write("\n")
f.write("15/18 Girls Back\n")
f.write(str(ofunc.OrderedScores(ov.FifteenEighteenGirls_Back_Points))+"\n")
f.write("\n")
f.write("15/18 Girls Fly\n")
f.write(str(ofunc.OrderedScores(ov.FifteenEighteenGirls_Back_Points))+"\n")
f.write("\n")
f.write("15/18 Girls Medley Relay\n")
#f.write(str(ofunc.OrderedScores(ov.FifteenEighteenGirls_MedRelay_Points))+"\n")
f.write("\n")
f.write("15/18 Girls Free Relay\n")
f.write(str(ofunc.OrderedScores(ov.FifteenEighteenGirls_FreeRelay_Points))+"\n")
f.write("\n")
f.write("15/18 Girls Total Age Group Points\n")
f.write(str(ofunc.OrderedScores(ov.FifteenEighteenGirls_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("15/18 Boys\n")
f.write("========================\n")
f.write("\n")
f.write("15/18 Boys Free\n")
f.write(str(ofunc.OrderedScores(ov.FifteenEighteenBoys_Free_Points))+"\n")
f.write("\n")
f.write("15/18 Boys Breast\n")
f.write(str(ofunc.OrderedScores(ov.FifteenEighteenBoys_Breast_Points))+"\n")
f.write("\n")
f.write("15/18 Boys Back\n")
f.write(str(ofunc.OrderedScores(ov.FifteenEighteenBoys_Back_Points))+"\n")
f.write("\n")
f.write("15/18 Boys Fly\n")
f.write(str(ofunc.OrderedScores(ov.FifteenEighteenBoys_Back_Points))+"\n")
f.write("\n")
f.write("15/18 Boys Medley Relay\n")
#f.write(str(ofunc.OrderedScores(ov.FifteenEighteenBoys_MedRelay_Points))+"\n")
f.write("\n")
f.write("15/18 Boys Free Relay\n")
f.write(str(ofunc.OrderedScores(ov.FifteenEighteenBoys_FreeRelay_Points))+"\n")
f.write("\n")
f.write("15/18 Boys Total Age Group Points + Relays\n")
f.write(str(ofunc.OrderedScores(ov.FifteenEighteenBoys_Points))+"\n")
f.write("\n")
f.write("========================\n")
f.write("15/18 Girls and Boys\n")
f.write("========================\n")
f.write("\n")
f.write("15/18 Girls and Boys Free\n")
f.write(str(ofunc.OrderedScores(ofunc.AddTwoDictionaries(ov.FifteenEighteenGirls_Free_Points,ov.FifteenEighteenBoys_Free_Points)))+"\n")
f.write("\n")
f.write("15/18 Girls and Boys Breast\n")
f.write(str(ofunc.OrderedScores(ofunc.AddTwoDictionaries(ov.FifteenEighteenGirls_Breast_Points,ov.FifteenEighteenBoys_Breast_Points)))+"\n")
f.write("\n")
f.write("15/18 Girls and Boys Back\n")
f.write(str(ofunc.OrderedScores(ofunc.AddTwoDictionaries(ov.FifteenEighteenGirls_Back_Points,ov.FifteenEighteenBoys_Back_Points)))+"\n")
f.write("\n")
f.write("15/18 Girls and Boys Fly\n")
f.write(str(ofunc.OrderedScores(ofunc.AddTwoDictionaries(ov.FifteenEighteenGirls_Fly_Points,ov.FifteenEighteenBoys_Fly_Points)))+"\n")
f.write("\n")
f.write("15/18 Girls and Boys IM\n")
f.write(str(ofunc.OrderedScores(ofunc.AddTwoDictionaries(ov.FifteenEighteenGirls_IM_Points,ov.FifteenEighteenBoys_IM_Points)))+"\n")
f.write("\n")
f.write("15/18 Girls and Boys Total Age Group Points + Relays\n")
f.write(str(ofunc.OrderedScores(ofunc.AddTwoDictionaries(ov.FifteenEighteenGirls_Points,ov.FifteenEighteenBoys_Points)))+"\n")
f.write("\n")


f.write("================================================\n")
f.write("=========    13 and Up Girls and Boys    =======\n")
f.write("================================================\n")
f.write("\n")
f.write("13 and Up Girls and Boys Free\n")
ThirteenUpTotal_Free_Points = ofunc.AddTwoDictionaries(
ofunc.AddTwoDictionaries(ov.ThirteenFourteenGirls_Free_Points,ov.ThirteenFourteenBoys_Free_Points),
ofunc.AddTwoDictionaries(ov.FifteenEighteenGirls_Free_Points,ov.FifteenEighteenBoys_Free_Points))
f.write(str(ofunc.OrderedScores(ThirteenUpTotal_Free_Points))+"\n")
f.write("\n")
f.write("13 and Up Girls and Boys Breast\n")
ThirteenUpTotal_Breast_Points = ofunc.AddTwoDictionaries(
ofunc.AddTwoDictionaries(ov.ThirteenFourteenGirls_Breast_Points,ov.ThirteenFourteenBoys_Breast_Points),
ofunc.AddTwoDictionaries(ov.FifteenEighteenGirls_Breast_Points,ov.FifteenEighteenBoys_Breast_Points))
f.write(str(ofunc.OrderedScores(ThirteenUpTotal_Breast_Points))+"\n")
f.write("\n")
f.write("13 and Up Girls and Boys Back\n")
ThirteenUpTotal_Back_Points = ofunc.AddTwoDictionaries(
ofunc.AddTwoDictionaries(ov.ThirteenFourteenGirls_Back_Points,ov.ThirteenFourteenBoys_Back_Points),
ofunc.AddTwoDictionaries(ov.FifteenEighteenGirls_Back_Points,ov.FifteenEighteenBoys_Back_Points))
f.write(str(ofunc.OrderedScores(ThirteenUpTotal_Back_Points))+"\n")
f.write("\n")
f.write("13 and Up Girls and Boys Fly\n")
ThirteenUpTotal_Fly_Points = ofunc.AddTwoDictionaries(
ofunc.AddTwoDictionaries(ov.ThirteenFourteenGirls_Fly_Points,ov.ThirteenFourteenBoys_Fly_Points),
ofunc.AddTwoDictionaries(ov.FifteenEighteenGirls_Fly_Points,ov.FifteenEighteenBoys_Fly_Points))
f.write(str(ofunc.OrderedScores(ThirteenUpTotal_Fly_Points))+"\n")
f.write("\n")
f.write("13 and Up Girls and Boys IM\n")
ThirteenUpTotal_IM_Points = ofunc.AddTwoDictionaries(
ofunc.AddTwoDictionaries(ov.ThirteenFourteenGirls_IM_Points,ov.ThirteenFourteenBoys_IM_Points),
ofunc.AddTwoDictionaries(ov.FifteenEighteenGirls_IM_Points,ov.FifteenEighteenBoys_IM_Points))
f.write(str(ofunc.OrderedScores(ThirteenUpTotal_IM_Points))+"\n")
f.write("\n")
f.write("13 and Up Girls and Boys Total Age Group Points + Relays\n")
ThirteenUpTotal_Points = ofunc.AddTwoDictionaries(
ofunc.AddTwoDictionaries(ov.ThirteenFourteenGirls_Points,ov.ThirteenFourteenBoys_Points),
ofunc.AddTwoDictionaries(ov.FifteenEighteenGirls_Points,ov.FifteenEighteenBoys_Points))
f.write(str(ofunc.OrderedScores(ThirteenUpTotal_Points))+"\n")
f.write("\n")
f.write("\n")
f.write("\n")
f.write("================================================\n")
f.write("============    Team Stroke Scores    ==========\n")
f.write("================================================\n")
f.write("\n")
f.write("Team Freestyle\n")
f.write(str(ofunc.OrderedScores(ofunc.AddTwoDictionaries(EightUnderTotal_Free_Points,
ofunc.AddTwoDictionaries(NineTwelveTotal_Free_Points,ThirteenUpTotal_Free_Points)
)))+"\n")
f.write("\n")
f.write("Team Breastroke\n")
f.write(str(ofunc.OrderedScores(ofunc.AddTwoDictionaries(EightUnderTotal_Breast_Points,
ofunc.AddTwoDictionaries(NineTwelveTotal_Breast_Points,ThirteenUpTotal_Breast_Points)
)))+"\n")
f.write("\n")
f.write("Team Backstroke\n")
f.write(str(ofunc.OrderedScores(ofunc.AddTwoDictionaries(EightUnderTotal_Back_Points,
ofunc.AddTwoDictionaries(NineTwelveTotal_Back_Points,ThirteenUpTotal_Back_Points)
)))+"\n")
f.write("\n")
f.write("Team Butterfly\n")
f.write(str(ofunc.OrderedScores(ofunc.AddTwoDictionaries(EightUnderTotal_Fly_Points,
ofunc.AddTwoDictionaries(NineTwelveTotal_Fly_Points,ThirteenUpTotal_Fly_Points)
)))+"\n")
f.write("\n")
f.write("Team IM\n")
f.write(str(ofunc.OrderedScores(ofunc.AddTwoDictionaries(EightUnderTotal_IM_Points,
ofunc.AddTwoDictionaries(NineTwelveTotal_IM_Points,ThirteenUpTotal_IM_Points)
)))+"\n")
f.write("\n")
f.write("Team Medley Relays\n")
f.write("\n")
f.write("Team Free Relays\n")
f.write("\n")
TotalFreeRelay_Points = ofunc.TotalPoints(ov.SixUnderGirls_FreeRelay_Points,ov.SixUnderBoys_FreeRelay_Points,ov.SevenEightGirls_FreeRelay_Points,ov.SevenEightBoys_FreeRelay_Points,
    ov.NineTenGirls_FreeRelay_Points,ov.NineTenBoys_FreeRelay_Points,ov.ElevenTwelveGirls_FreeRelay_Points,ov.ElevenTwelveBoys_FreeRelay_Points,
    ov.ThirteenFourteenGirls_FreeRelay_Points,ov.ThirteenFourteenBoys_FreeRelay_Points,ov.FifteenEighteenGirls_FreeRelay_Points,ov.FifteenEighteenBoys_FreeRelay_Points)
f.write(str(ofunc.OrderedScores(TotalFreeRelay_Points))+"\n")
f.write("\n")
f.write("================================================\n")
f.write("============    Total Team Scores     ==========\n")
f.write("================================================\n")
f.write("\n")
f.write(str(ofunc.OrderedScores(ofunc.AddTwoDictionaries(EightUnderTotal_Points,
ofunc.AddTwoDictionaries(NineTwelveTotal_Points,ThirteenUpTotal_Points)
)))+"\n")



#Relay events
#         Medley relay 12 age group genders
#                  Find lowest free, brst, back, fly total using 4 different swimmers
#                             Rank by team within each of the 12 age group genders
#                                    Convert each rank into a point total and add to team point categories







