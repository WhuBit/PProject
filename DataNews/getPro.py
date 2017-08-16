# ---coding:utf-8---
import urllib2
import json
import csv

key='Dle3ghve9A5rdKBp3o2SsCSFA0hBgUY1'
f=open(r'E:\\cinema_pro.csv','a')
writer = csv.writer(f)
with open(r'E:\\cinema2.csv') as csvfile: 
    print 'reading...'
    reader = csv.reader(csvfile)
    print 'end'
    for line in reader: 
        if line[6] and line[7]:
            lon = line[6].strip()
            lat= line[7].strip()
            url='http://api.map.baidu.com/geocoder/v2/?callback=renderReverse&location='+str(lat)+','+str(lon)+'&output=json&ak='+key
            js = json.loads(urllib2.urlopen(url).read().strip('renderReverse&&renderReverse()'))
            line.append(js['result']['addressComponent']['province'].encode('utf-8'))
            print line
            writer.writerow(line)
print 'end'