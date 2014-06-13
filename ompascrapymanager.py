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
call(["scrapy crawl ompaspider -a ttloage='3' -a tthiage='6' -a ttgenders='F' -a ttstrokes='1' -a ttdistances='25' -o sixundergirlsfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='3' -a tthiage='6' -a ttgenders='F' -a ttstrokes='3' -a ttdistances='25' -o sixundergirlsbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='3' -a tthiage='6' -a ttgenders='F' -a ttstrokes='2' -a ttdistances='25' -o sixundergirlsback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='3' -a tthiage='6' -a ttgenders='F' -a ttstrokes='4' -a ttdistances='25' -o sixundergirlsfly.json -t json"], shell=True)
sleep(randint(15,45))

#6under boys free,breast,back,fly
call(["scrapy crawl ompaspider -a ttloage='3' -a tthiage='6' -a ttgenders='M' -a ttstrokes='1' -a ttdistances='25' -o sixunderboysfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='3' -a tthiage='6' -a ttgenders='M' -a ttstrokes='3' -a ttdistances='25' -o sixunderboysbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='3' -a tthiage='6' -a ttgenders='M' -a ttstrokes='2' -a ttdistances='25' -o sixunderboysback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='3' -a tthiage='6' -a ttgenders='M' -a ttstrokes='4' -a ttdistances='25' -o sixunderboysfly.json -t json"], shell=True)
sleep(randint(15,45))

#78 girls free,breast,back,fly,im
call(["scrapy crawl ompaspider -a ttloage='7' -a tthiage='8' -a ttgenders='F' -a ttstrokes='1' -a ttdistances='25' -o seveneightgirlsfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='7' -a tthiage='8' -a ttgenders='F' -a ttstrokes='3' -a ttdistances='25' -o seveneightgirlsbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='7' -a tthiage='8' -a ttgenders='F' -a ttstrokes='2' -a ttdistances='25' -o seveneightgirlsback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='7' -a tthiage='8' -a ttgenders='F' -a ttstrokes='4' -a ttdistances='25' -o seveneightgirlsfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='7' -a tthiage='8' -a ttgenders='F' -a ttstrokes='5' -a ttdistances='100' -o seveneightgirlsim.json -t json"], shell=True)
sleep(randint(15,45))

#78 boys free,breast,back,fly,im
call(["scrapy crawl ompaspider -a ttloage='7' -a tthiage='8' -a ttgenders='M' -a ttstrokes='1' -a ttdistances='25' -o seveneightboysfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='7' -a tthiage='8' -a ttgenders='M' -a ttstrokes='3' -a ttdistances='25' -o seveneightboysbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='7' -a tthiage='8' -a ttgenders='M' -a ttstrokes='2' -a ttdistances='25' -o seveneightboysback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='7' -a tthiage='8' -a ttgenders='M' -a ttstrokes='4' -a ttdistances='25' -o seveneightboysfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='7' -a tthiage='8' -a ttgenders='M' -a ttstrokes='5' -a ttdistances='100' -o seveneightboysim.json -t json"], shell=True)
sleep(randint(15,45))

#910 girls free,breast,back,fly,im
call(["scrapy crawl ompaspider -a ttloage='9' -a tthiage='10' -a ttgenders='F' -a ttstrokes='1' -a ttdistances='50' -o ninetengirlsfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='9' -a tthiage='10' -a ttgenders='F' -a ttstrokes='3' -a ttdistances='50' -o ninetengirlsbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='9' -a tthiage='10' -a ttgenders='F' -a ttstrokes='2' -a ttdistances='50' -o ninetengirlsback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='9' -a tthiage='10' -a ttgenders='F' -a ttstrokes='4' -a ttdistances='50' -o ninetengirlsfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='9' -a tthiage='10' -a ttgenders='F' -a ttstrokes='5' -a ttdistances='100' -o ninetengirlsim.json -t json"], shell=True)
sleep(randint(15,45))

#910 boys
call(["scrapy crawl ompaspider -a ttloage='9' -a tthiage='10' -a ttgenders='M' -a ttstrokes='1' -a ttdistances='50' -o ninetenboysfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='9' -a tthiage='10' -a ttgenders='M' -a ttstrokes='3' -a ttdistances='50' -o ninetenboysbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='9' -a tthiage='10' -a ttgenders='M' -a ttstrokes='2' -a ttdistances='50' -o ninetenboysback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='9' -a tthiage='10' -a ttgenders='M' -a ttstrokes='4' -a ttdistances='50' -o ninetenboysfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='9' -a tthiage='10' -a ttgenders='M' -a ttstrokes='5' -a ttdistances='100' -o ninetenboysim.json -t json"], shell=True)
sleep(randint(15,45))

