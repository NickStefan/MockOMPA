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
call(["scrapy crawl ompaspider -a lowage='0' -a highage='6' -a sex='W' -a StrkDist='10025' -o SB2013sixundergirlsfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='0' -a highage='6' -a sex='W' -a StrkDist='30025' -o SB2013sixundergirlsbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='0' -a highage='6' -a sex='W' -a StrkDist='20025' -o SB2013sixundergirlsback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='0' -a highage='6' -a sex='W' -a StrkDist='40025' -o SB2013sixundergirlsfly.json -t json"], shell=True)
sleep(randint(15,45))

#6under boys free,breast,back,fly
call(["scrapy crawl ompaspider -a lowage='0' -a highage='6' -a sex='M' -a StrkDist='10025' -o SB2013sixunderboysfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='0' -a highage='6' -a sex='M' -a StrkDist='30025' -o SB2013sixunderboysbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='0' -a highage='6' -a sex='M' -a StrkDist='20025' -o SB2013sixunderboysback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='0' -a highage='6' -a sex='M' -a StrkDist='40025' -o SB2013sixunderboysfly.json -t json"], shell=True)
sleep(randint(15,45))

#78 girls free,breast,back,fly,im
call(["scrapy crawl ompaspider -a lowage='7' -a highage='8' -a sex='W' -a StrkDist='10025' -o SB2013seveneightgirlsfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='7' -a highage='8' -a sex='W' -a StrkDist='30025' -o SB2013seveneightgirlsbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='7' -a highage='8' -a sex='W' -a StrkDist='20025' -o SB2013seveneightgirlsback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='7' -a highage='8' -a sex='W' -a StrkDist='40025' -o SB2013seveneightgirlsfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='7' -a highage='8' -a sex='W' -a StrkDist='50100' -o SB2013seveneightgirlsim.json -t json"], shell=True)
sleep(randint(15,45))

#78 boys free,breast,back,fly,im
call(["scrapy crawl ompaspider -a lowage='7' -a highage='8' -a sex='M' -a StrkDist='10025' -o SB2013seveneightboysfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='7' -a highage='8' -a sex='M' -a StrkDist='30025' -o SB2013seveneightboysbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='7' -a highage='8' -a sex='M' -a StrkDist='20025' -o SB2013seveneightboysback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='7' -a highage='8' -a sex='M' -a StrkDist='40025' -o SB2013seveneightboysfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='7' -a highage='8' -a sex='M' -a StrkDist='50100' -o SB2013seveneightboysim.json -t json"], shell=True)
sleep(randint(15,45))

#910 girls free,breast,back,fly,im
call(["scrapy crawl ompaspider -a lowage='9' -a highage='10' -a sex='W' -a StrkDist='10050' -o SB2013ninetengirlsfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='9' -a highage='10' -a sex='W' -a StrkDist='30050' -o SB2013ninetengirlsbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='9' -a highage='10' -a sex='W' -a StrkDist='20050' -o SB2013ninetengirlsback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='9' -a highage='10' -a sex='W' -a StrkDist='40050' -o SB2013ninetengirlsfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='9' -a highage='10' -a sex='W' -a StrkDist='50100' -o SB2013ninetengirlsim.json -t json"], shell=True)
sleep(randint(15,45))

#910 boys
call(["scrapy crawl ompaspider -a lowage='9' -a highage='10' -a sex='M' -a StrkDist='10050' -o SB2013ninetenboysfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='9' -a highage='10' -a sex='M' -a StrkDist='30050' -o SB2013ninetenboysbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='9' -a highage='10' -a sex='M' -a StrkDist='20050' -o SB2013ninetenboysback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='9' -a highage='10' -a sex='M' -a StrkDist='40050' -o SB2013ninetenboysfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='9' -a highage='10' -a sex='M' -a StrkDist='50100' -o SB2013ninetenboysim.json -t json"], shell=True)
sleep(randint(15,45))

