# coding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

'''
Created on 2017年6月13日
@author: Caesar
'''

import requests
from lxml import etree
import re

TV_RUNTIME_RE = re.compile(ur'单集片长: (\d+)')
LANGUAGES_RE = re.compile(ur"语言:</span> (.+?)<br>")
COUNTRIES_RE = re.compile(ur"制片国家/地区:</span> (.+?)<br>")
NUM_RE = re.compile(r"(\d+)")

sel=requests.get('https://movie.douban.com/subject/10001352/')
response=etree.HTML(sel.text)

name = response.xpath("//title/text()")
if name: print name[0].replace(u" (豆瓣)", "").strip()

year = response.xpath("//span[@class='year']")
if year: print basestring(year[0])

directors = response.xpath("//a[@rel='v:directedBy']/text()").extract()
if directors: print directors

stars = response.xpath("//a[@rel='v:starring']/text()").extract()
if stars: print stars

genres = response.xpath("//span[@property='v:genre']/text()").extract()
if genres: print genres

average = response.xpath("//strong[@property='v:average']/text()").extract()
if average and average[0] != "": print float( average[0] ) + 0.0

S = "".join(response.xpath("//div[@id='info']").extract() )
M = COUNTRIES_RE.search(S)
if M is not None:
    print [ country.strip() for country in M.group(1).split("/") ]
