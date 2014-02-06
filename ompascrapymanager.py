#!/usr/bin/python

# MockOMPA
# Uses: 
# <> fully quantified knowlegde of team strengths and weaknesses
# <> program runnable at any time of the season, good for tracking team improvemts
# <> just for fun, the total scores can be like the BCS of OMPA swimming
# code written and designed by Nick Stefan

#scrapymanager

from random import randint
from time import sleep
from subprocess import call

#deletes json file
#call(["rm items.json"], shell=True)

#6under girls free,breast,back,fly
call(["scrapy crawl ompaspider -a lowage='0' -a highage='6' -a sex='W' -a StrkDist='10025' -o sixundergirlsfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='0' -a highage='6' -a sex='W' -a StrkDist='30025' -o sixundergirlsbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='0' -a highage='6' -a sex='W' -a StrkDist='20025' -o sixundergirlsback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='0' -a highage='6' -a sex='W' -a StrkDist='40025' -o sixundergirlsfly.json -t json"], shell=True)
sleep(randint(15,45))

#6under boys free,breast,back,fly
call(["scrapy crawl ompaspider -a lowage='0' -a highage='6' -a sex='M' -a StrkDist='10025' -o sixunderboysfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='0' -a highage='6' -a sex='M' -a StrkDist='30025' -o sixunderboysbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='0' -a highage='6' -a sex='M' -a StrkDist='20025' -o sixunderboysback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='0' -a highage='6' -a sex='M' -a StrkDist='40025' -o sixunderboysfly.json -t json"], shell=True)
sleep(randint(15,45))

#78 girls free,breast,back,fly,im
call(["scrapy crawl ompaspider -a lowage='7' -a highage='8' -a sex='W' -a StrkDist='10025' -o seveneightgirlsfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='7' -a highage='8' -a sex='W' -a StrkDist='30025' -o seveneightgirlsbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='7' -a highage='8' -a sex='W' -a StrkDist='20025' -o seveneightgirlsback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='7' -a highage='8' -a sex='W' -a StrkDist='40025' -o seveneightgirlsfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='7' -a highage='8' -a sex='W' -a StrkDist='50100' -o seveneightgirlsim.json -t json"], shell=True)
sleep(randint(15,45))

#78 boys free,breast,back,fly,im
call(["scrapy crawl ompaspider -a lowage='7' -a highage='8' -a sex='M' -a StrkDist='10025' -o seveneightboysfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='7' -a highage='8' -a sex='M' -a StrkDist='30025' -o seveneightboysbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='7' -a highage='8' -a sex='M' -a StrkDist='20025' -o seveneightboysback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='7' -a highage='8' -a sex='M' -a StrkDist='40025' -o seveneightboysfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='7' -a highage='8' -a sex='M' -a StrkDist='50100' -o seveneightboysim.json -t json"], shell=True)
sleep(randint(15,45))

#910 girls free,breast,back,fly,im
call(["scrapy crawl ompaspider -a lowage='9' -a highage='10' -a sex='W' -a StrkDist='10050' -o ninetengirlsfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='9' -a highage='10' -a sex='W' -a StrkDist='30050' -o ninetengirlsbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='9' -a highage='10' -a sex='W' -a StrkDist='20050' -o ninetengirlsback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='9' -a highage='10' -a sex='W' -a StrkDist='40050' -o ninetengirlsfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='9' -a highage='10' -a sex='W' -a StrkDist='50100' -o ninetengirlsim.json -t json"], shell=True)
sleep(randint(15,45))

#910 boys
call(["scrapy crawl ompaspider -a lowage='9' -a highage='10' -a sex='M' -a StrkDist='10050' -o ninetenboysfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='9' -a highage='10' -a sex='M' -a StrkDist='30050' -o ninetenboysbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='9' -a highage='10' -a sex='M' -a StrkDist='20050' -o ninetenboysback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='9' -a highage='10' -a sex='M' -a StrkDist='40050' -o ninetenboysfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='9' -a highage='10' -a sex='M' -a StrkDist='50100' -o ninetenboysim.json -t json"], shell=True)
sleep(randint(15,45))

