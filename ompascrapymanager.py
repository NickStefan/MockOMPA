#!/usr/bin/python

#scrapymanager repeatedly deploys web crawler contained in folder /ompa/

from random import randint
from time import sleep
from subprocess import call

#deletes json file
#call(["rm items.json"], shell=True)

#proxy for counting number of swimmers per team
# 8under freestyle girls and boys
# 9up freestyle girls and boys
call(["scrapy crawl countspider -a ttloage='3' -a tthiage='8' -a ttgenders='F' -a ttstrokes='1' -a ttdistances='25' -o JSONdata/count/eightundergirlsfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl countspider -a ttloage='3' -a tthiage='8' -a ttgenders='M' -a ttstrokes='1' -a ttdistances='25' -o JSONdata/count/eightunderboysfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl countspider -a ttloage='9' -a tthiage='18' -a ttgenders='F' -a ttstrokes='1' -a ttdistances='50' -o JSONdata/count/nineupgirlsfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl countspider -a ttloage='9' -a tthiage='18' -a ttgenders='M' -a ttstrokes='1' -a ttdistances='50' -o JSONdata/count/nineupboysfree.json -t json"], shell=True)
sleep(randint(15,45))

# get the actual data for the scoring program
#6under girls free,breast,back,fly
call(["scrapy crawl ompaspider -a ttloage='3' -a tthiage='6' -a ttgenders='F' -a ttstrokes='1' -a ttdistances='25' -o JSONdata/sixundergirlsfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='3' -a tthiage='6' -a ttgenders='F' -a ttstrokes='3' -a ttdistances='25' -o JSONdata/sixundergirlsbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='3' -a tthiage='6' -a ttgenders='F' -a ttstrokes='2' -a ttdistances='25' -o JSONdata/sixundergirlsback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='3' -a tthiage='6' -a ttgenders='F' -a ttstrokes='4' -a ttdistances='25' -o JSONdata/sixundergirlsfly.json -t json"], shell=True)
sleep(randint(15,45))

#6under boys free,breast,back,fly
call(["scrapy crawl ompaspider -a ttloage='3' -a tthiage='6' -a ttgenders='M' -a ttstrokes='1' -a ttdistances='25' -o JSONdata/sixunderboysfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='3' -a tthiage='6' -a ttgenders='M' -a ttstrokes='3' -a ttdistances='25' -o JSONdata/sixunderboysbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='3' -a tthiage='6' -a ttgenders='M' -a ttstrokes='2' -a ttdistances='25' -o JSONdata/sixunderboysback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='3' -a tthiage='6' -a ttgenders='M' -a ttstrokes='4' -a ttdistances='25' -o JSONdata/sixunderboysfly.json -t json"], shell=True)
sleep(randint(15,45))

#78 girls free,breast,back,fly,im
call(["scrapy crawl ompaspider -a ttloage='7' -a tthiage='8' -a ttgenders='F' -a ttstrokes='1' -a ttdistances='25' -o JSONdata/seveneightgirlsfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='7' -a tthiage='8' -a ttgenders='F' -a ttstrokes='3' -a ttdistances='25' -o JSONdata/seveneightgirlsbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='7' -a tthiage='8' -a ttgenders='F' -a ttstrokes='2' -a ttdistances='25' -o JSONdata/seveneightgirlsback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='7' -a tthiage='8' -a ttgenders='F' -a ttstrokes='4' -a ttdistances='25' -o JSONdata/seveneightgirlsfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='7' -a tthiage='8' -a ttgenders='F' -a ttstrokes='5' -a ttdistances='100' -o JSONdata/seveneightgirlsim.json -t json"], shell=True)
sleep(randint(15,45))

