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
call(["scrapy crawl ompa2011spider -a lowage='0' -a highage='6' -a sex='Women' -a Stroke='Free' -a Distance='25' -o OMPA2011sixundergirlsfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompa2011spider -a lowage='0' -a highage='6' -a sex='Women' -a Stroke='Breast' -a Distance='25' -o OMPA2011sixundergirlsbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompa2011spider -a lowage='0' -a highage='6' -a sex='Women' -a Stroke='Back' -a Distance='25' -o OMPA2011sixundergirlsback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompa2011spider -a lowage='0' -a highage='6' -a sex='Women' -a Stroke='Fly' -a Distance='25' -o OMPA2011sixundergirlsfly.json -t json"], shell=True)
sleep(randint(15,45))

#6under boys free,breast,back,fly
call(["scrapy crawl ompa2011spider -a lowage='0' -a highage='6' -a sex='Men' -a Stroke ='Free' -a Distance='25' -o OMPA2011sixunderboysfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompa2011spider -a lowage='0' -a highage='6' -a sex='Men' -a Stroke='Breast' -a Distance='25' -o OMPA2011sixunderboysbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompa2011spider -a lowage='0' -a highage='6' -a sex='Men' -a Stroke='Back' -a Distance='25' -o OMPA2011sixunderboysback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompa2011spider -a lowage='0' -a highage='6' -a sex='Men' -a Stroke='Fly' -a Distance='25' -o OMPA2011sixunderboysfly.json -t json"], shell=True)
sleep(randint(15,45))

#78 girls free,breast,back,fly,im
call(["scrapy crawl ompa2011spider -a lowage='7' -a highage='8' -a sex='Women' -a Stroke='Free' -a Distance='25' -o OMPA2011seveneightgirlsfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompa2011spider -a lowage='7' -a highage='8' -a sex='Women' -a Stroke='Breast' -a Distance='25' -o OMPA2011seveneightgirlsbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompa2011spider -a lowage='7' -a highage='8' -a sex='Women' -a Stroke='Back' -a Distance='25' -o OMPA2011seveneightgirlsback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompa2011spider -a lowage='7' -a highage='8' -a sex='Women' -a Stroke='Fly' -a Distance='25' -o OMPA2011seveneightgirlsfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompa2011spider -a lowage='7' -a highage='8' -a sex='Women' -a Stroke='IM' -a Distance='100' -o OMPA2011seveneightgirlsim.json -t json"], shell=True)
sleep(randint(15,45))

#78 boys free,breast,back,fly,im
call(["scrapy crawl ompa2011spider -a lowage='7' -a highage='8' -a sex='Men' -a Stroke='Free' -a Distance='25' -o OMPA2011seveneightboysfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompa2011spider -a lowage='7' -a highage='8' -a sex='Men' -a Stroke='Breast' -a Distance='25' -o OMPA2011seveneightboysbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompa2011spider -a lowage='7' -a highage='8' -a sex='Men' -a Stroke='Back' -a Distance='25' -o OMPA2011seveneightboysback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompa2011spider -a lowage='7' -a highage='8' -a sex='Men' -a Stroke='Fly' -a Distance='25' -o OMPA2011seveneightboysfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompa2011spider -a lowage='7' -a highage='8' -a sex='Men' -a Stroke='IM' -a Distance='100' -o OMPA2011seveneightboysim.json -t json"], shell=True)
sleep(randint(15,45))

#910 girls free,breast,back,fly,im
call(["scrapy crawl ompa2011spider -a lowage='9' -a highage='10' -a sex='Women' -a Stroke='Free' -a Distance='50' -o OMPA2011ninetengirlsfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompa2011spider -a lowage='9' -a highage='10' -a sex='Women' -a Stroke='Breast' -a Distance='50' -o OMPA2011ninetengirlsbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompa2011spider -a lowage='9' -a highage='10' -a sex='Women' -a Stroke='Back' -a Distance='50' -o OMPA2011ninetengirlsback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompa2011spider -a lowage='9' -a highage='10' -a sex='Women' -a Stroke='Fly' -a Distance='50' -o OMPA2011ninetengirlsfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompa2011spider -a lowage='9' -a highage='10' -a sex='Women' -a Stroke='IM' -a Distance='100' -o OMPA2011ninetengirlsim.json -t json"], shell=True)
sleep(randint(15,45))

#910 boys
call(["scrapy crawl ompa2011spider -a lowage='9' -a highage='10' -a sex='Men' -a Stroke='Free' -a Distance='50' -o OMPA2011ninetenboysfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompa2011spider -a lowage='9' -a highage='10' -a sex='Men' -a Stroke='Breast' -a Distance='50' -o OPA2011ninetenboysbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompa2011spider -a lowage='9' -a highage='10' -a sex='Men' -a Stroke='Back' -a Distance='50' -o OMPA2011ninetenboysback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompa2011spider -a lowage='9' -a highage='10' -a sex='Men' -a Stroke='Fly' -a Distance='50' -o OMPA2011ninetenboysfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompa2011spider -a lowage='9' -a highage='10' -a sex='Men' -a Stroke='IM' -a Distance='100' -o OMPA2011ninetenboysim.json -t json"], shell=True)
sleep(randint(15,45))

