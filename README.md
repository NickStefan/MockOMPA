# MockOMPA

#### Dependencies:
* Scrapy python webscraping library release 0.20.2
* python 2.7

#### Needs Further Refactoring
* When I made this in Jan 2014, it was the first programming I had done since a trading algorithm in VB in 2009
* Too many explicit statements of using the same function called again and again for each age group
* Could be made much more DRY by using wrapper functions that take a list of the age group variables, and a callback
* I've been busy with swimsolo.com (swimsetswebsite repo), and preparing for Hack Reactor; the only reason I updated this repo at all was because the OMPA completely changed their site, and I needed to update the spider to still crawl for the 2014 swim season.

#### Uses: 
* fully quantified knowlegde of team strengths and weaknesses
* program runnable at any time of the season, creates a "mock OMPA" as if the OMPA were swam "today"
* good for tracking team improvements
* just for fun, the total scores can be like the BCS of OMPA swimming
* can run the meet with certain teams removed
* can remove all but two teams to simulate a dualmeet
* can toggle dual meet scoring or ompa scoring


#### Flow of Data:
* ompascrapymanager.py manages the spiders that crawl the ompa database website, and creates the json files

* mockOMPA.py:
  * the .json files from ompascrapymanager.py are fed into LoadScrapyData()
  * LoadScrappyData() -> ReOrderStrokes() -> SortTeamSwimmers() -> PickEvents() -> FillEvents()
  * variables loaded from FillEvents() are then evaluated with ScoreEvent()
  * ScoreEvent() also prints out event results (ie 1st place swimmer, 2nd place swimmer etc)
  * various points dictionaries stated in ompapresetvariables module are then added and totaled in various ways to give information such as total team points, team fly points, team 6/u girls points etc
  * AddTwoDictionaries() helps with the totaling of these different dictionaries
  * OrderedScores() is a formating tool for printing, but really isnt used to affect program variables