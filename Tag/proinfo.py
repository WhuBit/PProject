# -*- coding: UTF-8 -*- 
import sys  
reload(sys)  
sys.setdefaultencoding("utf-8")  

fw=open('E:\Tag\infon6-3.txt','w')
with open('E:\Tag\info6-3.txt') as f:
    line = f.readline().strip()
    while line:
        line = line.strip()
        info={}.fromkeys(['url','dirc','player','year','rate','type','area','name'])
        str=line.split('\t')
        if len(str)<3:
            line=f.readline()
            continue
        for word in str:
            if word:
                print word
        info['url']=str[0]
        info['name']=str[1].strip()
        info['year']=str[2].strip('()\r ')
        if len(str)>3:
            info['rate']=str[3].strip()
        line = f.readline()
        while line and not line.startswith('https:'):
            line=line.strip()
            print line
            if line.startswith('主演'):
                info['player']=line.split(':')[1]
            elif line.startswith('类型'):
                info['type']=line.split(':')[1]
            elif line.startswith('制片国家'):
                info['area']=line.split(':')[1]
            elif line.startswith('导演'):
                info['dirc']=line.split(':')[1]
            line = f.readline()
        print info
        fw.writelines("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n"%(info['url'], info['name'], info['year'], info['rate'], info['dirc'], info['player'], info['area'], info['type']))

        