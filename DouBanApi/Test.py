# ---coding:utf-8---
import urllib2
import json

js = json.loads(urllib2.urlopen('https://api.douban.com/v2/movie/25786060').read())
print js
print js['title'], '\t', js['attrs']['year'], '\t',js['rating']['average']
for one in js['attrs']['movie_type']:
    print one.strip(),','
for one in js['attrs']['country']:
    print one.strip(),','
for one in js['attrs']['director']:
    print one.strip()+','
for one in js['attrs']['cast']:
    print one.strip()+','
print 'over!'