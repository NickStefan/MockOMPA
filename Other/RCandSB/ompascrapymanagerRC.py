#!/usr/bin/python

# MockOMPA
# Uses: 
# <> fully quantified knowlegde of team strengths and weaknesses
# <> program runnable at any time of the season, good for tracking team improvemts
# <> just for fun, the total scores can be like the BCS of OMPA swimming
# code written and designed by Nick Stefan copyright 2014

#scrapymanager

from random import randint
from time import sleep
from subprocess import call

#deletes json file
#call(["rm items.json"], shell=True)

#6under girls free,breast,back,fly
call(["scrapy crawl ompaspider -a lowage='0' -a highage='6' -a sex='W' -a StrkDist='10025' -o RCsixundergirlsfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='0' -a highage='6' -a sex='W' -a StrkDist='30025' -o RCsixundergirlsbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='0' -a highage='6' -a sex='W' -a StrkDist='20025' -o RCsixundergirlsback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='0' -a highage='6' -a sex='W' -a StrkDist='40025' -o RCsixundergirlsfly.json -t json"], shell=True)
sleep(randint(15,45))

#6under boys free,breast,back,fly
call(["scrapy crawl ompaspider -a lowage='0' -a highage='6' -a sex='M' -a StrkDist='10025' -o RCsixunderboysfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='0' -a highage='6' -a sex='M' -a StrkDist='30025' -o RCsixunderboysbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='0' -a highage='6' -a sex='M' -a StrkDist='20025' -o RCsixunderboysback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='0' -a highage='6' -a sex='M' -a StrkDist='40025' -o RCsixunderboysfly.json -t json"], shell=True)
sleep(randint(15,45))

#78 girls free,breast,back,fly,im
call(["scrapy crawl ompaspider -a lowage='7' -a highage='8' -a sex='W' -a StrkDist='10025' -o RCseveneightgirlsfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='7' -a highage='8' -a sex='W' -a StrkDist='30025' -o RCseveneightgirlsbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='7' -a highage='8' -a sex='W' -a StrkDist='20025' -o RCseveneightgirlsback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='7' -a highage='8' -a sex='W' -a StrkDist='40025' -o RCseveneightgirlsfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='7' -a highage='8' -a sex='W' -a StrkDist='50100' -o RCseveneightgirlsim.json -t json"], shell=True)
sleep(randint(15,45))

#78 boys free,breast,back,fly,im
call(["scrapy crawl ompaspider -a lowage='7' -a highage='8' -a sex='M' -a StrkDist='10025' -o RCseveneightboysfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='7' -a highage='8' -a sex='M' -a StrkDist='30025' -o RCseveneightboysbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='7' -a highage='8' -a sex='M' -a StrkDist='20025' -o RCseveneightboysback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='7' -a highage='8' -a sex='M' -a StrkDist='40025' -o RCseveneightboysfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='7' -a highage='8' -a sex='M' -a StrkDist='50100' -o RCseveneightboysim.json -t json"], shell=True)
sleep(randint(15,45))

#910 girls free,breast,back,fly,im
call(["scrapy crawl ompaspider -a lowage='9' -a highage='10' -a sex='W' -a StrkDist='10050' -o RCninetengirlsfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='9' -a highage='10' -a sex='W' -a StrkDist='30050' -o RCninetengirlsbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='9' -a highage='10' -a sex='W' -a StrkDist='20050' -o RCninetengirlsback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='9' -a highage='10' -a sex='W' -a StrkDist='40050' -o RCninetengirlsfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='9' -a highage='10' -a sex='W' -a StrkDist='50100' -o RCninetengirlsim.json -t json"], shell=True)
sleep(randint(15,45))

#910 boys
call(["scrapy crawl ompaspider -a lowage='9' -a highage='10' -a sex='M' -a StrkDist='10050' -o RCninetenboysfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='9' -a highage='10' -a sex='M' -a StrkDist='30050' -o RCninetenboysbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='9' -a highage='10' -a sex='M' -a StrkDist='20050' -o RCninetenboysback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='9' -a highage='10' -a sex='M' -a StrkDist='40050' -o RCninetenboysfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='9' -a highage='10' -a sex='M' -a StrkDist='50100' -o RCninetenboysim.json -t json"], shell=True)
sleep(randint(15,45))