#1112 girls
call(["scrapy crawl ompaspider -a ttloage='11' -a tthiage='12' -a ttgenders='F' -a ttstrokes='1' -a ttdistances='50' -o eleventwelvegirlsfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='11' -a tthiage='12' -a ttgenders='F' -a ttstrokes='3' -a ttdistances='50' -o eleventwelvegirlsbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='11' -a tthiage='12' -a ttgenders='F' -a ttstrokes='2' -a ttdistances='50' -o eleventwelvegirlsback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='11' -a tthiage='12' -a ttgenders='F' -a ttstrokes='4' -a ttdistances='50' -o eleventwelvegirlsfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='11' -a tthiage='12' -a ttgenders='F' -a ttstrokes='5' -a ttdistances='100' -o eleventwelvegirlsim.json -t json"], shell=True)
sleep(randint(15,45))

#1112 boys
call(["scrapy crawl ompaspider -a ttloage='11' -a tthiage='12' -a ttgenders='M' -a ttstrokes='1' -a ttdistances='50' -o eleventwelveboysfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='11' -a tthiage='12' -a ttgenders='M' -a ttstrokes='3' -a ttdistances='50' -o eleventwelveboysbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='11' -a tthiage='12' -a ttgenders='M' -a ttstrokes='2' -a ttdistances='50' -o eleventwelveboysback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='11' -a tthiage='12' -a ttgenders='M' -a ttstrokes='4' -a ttdistances='50' -o eleventwelveboysfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='11' -a tthiage='12' -a ttgenders='M' -a ttstrokes='5' -a ttdistances='100' -o eleventwelveboysim.json -t json"], shell=True)
sleep(randint(15,45))

#1314 girls
call(["scrapy crawl ompaspider -a ttloage='13' -a tthiage='14' -a ttgenders='F' -a ttstrokes='1' -a ttdistances='50' -o thirteenfourteengirlsfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='13' -a tthiage='14' -a ttgenders='F' -a ttstrokes='3' -a ttdistances='50' -o thirteenfourteengirlsbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='13' -a tthiage='14' -a ttgenders='F' -a ttstrokes='2' -a ttdistances='50' -o thirteenfourteengirlsback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='13' -a tthiage='14' -a ttgenders='F' -a ttstrokes='4' -a ttdistances='50' -o thirteenfourteengirlsfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='13' -a tthiage='14' -a ttgenders='F' -a ttstrokes='5' -a ttdistances='100' -o thirteenfourteengirlsim.json -t json"], shell=True)
sleep(randint(15,45))

#1314 boys
call(["scrapy crawl ompaspider -a ttloage='13' -a tthiage='14' -a ttgenders='M' -a ttstrokes='1' -a ttdistances='50' -o thirteenfourteenboysfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='13' -a tthiage='14' -a ttgenders='M' -a ttstrokes='3' -a ttdistances='50' -o thirteenfourteenboysbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='13' -a tthiage='14' -a ttgenders='M' -a ttstrokes='2' -a ttdistances='50' -o thirteenfourteenboysback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='13' -a tthiage='14' -a ttgenders='M' -a ttstrokes='4' -a ttdistances='50' -o thirteenfourteenboysfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='13' -a tthiage='14' -a ttgenders='M' -a ttstrokes='5' -a ttdistances='100' -o thirteenfourteenboysim.json -t json"], shell=True)
sleep(randint(15,45))

#1518 girls
call(["scrapy crawl ompaspider -a ttloage='15' -a tthiage='18' -a ttgenders='F' -a ttstrokes='1' -a ttdistances='50' -o fifteeneighteengirlsfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='15' -a tthiage='18' -a ttgenders='F' -a ttstrokes='3' -a ttdistances='50' -o fifteeneighteengirlsbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='15' -a tthiage='18' -a ttgenders='F' -a ttstrokes='2' -a ttdistances='50' -o fifteeneighteengirlsback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='15' -a tthiage='18' -a ttgenders='F' -a ttstrokes='4' -a ttdistances='50' -o fifteeneighteengirlsfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='15' -a tthiage='18' -a ttgenders='F' -a ttstrokes='5' -a ttdistances='100' -o fifteeneighteengirlsim.json -t json"], shell=True)
sleep(randint(15,45))

#1518 boys
call(["scrapy crawl ompaspider -a ttloage='15' -a tthiage='18' -a ttgenders='M' -a ttstrokes='1' -a ttdistances='50' -o fifteeneighteenboysfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='15' -a tthiage='18' -a ttgenders='M' -a ttstrokes='3' -a ttdistances='50' -o fifteeneighteenboysbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='15' -a tthiage='18' -a ttgenders='M' -a ttstrokes='2' -a ttdistances='50' -o fifteeneighteenboysback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='15' -a tthiage='18' -a ttgenders='M' -a ttstrokes='4' -a ttdistances='50' -o fifteeneighteenboysfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='15' -a tthiage='18' -a ttgenders='M' -a ttstrokes='5' -a ttdistances='100' -o fifteeneighteenboysim.json -t json"], shell=True)
sleep(randint(15,45))