#78 boys free,breast,back,fly,im
call(["scrapy crawl ompaspider -a ttloage='7' -a tthiage='8' -a ttgenders='M' -a ttstrokes='1' -a ttdistances='25' -o JSONdata/seveneightboysfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='7' -a tthiage='8' -a ttgenders='M' -a ttstrokes='3' -a ttdistances='25' -o JSONdata/seveneightboysbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='7' -a tthiage='8' -a ttgenders='M' -a ttstrokes='2' -a ttdistances='25' -o JSONdata/seveneightboysback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='7' -a tthiage='8' -a ttgenders='M' -a ttstrokes='4' -a ttdistances='25' -o JSONdata/seveneightboysfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='7' -a tthiage='8' -a ttgenders='M' -a ttstrokes='5' -a ttdistances='100' -o JSONdata/seveneightboysim.json -t json"], shell=True)
sleep(randint(15,45))

#910 girls free,breast,back,fly,im
call(["scrapy crawl ompaspider -a ttloage='9' -a tthiage='10' -a ttgenders='F' -a ttstrokes='1' -a ttdistances='50' -o JSONdata/ninetengirlsfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='9' -a tthiage='10' -a ttgenders='F' -a ttstrokes='3' -a ttdistances='50' -o JSONdata/ninetengirlsbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='9' -a tthiage='10' -a ttgenders='F' -a ttstrokes='2' -a ttdistances='50' -o JSONdata/ninetengirlsback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='9' -a tthiage='10' -a ttgenders='F' -a ttstrokes='4' -a ttdistances='50' -o JSONdata/ninetengirlsfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='9' -a tthiage='10' -a ttgenders='F' -a ttstrokes='5' -a ttdistances='100' -o JSONdata/ninetengirlsim.json -t json"], shell=True)
sleep(randint(15,45))

#910 boys
call(["scrapy crawl ompaspider -a ttloage='9' -a tthiage='10' -a ttgenders='M' -a ttstrokes='1' -a ttdistances='50' -o JSONdata/ninetenboysfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='9' -a tthiage='10' -a ttgenders='M' -a ttstrokes='3' -a ttdistances='50' -o JSONdata/ninetenboysbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='9' -a tthiage='10' -a ttgenders='M' -a ttstrokes='2' -a ttdistances='50' -o JSONdata/ninetenboysback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='9' -a tthiage='10' -a ttgenders='M' -a ttstrokes='4' -a ttdistances='50' -o JSONdata/ninetenboysfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='9' -a tthiage='10' -a ttgenders='M' -a ttstrokes='5' -a ttdistances='100' -o JSONdata/ninetenboysim.json -t json"], shell=True)
sleep(randint(15,45))

#1112 girls
call(["scrapy crawl ompaspider -a ttloage='11' -a tthiage='12' -a ttgenders='F' -a ttstrokes='1' -a ttdistances='50' -o JSONdata/eleventwelvegirlsfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='11' -a tthiage='12' -a ttgenders='F' -a ttstrokes='3' -a ttdistances='50' -o JSONdata/eleventwelvegirlsbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='11' -a tthiage='12' -a ttgenders='F' -a ttstrokes='2' -a ttdistances='50' -o JSONdata/eleventwelvegirlsback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='11' -a tthiage='12' -a ttgenders='F' -a ttstrokes='4' -a ttdistances='50' -o JSONdata/eleventwelvegirlsfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='11' -a tthiage='12' -a ttgenders='F' -a ttstrokes='5' -a ttdistances='100' -o JSONdata/eleventwelvegirlsim.json -t json"], shell=True)
sleep(randint(15,45))

#1112 boys
call(["scrapy crawl ompaspider -a ttloage='11' -a tthiage='12' -a ttgenders='M' -a ttstrokes='1' -a ttdistances='50' -o JSONdata/eleventwelveboysfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='11' -a tthiage='12' -a ttgenders='M' -a ttstrokes='3' -a ttdistances='50' -o JSONdata/eleventwelveboysbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='11' -a tthiage='12' -a ttgenders='M' -a ttstrokes='2' -a ttdistances='50' -o JSONdata/eleventwelveboysback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='11' -a tthiage='12' -a ttgenders='M' -a ttstrokes='4' -a ttdistances='50' -o JSONdata/eleventwelveboysfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='11' -a tthiage='12' -a ttgenders='M' -a ttstrokes='5' -a ttdistances='100' -o JSONdata/eleventwelveboysim.json -t json"], shell=True)
sleep(randint(15,45))