#1112 girls
call(["scrapy crawl ompa2011spider -a lowage='11' -a highage='12' -a sex='Women' -a Stroke='Free' -a Distance='50' -o OMPA2011eleventwelvegirlsfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompa2011spider -a lowage='11' -a highage='12' -a sex='Women' -a Stroke='Breast' -a Distance='50' -o OMPA2011eleventwelvegirlsbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompa2011spider -a lowage='11' -a highage='12' -a sex='Women' -a Stroke='Back' -a Distance='50' -o OMPA2011eleventwelvegirlsback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompa2011spider -a lowage='11' -a highage='12' -a sex='Women' -a Stroke='Fly' -a Distance='50' -o OMPA2011eleventwelvegirlsfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompa2011spider -a lowage='11' -a highage='12' -a sex='Women' -a Stroke='IM' -a Distance='100' -o OMPA2011eleventwelvegirlsim.json -t json"], shell=True)
sleep(randint(15,45))

#1112 boys
call(["scrapy crawl ompa2011spider -a lowage='11' -a highage='12' -a sex='Men' -a Stroke='Free' -a Distance='50' -o OMPA2011eleventwelveboysfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompa2011spider -a lowage='11' -a highage='12' -a sex='Men' -a Stroke='Breast' -a Distance='50' -o OMPA2011eleventwelveboysbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompa2011spider -a lowage='11' -a highage='12' -a sex='Men' -a Stroke='Back' -a Distance='50' -o OMPA2011eleventwelveboysback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompa2011spider -a lowage='11' -a highage='12' -a sex='Men' -a Stroke='Fly' -a Distance='50' -o OMPA2011eleventwelveboysfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompa2011spider -a lowage='11' -a highage='12' -a sex='Men' -a Stroke='IM' -a Distance='100' -o OMPA2011eleventwelveboysim.json -t json"], shell=True)
sleep(randint(15,45))

#1314 girls
call(["scrapy crawl ompa2011spider -a lowage='13' -a highage='14' -a sex='Women' -a Stroke='Free' -a Distance='50' -o OMPA2011thirteenfourteengirlsfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompa2011spider -a lowage='13' -a highage='14' -a sex='Women' -a Stroke='Breast' -a Distance='50' -o OMPA2011thirteenfourteengirlsbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompa2011spider -a lowage='13' -a highage='14' -a sex='Women' -a Stroke='Back' -a Distance='50' -o OMPA2011thirteenfourteengirlsback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompa2011spider -a lowage='13' -a highage='14' -a sex='Women' -a Stroke='Fly' -a Distance='50' -o OMPA2011thirteenfourteengirlsfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompa2011spider -a lowage='13' -a highage='14' -a sex='Women' -a Stroke='IM' -a Distance='100' -o OMPA2011thirteenfourteengirlsim.json -t json"], shell=True)
sleep(randint(15,45))

#1314 boys
call(["scrapy crawl ompa2011spider -a lowage='13' -a highage='14' -a sex='Men' -a Stroke='Free' -a Distance='50' -o OMPA2011thirteenfourteenboysfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompa2011spider -a lowage='13' -a highage='14' -a sex='Men' -a Stroke='Breast' -a Distance='50' -o OMPA2011thirteenfourteenboysbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompa2011spider -a lowage='13' -a highage='14' -a sex='Men' -a Stroke='Back' -a Distance='50' -o OMPA2011thirteenfourteenboysback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompa2011spider -a lowage='13' -a highage='14' -a sex='Men' -a Stroke='Fly' -a Distance='50' -o OMPA2011thirteenfourteenboysfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompa2011spider -a lowage='13' -a highage='14' -a sex='Men' -a Stroke='IM' -a Distance='100' -o OMPA2011thirteenfourteenboysim.json -t json"], shell=True)
sleep(randint(15,45))

#1518 girls
call(["scrapy crawl ompa2011spider -a lowage='15' -a highage='18' -a sex='Women' -a Stroke='Free' -a Distance='50' -o OMPA2011fifteeneighteengirlsfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompa2011spider -a lowage='15' -a highage='18' -a sex='Women' -a Stroke='Breast' -a Distance='50' -o OMPA2011fifteeneighteengirlsbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompa2011spider -a lowage='15' -a highage='18' -a sex='Women' -a Stroke='Back' -a Distance='50' -o OMPA2011fifteeneighteengirlsback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompa2011spider -a lowage='15' -a highage='18' -a sex='Women' -a Stroke='Fly' -a Distance='50' -o OMPA2011fifteeneighteengirlsfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompa2011spider -a lowage='15' -a highage='18' -a sex='Women' -a Stroke='IM' -a Distance='100' -o OMPA2011fifteeneighteengirlsim.json -t json"], shell=True)
sleep(randint(15,45))

#1518 boys
call(["scrapy crawl ompa2011spider -a lowage='15' -a highage='18' -a sex='Men' -a Stroke='Free' -a Distance='50' -o OMPA2011fifteeneighteenboysfree.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompa2011spider -a lowage='15' -a highage='18' -a sex='Men' -a Stroke='Breast' -a Distance='50' -o OMPA2011fifteeneighteenboysbreast.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompa2011spider -a lowage='15' -a highage='18' -a sex='Men' -a Stroke='Back' -a Distance='50' -o OMPA2011fifteeneighteenboysback.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompa2011spider -a lowage='15' -a highage='18' -a sex='Men' -a Stroke='Fly' -a Distance='50' -o OMPA2011fifteeneighteenboysfly.json -t json"], shell=True)
sleep(randint(15,45))
call(["scrapy crawl ompa2011spider -a lowage='15' -a highage='18' -a sex='Men' -a Stroke='IM' -a Distance='100' -o OMPA2011fifteeneighteenboysim.json -t json"], shell=True)
sleep(randint(15,45))