#1112 girls
call(["scrapy crawl ompaspider -a lowage='11' -a highage='12' -a sex='W' -a StrkDist='10050' -o SB2013eleventwelvegirlsfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='11' -a highage='12' -a sex='W' -a StrkDist='30050' -o SB2013eleventwelvegirlsbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='11' -a highage='12' -a sex='W' -a StrkDist='20050' -o SB2013eleventwelvegirlsback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='11' -a highage='12' -a sex='W' -a StrkDist='40050' -o SB2013eleventwelvegirlsfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='11' -a highage='12' -a sex='W' -a StrkDist='50100' -o SB2013eleventwelvegirlsim.json -t json"], shell=True)
sleep(randint(15,45))

#1112 boys
call(["scrapy crawl ompaspider -a lowage='11' -a highage='12' -a sex='M' -a StrkDist='10050' -o SB2013eleventwelveboysfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='11' -a highage='12' -a sex='M' -a StrkDist='30050' -o SB2013eleventwelveboysbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='11' -a highage='12' -a sex='M' -a StrkDist='20050' -o SB2013eleventwelveboysback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='11' -a highage='12' -a sex='M' -a StrkDist='40050' -o SB2013eleventwelveboysfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='11' -a highage='12' -a sex='M' -a StrkDist='50100' -o SB2013eleventwelveboysim.json -t json"], shell=True)
sleep(randint(15,45))

#1314 girls
call(["scrapy crawl ompaspider -a lowage='13' -a highage='14' -a sex='W' -a StrkDist='10050' -o SB2013thirteenfourteengirlsfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='13' -a highage='14' -a sex='W' -a StrkDist='30050' -o SB2013thirteenfourteengirlsbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='13' -a highage='14' -a sex='W' -a StrkDist='20050' -o SB2013thirteenfourteengirlsback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='13' -a highage='14' -a sex='W' -a StrkDist='40050' -o SB2013thirteenfourteengirlsfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='13' -a highage='14' -a sex='W' -a StrkDist='50100' -o SB2013thirteenfourteengirlsim.json -t json"], shell=True)
sleep(randint(15,45))

#1314 boys
call(["scrapy crawl ompaspider -a lowage='13' -a highage='14' -a sex='M' -a StrkDist='10050' -o SB2013thirteenfourteenboysfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='13' -a highage='14' -a sex='M' -a StrkDist='30050' -o SB2013thirteenfourteenboysbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='13' -a highage='14' -a sex='M' -a StrkDist='20050' -o SB2013thirteenfourteenboysback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='13' -a highage='14' -a sex='M' -a StrkDist='40050' -o SB2013thirteenfourteenboysfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='13' -a highage='14' -a sex='M' -a StrkDist='50100' -o SB2013thirteenfourteenboysim.json -t json"], shell=True)
sleep(randint(15,45))

#1518 girls
call(["scrapy crawl ompaspider -a lowage='15' -a highage='18' -a sex='W' -a StrkDist='10050' -o SB2013fifteeneighteengirlsfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='15' -a highage='18' -a sex='W' -a StrkDist='30050' -o SB2013fifteeneighteengirlsbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='15' -a highage='18' -a sex='W' -a StrkDist='20050' -o SB2013fifteeneighteengirlsback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='15' -a highage='18' -a sex='W' -a StrkDist='40050' -o SB2013fifteeneighteengirlsfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='15' -a highage='18' -a sex='W' -a StrkDist='50100' -o SB2013fifteeneighteengirlsim.json -t json"], shell=True)
sleep(randint(15,45))

#1518 boys
call(["scrapy crawl ompaspider -a lowage='15' -a highage='18' -a sex='M' -a StrkDist='10050' -o SB2013fifteeneighteenboysfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='15' -a highage='18' -a sex='M' -a StrkDist='30050' -o SB2013fifteeneighteenboysbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='15' -a highage='18' -a sex='M' -a StrkDist='20050' -o SB2013fifteeneighteenboysback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='15' -a highage='18' -a sex='M' -a StrkDist='40050' -o SB2013fifteeneighteenboysfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='15' -a highage='18' -a sex='M' -a StrkDist='50100' -o SB2013fifteeneighteenboysim.json -t json"], shell=True)
sleep(randint(15,45))