#1314 girls
call(["scrapy crawl ompaspider -a ttloage='13' -a tthiage='14' -a ttgenders='F' -a ttstrokes='1' -a ttdistances='50' -o JSONdata/thirteenfourteengirlsfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='13' -a tthiage='14' -a ttgenders='F' -a ttstrokes='3' -a ttdistances='50' -o JSONdata/thirteenfourteengirlsbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='13' -a tthiage='14' -a ttgenders='F' -a ttstrokes='2' -a ttdistances='50' -o JSONdata/thirteenfourteengirlsback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='13' -a tthiage='14' -a ttgenders='F' -a ttstrokes='4' -a ttdistances='50' -o JSONdata/thirteenfourteengirlsfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='13' -a tthiage='14' -a ttgenders='F' -a ttstrokes='5' -a ttdistances='100' -o JSONdata/thirteenfourteengirlsim.json -t json"], shell=True)
sleep(randint(15,45))

#1314 boys
call(["scrapy crawl ompaspider -a ttloage='13' -a tthiage='14' -a ttgenders='M' -a ttstrokes='1' -a ttdistances='50' -o JSONdata/thirteenfourteenboysfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='13' -a tthiage='14' -a ttgenders='M' -a ttstrokes='3' -a ttdistances='50' -o JSONdata/thirteenfourteenboysbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='13' -a tthiage='14' -a ttgenders='M' -a ttstrokes='2' -a ttdistances='50' -o JSONdata/thirteenfourteenboysback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='13' -a tthiage='14' -a ttgenders='M' -a ttstrokes='4' -a ttdistances='50' -o JSONdata/thirteenfourteenboysfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='13' -a tthiage='14' -a ttgenders='M' -a ttstrokes='5' -a ttdistances='100' -o JSONdata/thirteenfourteenboysim.json -t json"], shell=True)
sleep(randint(15,45))

#1518 girls
call(["scrapy crawl ompaspider -a ttloage='15' -a tthiage='18' -a ttgenders='F' -a ttstrokes='1' -a ttdistances='50' -o JSONdata/fifteeneighteengirlsfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='15' -a tthiage='18' -a ttgenders='F' -a ttstrokes='3' -a ttdistances='50' -o JSONdata/fifteeneighteengirlsbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='15' -a tthiage='18' -a ttgenders='F' -a ttstrokes='2' -a ttdistances='50' -o JSONdata/fifteeneighteengirlsback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='15' -a tthiage='18' -a ttgenders='F' -a ttstrokes='4' -a ttdistances='50' -o JSONdata/fifteeneighteengirlsfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='15' -a tthiage='18' -a ttgenders='F' -a ttstrokes='5' -a ttdistances='100' -o JSONdata/fifteeneighteengirlsim.json -t json"], shell=True)
sleep(randint(15,45))

#1518 boys
call(["scrapy crawl ompaspider -a ttloage='15' -a tthiage='18' -a ttgenders='M' -a ttstrokes='1' -a ttdistances='50' -o JSONdata/fifteeneighteenboysfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='15' -a tthiage='18' -a ttgenders='M' -a ttstrokes='3' -a ttdistances='50' -o JSONdata/fifteeneighteenboysbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='15' -a tthiage='18' -a ttgenders='M' -a ttstrokes='2' -a ttdistances='50' -o JSONdata/fifteeneighteenboysback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='15' -a tthiage='18' -a ttgenders='M' -a ttstrokes='4' -a ttdistances='50' -o JSONdata/fifteeneighteenboysfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompaspider -a ttloage='15' -a tthiage='18' -a ttgenders='M' -a ttstrokes='5' -a ttdistances='100' -o JSONdata/fifteeneighteenboysim.json -t json"], shell=True)
sleep(randint(15,45))