#1112 girls
call(["scrapy crawl ompaspider -a lowage='11' -a highage='12' -a sex='W' -a StrkDist='10050' -o eleventwelvegirlsfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='11' -a highage='12' -a sex='W' -a StrkDist='30050' -o eleventwelvegirlsbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='11' -a highage='12' -a sex='W' -a StrkDist='20050' -o eleventwelvegirlsback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='11' -a highage='12' -a sex='W' -a StrkDist='40050' -o eleventwelvegirlsfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='11' -a highage='12' -a sex='W' -a StrkDist='50100' -o eleventwelvegirlsim.json -t json"], shell=True)
sleep(randint(15,45))

#1112 boys
call(["scrapy crawl ompaspider -a lowage='11' -a highage='12' -a sex='M' -a StrkDist='10050' -o eleventwelveboysfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='11' -a highage='12' -a sex='M' -a StrkDist='30050' -o eleventwelveboysbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='11' -a highage='12' -a sex='M' -a StrkDist='20050' -o eleventwelveboysback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='11' -a highage='12' -a sex='M' -a StrkDist='40050' -o eleventwelveboysfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='11' -a highage='12' -a sex='M' -a StrkDist='50100' -o eleventwelveboysim.json -t json"], shell=True)
sleep(randint(15,45))

#1314 girls
call(["scrapy crawl ompaspider -a lowage='13' -a highage='14' -a sex='W' -a StrkDist='10050' -o thirteenfourteengirlsfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='13' -a highage='14' -a sex='W' -a StrkDist='30050' -o thirteenfourteengirlsbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='13' -a highage='14' -a sex='W' -a StrkDist='20050' -o thirteenfourteengirlsback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='13' -a highage='14' -a sex='W' -a StrkDist='40050' -o thirteenfourteengirlsfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='13' -a highage='14' -a sex='W' -a StrkDist='50100' -o thirteenfourteengirlsim.json -t json"], shell=True)
sleep(randint(15,45))

#1314 boys
call(["scrapy crawl ompaspider -a lowage='13' -a highage='14' -a sex='M' -a StrkDist='10050' -o thirteenfourteenboysfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='13' -a highage='14' -a sex='M' -a StrkDist='30050' -o thirteenfourteenboysbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='13' -a highage='14' -a sex='M' -a StrkDist='20050' -o thirteenfourteenboysback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='13' -a highage='14' -a sex='M' -a StrkDist='40050' -o thirteenfourteenboysfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='13' -a highage='14' -a sex='M' -a StrkDist='50100' -o thirteenfourteenboysim.json -t json"], shell=True)
sleep(randint(15,45))

#1518 girls
call(["scrapy crawl ompaspider -a lowage='15' -a highage='18' -a sex='W' -a StrkDist='10050' -o fifteeneighteengirlsfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='15' -a highage='18' -a sex='W' -a StrkDist='30050' -o fifteeneighteengirlsbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='15' -a highage='18' -a sex='W' -a StrkDist='20050' -o fifteeneighteengirlsback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='15' -a highage='18' -a sex='W' -a StrkDist='40050' -o fifteeneighteengirlsfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='15' -a highage='18' -a sex='W' -a StrkDist='50100' -o fifteeneighteengirlsim.json -t json"], shell=True)
sleep(randint(15,45))

#1518 boys
call(["scrapy crawl ompaspider -a lowage='15' -a highage='18' -a sex='M' -a StrkDist='10050' -o fifteeneighteenboysfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='15' -a highage='18' -a sex='M' -a StrkDist='30050' -o fifteeneighteenboysbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='15' -a highage='18' -a sex='M' -a StrkDist='20050' -o fifteeneighteenboysback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='15' -a highage='18' -a sex='M' -a StrkDist='40050' -o fifteeneighteenboysfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a lowage='15' -a highage='18' -a sex='M' -a StrkDist='50100' -o fifteeneighteenboysim.json -t json"], shell=True)
sleep(randint(15,45))