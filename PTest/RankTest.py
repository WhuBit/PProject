# -- coding: UTF-8 --

'''
Created on 2017年4月30日

@author: Caesar
'''

import MySQLdb

print '正在连接数据库'
conn=MySQLdb.connect("localhost","root","1997syx","tag")
print '连接成功'
curs=conn.cursor()

for i in range(200):
    path=unicode('E:\Tag\MyTest\Type\Sim\用户'+str(i)+'相似度.txt',"UTF-8")
    for line in open(path):
        fiels=line.split('\t')
        curs.execute('INSERT INTO user'+str(i)+' VALUES(?,?,?)',fiels)
    
conn.commit()
conn.close()


