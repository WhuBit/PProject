
import requests
import os
from bs4 import BeautifulSoup


# headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'}
url = 'https://api.douban.com/v2/movie/subject/10001352'
fp = open(r'E:\Tag\host.txt','r')
f=open(r'E:\Tag\whost.txt','w')
ips = fp.readlines()
for p in ips:
    ip =p.strip('{}\n').split(':')
    proxy = 'http:\\' +  ip[0] + ':' + ip[1]
    proxies = {'proxy':proxy}
    try :
        s = requests.get(url,proxies = proxies).status_code
        print (s)
        if s==200:
            f.write(p)
    except Exception as e:
        print (e)

print 'over'