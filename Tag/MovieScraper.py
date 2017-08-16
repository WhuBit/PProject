# -*- coding: UTF-8 -*-

'''
Created on 2017年6月10日

@author: Caesar
'''

import requests
from bs4 import BeautifulSoup

#模拟登陆
s=requests.session()
hostUrl='http://douban.fm/'
user_agent='Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0'
headers={'User-Agent':user_agent,
        'Connection':'keep-alive',
        'Referer': hostUrl}
postdata={'form_email':'774534486@qq.com','form_password':'19971009syx'}
res=s.post('https://www.douban.com/accounts/login', data=postdata,headers=headers)

#获取URL列表
f1=open(r'E:\Tag\url.txt')
f2=open(r'E:\Tag\MovieInfo.txt','w')
for line in f1:
    movieUrl=line
    result=s.get(movieUrl,headers)
    print result.text
    soup=BeautifulSoup(result.text)
    h1=soup.h1
    if(not h1):
        continue
    title=h1.get_text('\t',strip=True)
    info=soup.select('div#info')[0].get_text('\t',strip=True).replace(':','').split('\t')

    dirc=''
    player=''
    mtype=''
    area=''

    for i in range(len(info)):
        if(info[i].encode('utf-8')=='导演'):
            while(info[i+1].encode('utf-8')!='编剧' and info[i+1].encode('utf-8')!='主演' and info[i+1].encode('utf-8')!='类型' and i+1<len(info)):
                dirc+=info[i+1]
                i=i+1
            
        if(info[i].encode('utf-8')=='主演'):
            while(info[i+1].encode('utf-8')!='类型' and i+1<len(info)):
                player+=info[i+1]
                i=i+1
            
        if(info[i].encode('utf-8')=='类型'):
            while(info[i+1].encode('utf-8')!='官方网站' and info[i+1].encode('utf-8')!=r'制片国家/地区' and i+1<len(info)):
                mtype+=info[i+1]
                i=i+1
            
        if(info[i].encode('utf-8')==r'制片国家/地区'):
            while(info[i+1].encode('utf-8')!='语言' and info[i+1].encode('utf-8')!='IMDb链接' and i+1<len(info)):
                area+=info[i+1]
                i=i+1
            
    if(not dirc):
        dirc='None'
    if(not player):
        player='None'
    if(not mtype):
        mtype='None'
    if(not area):
        area='None'
    
    rate=soup.strong.get_text()
    if(not rate):
        rate='None'

    movieInfo=movieUrl+'\t'+title+'\t'+dirc+'\t'+player+'\t'+mtype+'\t'+area+'\t'+rate
    print movieInfo
    
    f2.write(movieInfo+'\n')
    
f1.close()