#1112 girls
call(["scrapy crawl ompaspider -a lowage='11' -a highage='12' -a sex='W' -a StrkDist='10050' -o RCeleventwelvegirlsfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='11' -a highage='12' -a sex='W' -a StrkDist='30050' -o RCeleventwelvegirlsbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='11' -a highage='12' -a sex='W' -a StrkDist='20050' -o RCeleventwelvegirlsback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='11' -a highage='12' -a sex='W' -a StrkDist='40050' -o RCeleventwelvegirlsfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='11' -a highage='12' -a sex='W' -a StrkDist='50100' -o RCeleventwelvegirlsim.json -t json"], shell=True)
sleep(randint(15,45))

#1112 boys
call(["scrapy crawl ompaspider -a lowage='11' -a highage='12' -a sex='M' -a StrkDist='10050' -o RCeleventwelveboysfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='11' -a highage='12' -a sex='M' -a StrkDist='30050' -o RCeleventwelveboysbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='11' -a highage='12' -a sex='M' -a StrkDist='20050' -o RCeleventwelveboysback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='11' -a highage='12' -a sex='M' -a StrkDist='40050' -o RCeleventwelveboysfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='11' -a highage='12' -a sex='M' -a StrkDist='50100' -o RCeleventwelveboysim.json -t json"], shell=True)
sleep(randint(15,45))

#1314 girls
call(["scrapy crawl ompaspider -a lowage='13' -a highage='14' -a sex='W' -a StrkDist='10050' -o RCthirteenfourteengirlsfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='13' -a highage='14' -a sex='W' -a StrkDist='30050' -o RCthirteenfourteengirlsbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='13' -a highage='14' -a sex='W' -a StrkDist='20050' -o RCthirteenfourteengirlsback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='13' -a highage='14' -a sex='W' -a StrkDist='40050' -o RCthirteenfourteengirlsfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='13' -a highage='14' -a sex='W' -a StrkDist='50100' -o RCthirteenfourteengirlsim.json -t json"], shell=True)
sleep(randint(15,45))

#1314 boys
call(["scrapy crawl ompaspider -a lowage='13' -a highage='14' -a sex='M' -a StrkDist='10050' -o RCthirteenfourteenboysfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='13' -a highage='14' -a sex='M' -a StrkDist='30050' -o RCthirteenfourteenboysbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='13' -a highage='14' -a sex='M' -a StrkDist='20050' -o RCthirteenfourteenboysback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='13' -a highage='14' -a sex='M' -a StrkDist='40050' -o RCthirteenfourteenboysfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='13' -a highage='14' -a sex='M' -a StrkDist='50100' -o RCthirteenfourteenboysim.json -t json"], shell=True)
sleep(randint(15,45))

#1518 girls
call(["scrapy crawl ompaspider -a lowage='15' -a highage='18' -a sex='W' -a StrkDist='10050' -o RCfifteeneighteengirlsfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='15' -a highage='18' -a sex='W' -a StrkDist='30050' -o RCfifteeneighteengirlsbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='15' -a highage='18' -a sex='W' -a StrkDist='20050' -o RCfifteeneighteengirlsback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='15' -a highage='18' -a sex='W' -a StrkDist='40050' -o RCfifteeneighteengirlsfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='15' -a highage='18' -a sex='W' -a StrkDist='50100' -o RCfifteeneighteengirlsim.json -t json"], shell=True)
sleep(randint(15,45))

#1518 boys
call(["scrapy crawl ompaspider -a lowage='15' -a highage='18' -a sex='M' -a StrkDist='10050' -o RCfifteeneighteenboysfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='15' -a highage='18' -a sex='M' -a StrkDist='30050' -o RCfifteeneighteenboysbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='15' -a highage='18' -a sex='M' -a StrkDist='20050' -o RCfifteeneighteenboysback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='15' -a highage='18' -a sex='M' -a StrkDist='40050' -o RCfifteeneighteenboysfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='15' -a highage='18' -a sex='M' -a StrkDist='50100' -o RCfifteeneighteenboysim.json -t json"], shell=True)
sleep(randint(15,45))